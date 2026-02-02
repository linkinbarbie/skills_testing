---
name: qa-triage
description: Triage test failures and flaky tests in this repo. Use when a user asks to investigate failing CI, interpret test output, or suggest fixes for flaky tests.
---

# QA Triage

## Quick Start
- Read failing test output or CI logs first.
- Identify the failing test file and error message.
- Run the smallest relevant test command locally.

## Repo Commands
- See `references/test-commands.md` for exact commands.

## Fix Guidance
- Prefer minimal fixes that preserve test intent.
- If a test is flaky, propose stabilization before skipping.
