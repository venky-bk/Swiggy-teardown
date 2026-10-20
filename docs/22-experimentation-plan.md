# 22 — Experimentation plan

## Experiment 1: Total-price clarity
- Hypothesis: itemised total payable price earlier in the journey improves checkout confidence and reduces late abandonment.
- Control: current eligible experience.
- Treatment: itemised total shown at a defined earlier point.
- Primary: completed orders per eligible cart.
- Guardrails: contribution/order, discount use, price-related contacts, cancellation.
- Randomisation: user or stable account ID to avoid cross-device contamination where possible.
- Decision: adopt only if primary metric improves and contribution/trust guardrails remain within pre-registered bounds.

## Experiment 2: ETA range vs point estimate
- Hypothesis: a calibrated range reduces perceived surprise without materially reducing conversion.
- Primary: ETA-related complaint/contact rate and satisfaction.
- Guardrails: checkout conversion, actual ETA error, cancellations.
- Precondition: ETA model can produce calibrated intervals; do not fabricate ranges.

## Experiment 3: Dietary attribute provenance
- Hypothesis: source/verification labels improve confidence for users who use dietary filters.
- Primary: task success and correct interpretation in usability test.
- Guardrails: unsupported-claim reports, filter abandonment.
- Begin with qualitative usability tests; only later run a powered experiment.

## Experiment 4: Proactive recovery
- Hypothesis: a clear proactive message for material delays reduces repeat support contacts.
- Primary: resolution time and repeat contacts.
- Guardrails: message opt-out, unnecessary-contact rate, refund cost, satisfaction.
- Do not send notifications based on low-confidence status predictions.

## Experiment 5: Conversational meal discovery
- Hypothesis: natural-language intent can shorten time to a suitable menu for complex requests.
- Control: standard search/filter flow.
- Treatment: assistant-generated shortlist grounded in live menu/price/availability data.
- Primary: task completion and completed order per eligible session.
- Guardrails: wrong-item correction, price mismatch, latency, tool failure, user trust.

## Sample size and statistics
No sample size is claimed without baseline conversion, minimum detectable effect, alpha, power, allocation ratio, and expected eligibility. Use a standard two-proportion power calculation for binary conversion outcomes, and pre-register exclusions, stopping rules, and guardrails. Qualitative tests are for discovering usability issues, not estimating population-level lift.

## Interpret outcomes
- Positive: primary improves and guardrails pass; replicate or stage rollout.
- Negative: stop or revise based on mechanism.
- Inconclusive: inspect power, data quality, segment heterogeneity, and treatment fidelity; do not declare success from clicks alone.
