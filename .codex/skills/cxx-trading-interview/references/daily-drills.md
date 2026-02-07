# 7-Day C++ Trading Interview Drills

Use 30–60 minutes per day. Keep answers short and specific.

## Day 1: C++ Core + STL
- Explain stack vs heap; when does allocation happen?
- `vector` vs `deque` vs `list` tradeoffs.
- RAII and why it matters in low-latency systems.
- What is move semantics? Give a simple example.

## Day 2: Concurrency Basics
- Difference between `mutex`, `spinlock`, and `shared_mutex`.
- What is false sharing? How to avoid it.
- How to safely pass data between threads.
- When would you use lock-free structures?

## Day 3: Latency & Performance
- Where does latency come from in trading systems?
- What is cache locality? Why does it matter?
- How to profile a slow C++ path.
- What is the cost of a system call?

## Day 4: Market Data + Order Books
- What is a limit order book?
- Describe how you would maintain top-of-book.
- How to handle out-of-order market data updates.
- Difference between snapshot vs incremental updates.

## Day 5: System Design (Trading)
- Design a market data handler in C++.
- Design a simple matching engine.
- Where do you put risk checks?
- What should be logged for auditability?

## Day 6: Testing + Migration
- How to validate parity between legacy and new system.
- What tests would you automate first?
- What metrics show the migration is safe?
- How to roll back safely.

## Day 7: Mock Interview
- 3 technical questions (rotate from above).
- 1 coding question (order book update or ring buffer).
- 1 system design question (latency-sensitive pipeline).
- 1 behavioral: handling a production incident.
