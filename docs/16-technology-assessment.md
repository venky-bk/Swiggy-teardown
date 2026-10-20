# 16 — Technology and AI assessment

## Publicly documented directions
- Swiggy's 2025 AGM transcript references AI-driven allocation and routing and Eco Saver batching (company leadership commentary; see S5).
- Swiggy announced MCP integrations for food ordering, dining reservations, and Instamart shopping in January 2026 (S6).
- Swiggy announced a multilingual voice-led commerce partnership with Sarvam in April 2026 (S8).

These announcements do **not** disclose Swiggy's full proprietary architecture, model types, training data, service-level objectives, or production performance.

## Relevant technology domains
- Search and ranking: relevance, availability, and user intent.
- ETA prediction: restaurant prep + dispatch + travel uncertainty.
- Dispatch/routing: proximity, capacity, batching, fairness, and safety constraints.
- Experimentation and analytics: event quality, assignment, attribution, guardrails.
- Conversational commerce: intent parsing, tool selection, policy enforcement, and explicit confirmation.
- Multilingual voice: speech recognition, language switching, menu/entity resolution, and confirmation.
- Data platform: real-time operational events and offline analysis.
- Observability: latency, error rate, tool failure, stale menu/price, and transaction integrity.

## AI opportunity test
Use AI only when it materially outperforms simpler alternatives:
1. Is the problem frequent and costly?
2. Are suitable data and feedback labels available?
3. Is the task ambiguous enough to benefit from ML/LLM?
4. Can errors be detected and safely recovered?
5. Does an offline benchmark and online experiment demonstrate value?
6. Can privacy, security, latency, and cost be controlled?

## Proposed architecture boundary
The proposed Meal Confidence experience should call existing authorised menu, price, ETA, and order-status services. A model may summarise or explain data but must not invent availability, dietary facts, prices, or delivery promises. Deterministic validation and user confirmation should govern checkout.
