# 12 — Unit economics

## Metrics and formulas
- **Average order value (AOV)** = gross order value / completed orders.
- **Take rate** = platform revenue attributable to marketplace / gross order value. Define numerator consistently.
- **Contribution per order** = order-level platform revenue − variable order-level costs.
- **Customer acquisition cost (CAC)** = acquisition spend / new customers attributed to that spend.
- **Customer lifetime contribution (LTC)** = expected active lifetime orders × contribution/order − lifecycle costs not already included.
- **LTC:CAC** = lifetime contribution / CAC.
- **Payback period** = time until cumulative contribution covers acquisition cost.
- **Repeat rate** = eligible customers who place another order within the defined window / eligible first-order customers.

## Inputs required
Orders, GOV, recognised revenue by stream, discounts split by funder, delivery costs, support/refunds, payment costs, acquisition spend, cohort retention, and attribution rules.

## Illustrative calculation (not Swiggy data)
Assume a hypothetical order has:
- platform revenue: ₹70
- variable fulfilment and payment costs: ₹42
- platform-funded promotion: ₹10
- order-level support/refund allowance: ₹3

Contribution/order = ₹70 − ₹42 − ₹10 − ₹3 = **₹15**.

If a product change adds 10,000 truly incremental orders, illustrative incremental contribution before fixed build costs = 10,000 × ₹15 = **₹1,50,000**. This is only a worked example; cannibalisation, extra costs, and contribution changes must be tested.

## Decision implications
A product change that increases orders but reduces contribution may still be worthwhile if retention or customer lifetime contribution improves. Conversely, gross order value growth alone is insufficient to prove product success.

See [`../analysis/unit_economics.py`](../analysis/README.md) for a reusable calculator.
