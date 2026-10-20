# 19 — Proposed solution: Meal Confidence

## Problem statement
When choosing food, a customer needs to trade off menu fit, total cost, and arrival time. If those signals are unclear or appear at different stages, the customer may make a lower-confidence choice or abandon the order. This is a **hypothesis**, not a verified Swiggy defect.

## Target users
Start with repeat users who place time-constrained weekday orders and budget-conscious users. Validate both segments separately.

## Value proposition
“Choose a meal with a clearer view of what it costs, when it is likely to arrive, and what is known about the menu—before you commit.”

## MVP
1. Show a clear total payable estimate before payment, with item price, fees, taxes, discounts, and membership effects itemised.
2. Display an ETA range or confidence band based on approved operational estimates; label it as an estimate.
3. Explain major ETA changes in plain language when reliable status data exists.
4. Present restaurant-supplied dietary attributes with source/verification status; do not make unsupported health or allergen guarantees.
5. Offer a clear recovery route when the order is delayed or unavailable.

## Non-goals
- No autonomous purchase without explicit user confirmation.
- No new delivery-speed promise.
- No medical or allergen safety guarantee from an LLM.
- No redesign of the full Swiggy app.
- No new loyalty/discount scheme.
- No assumption that internal services or data are available without platform-team confirmation.

## Why not lead with generative AI?
The main problem is information confidence and coordination. Transparent UI, deterministic price calculations, and calibrated ETA ranges may solve much of it. AI can help explain a complex status or translate a request, but should not replace source-of-truth services.

## User flow
Open food → search/browse → compare total cost and ETA confidence → inspect menu attributes → add to cart → confirm final payable amount → place order → monitor meaningful status changes → receive or enter recovery path.

## Success criteria
- Improve checkout completion or reduce abandonment without worsening contribution/order.
- Reduce price-surprise and ETA-related contacts.
- Maintain or improve order accuracy and satisfaction.
- No increase in unsafe delivery signals or misleading dietary claims.
- Demonstrate improvement in a pre-registered controlled experiment.
