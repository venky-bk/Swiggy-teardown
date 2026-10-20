# 21 — Proposed technical design

**This is a proposed architecture for Meal Confidence, not a diagram of Swiggy's actual internal systems.**

## Components
- Consumer UI: renders price breakdown, ETA confidence, supported menu attributes, and recovery actions.
- Product orchestration/API layer: requests data from authorised source-of-truth services.
- Price service: authoritative cart and checkout totals.
- ETA service: estimate, timestamp, confidence/calibration metadata where supported.
- Menu metadata service: restaurant-provided attributes and provenance.
- Order-state service: current status and eligible recovery paths.
- Analytics pipeline: event validation, aggregation, experiment assignment, and KPI computation.
- Experimentation service: eligible cohorts and treatment assignment.

## Data flow
1. User opens menu or cart.
2. UI requests current menu, price, ETA, and order context through authenticated APIs.
3. Orchestration layer validates freshness and permissions.
4. UI displays source-backed values and explicit unavailable states.
5. Checkout revalidates total and requires user confirmation.
6. Event pipeline records minimised product events.
7. Dashboards compare outcomes and guardrails by experiment cohort.

## API sketch (illustrative only)
- `GET /v1/cart/{cart_id}/price-breakdown`
- `GET /v1/availability/{restaurant_id}/{item_id}`
- `GET /v1/eta/{order_or_quote_id}`
- `GET /v1/menu-attributes/{restaurant_id}/{item_id}`
- `GET /v1/orders/{order_id}/recovery-options`
- `POST /v1/analytics/events`

These are design examples, not claimed Swiggy endpoints.

## Failure handling
- Price stale: force refresh and re-confirm.
- ETA unavailable: show standard fallback without confidence badge.
- Menu attribute missing: do not infer from dish name.
- Order-state API error: show latest known timestamp and support route.
- Analytics unavailable: do not block checkout.
- AI/tool error: return to conventional app flow; no hidden order placement.

## Security and privacy
Use scoped tokens, least privilege, access logging, input validation, rate limits, data retention controls, and redaction. Avoid storing raw address or payment details in analytics. AI tools must not receive more customer data than needed for the requested action.
