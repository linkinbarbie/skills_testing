---
name: cxx-trading-interview
description: C++ trading-platform interview preparation focused on low-latency design, market data, order books, concurrency, and practical coding drills. Use when preparing for interviews in electronic trading, market-making, macro flow systems, or latency-sensitive C++ roles, especially for structured practice, mock Q&A, or a small project outline.
---

# C++ Trading Interview

## Overview
Run a focused, one-week prep routine for C++ trading interviews, with daily drills and a tiny trading-platform project you can explain in interviews.

## Quick Start
- Ask how many days remain and which areas are weakest.
- Use `references/daily-drills.md` for the daily Q&A blocks.
- If they want a portfolio signal, use `references/project-outline.md`.
- Keep answers concrete: short definitions, examples, and pitfalls.

## Interview Flow (Use This Order)
1. Clarify role: low-latency C++? macro flow? risk? tooling?
2. Run 3 short Q&A drills (see `references/daily-drills.md`).
3. Do 1 coding exercise (STL + concurrency + latency awareness).
4. Summarize gaps and give a 24-hour plan.

## What Good Answers Look Like
- Emphasize correctness first, then performance.
- Mention data structures + time complexity.
- Show awareness of latency sources: allocation, locks, cache misses, syscalls.
- Keep to practical, interview-sized code.

## When To Use The Project Outline
Use `references/project-outline.md` if the user wants a concrete portfolio example to discuss (order book + matching + metrics).

## References
- `references/daily-drills.md` for 7-day Q&A drills.
- `references/project-outline.md` for a tiny C++ trading-platform project.
