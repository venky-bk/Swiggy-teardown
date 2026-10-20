# 10 — Market opportunity

## Market context
Swiggy and research partners have published estimates that India's overall food-services market could exceed US$125 billion by 2030; this is a forecast from the company's 2025 *How India Eats* release, not actual revenue and not Swiggy's addressable market. Third-party online-delivery estimates use different definitions. See S9 and S12 in [`../research/sources.md`](../research/sources.md).

## Why not provide a single TAM/SAM/SOM number?
A defensible estimate for this product proposal requires a narrower scope: target cities, eligible active customers, relevant ordering occasions, adoption, incremental order rate, and contribution per incremental order. A broad food-services TAM would overstate the opportunity for one UX intervention.

## Bottom-up model
- **TAM orders/year** = target population × eligible ordering occasions/person/year.
- **SAM orders/year** = TAM orders × share of occasions and locations served by the target feature.
- **SOM incremental orders/year** = SAM orders × expected adoption × causal incremental-order rate.
- **Incremental contribution** = incremental orders × contribution/order − implementation and operating costs.

## Inputs required
1. Target segment population by city and cohort.
2. Baseline frequency and order success.
3. Feature eligibility and exposure.
4. Incremental conversion/retention from experiment.
5. Contribution margin per incremental order, net of incentives and support.
6. Cannibalisation and substitution between existing Swiggy order types.

## Sensitivity
Run low/base/high scenarios for adoption, incremental lift, and contribution per order. If value is driven mainly by assumptions rather than evidence, prioritise a pilot rather than a large rollout.
