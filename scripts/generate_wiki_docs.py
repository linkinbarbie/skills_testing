import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return text
    return parts[2].lstrip()


def build_prompt(readme: str, skills: str, skill_body: str) -> str:
    instructions = (
        "You are a documentation writer. Follow the docs-helper skill instructions below. "
        "Write a concise technical wiki page in Markdown for this repo. "
        "Use short headings and bullet points. "
        "Do not include raw file dumps. "
        "Keep it under 400 words."
    )
    return (
        f"{instructions}\n\n"
        "docs-helper SKILL.md (body):\n"
        f"{skill_body}\n\n"
        "README.md:\n"
        f"{readme}\n\n"
        "SKILLS.md:\n"
        f"{skills}\n"
    )


def call_openai(api_key: str, model: str, prompt: str, max_output_tokens: int) -> str:
    url = "https://api.openai.com/v1/responses"
    payload = {
        "model": model,
        "input": prompt,
        "max_output_tokens": max_output_tokens,
    }
    data = json.dumps(payload).encode("utf-8")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    attempts = 5
    backoff = 2.0
    last_error = None
    for i in range(attempts):
        req = urllib.request.Request(
            url,
            data=data,
            headers=headers,
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                body = resp.read().decode("utf-8")
            response = json.loads(body)
            break
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code == 429 or 500 <= exc.code < 600:
                time.sleep(backoff)
                backoff *= 2
                continue
            raise
    else:
        raise last_error

    if isinstance(response, dict) and "output_text" in response:
        return response["output_text"]

    chunks = []
    for item in response.get("output", []):
        for content in item.get("content", []):
            if content.get("type") == "output_text":
                chunks.append(content.get("text", ""))
    return "\n".join(chunks).strip()


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    readme_path = repo_root / "README.md"
    skills_path = repo_root / "SKILLS.md"
    skill_path = repo_root / ".codex" / "skills" / "docs-helper" / "SKILL.md"

    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini").strip()
    max_output_tokens = int(os.environ.get("MAX_OUTPUT_TOKENS", "800"))
    output_path = Path(os.environ.get("OUTPUT_PATH", str(repo_root / "generated" / "Repo-Docs.md")))

    if not api_key:
        print("OPENAI_API_KEY is required.", file=sys.stderr)
        return 2

    readme = read_text(readme_path)
    skills = read_text(skills_path)
    skill_body = strip_frontmatter(read_text(skill_path)) if skill_path.exists() else ""

    prompt = build_prompt(readme, skills, skill_body)
    output = call_openai(api_key, model, prompt, max_output_tokens)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output + "\n", encoding="utf-8")
    print(f"Wrote wiki doc to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
