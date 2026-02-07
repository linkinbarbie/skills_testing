# Tiny C++ Trading-Platform Project (2–3 Days)

Goal: Build a small project you can describe in interviews.

## Scope (Keep It Small)
- Parse simple market data lines.
- Maintain a top-of-book.
- Support add/modify/cancel orders.
- Provide basic latency stats.

## Suggested Components
1. **OrderBook**
   - Data structures for bids/asks.
   - Update API: add/modify/cancel.

2. **MarketDataParser**
   - Parse CSV lines into updates.
   - Validate sequence numbers.

3. **MatchingEngine (toy)**
   - Match crossing orders (optional).

4. **Metrics**
   - Track update latency (ms).
   - Track throughput (updates/sec).

## Talking Points
- Data structures chosen and why.
- Time complexity for updates.
- Where latency comes from.
- How you’d scale or harden it.

## Interview Demo Script
- Walk through order book update.
- Show how you handle out-of-order updates.
- Explain how you’d add risk checks.
