# 20 — Product Requirements Document: Meal Confidence

## 1. Executive summary
Build a small decision-support layer for food discovery and checkout that clarifies total cost, ETA uncertainty, menu attributes, and recovery options.

## 2. Problem and evidence
Public product announcements show Swiggy has distinct propositions for speed, affordability, and health-oriented discovery, while its AI initiatives include conversational and voice-led commerce. The proposed feature is an inference about a cross-cutting need; public sources do not prove that customers currently experience a specific defect.

## 3. Goals
- Increase confidence in the meal decision.
- Improve successful checkout and fulfilment outcomes.
- Reduce avoidable price/ETA surprise contacts.
- Preserve sustainable unit economics and safety.

## 4. Non-goals
- Replacing existing ranking, dispatch, payment, or support systems.
- Making delivery-time guarantees.
- Generating unsourced dietary/allergen claims.
- Automatically placing orders without confirmation.

## 5. Users and user stories
- As a time-constrained customer, I want to compare likely arrival windows so I can choose a meal that fits my break.
- As a budget-conscious customer, I want to see the total payable price before checkout so I can stay within budget.
- As a customer with dietary preferences, I want to see where menu attributes came from so I can judge how much to rely on them.
- As a customer whose order is delayed, I want a clear next step so I can recover without repeated searching.

## 6. Functional requirements
- FR1: Display item subtotal, fees, taxes, discounts, and final payable amount using the current checkout source of truth.
- FR2: Display ETA information supplied by the approved delivery-estimation service; show uncertainty honestly.
- FR3: Refresh or mark stale ETA/price data when a defined validity threshold is exceeded.
- FR4: Show only supported menu attributes and their provenance/status.
- FR5: Provide a recovery entry point tied to the current order state.
- FR6: Log exposure, interaction, checkout, correction, and recovery events with privacy-minimised identifiers.
- FR7: Ensure any conversational/AI summary is subordinate to source-of-truth values and cannot silently modify cart or payment.

## 7. Non-functional requirements
- Performance: no material degradation to critical discovery/checkout latency; set numeric SLO after baseline measurement.
- Reliability: graceful fallback to existing experience if confidence data is unavailable.
- Security: authenticated access, least privilege, audit logging for sensitive actions.
- Accessibility: screen-reader labels, clear contrast, touch targets, and language support.
- Privacy: collect only data needed for fulfilment and evaluation; respect consent and retention rules.

## 8. Acceptance criteria
- Given a cart with valid prices, when the customer opens checkout, then the displayed total matches the checkout source of truth.
- Given a price changes before order placement, when the customer confirms, then the updated total is shown before payment.
- Given ETA confidence data is unavailable or stale, then the UI shows the standard estimate or an explicit unavailable state rather than fabricating confidence.
- Given an unsupported dietary attribute, then it is not shown as verified.
- Given a delay event that meets an agreed threshold, then the customer sees a clear status and support path.
- Given an AI assistant proposes a cart, then the customer must review and explicitly confirm before the order is placed.
- Given an analytics event is emitted, then it must not include raw payment credentials or unnecessary personal data.

## 9. Analytics
Track `menu_viewed`, `price_breakdown_viewed`, `eta_confidence_viewed`, `item_added_to_cart`, `checkout_started`, `checkout_completed`, `eta_updated`, `order_delivered`, `support_opened`, and `order_issue_resolved`.

## 10. Risks and mitigations
- False confidence: calibrate estimates and expose uncertainty.
- Stale price: source-of-truth validation at checkout.
- Misleading dietary data: provenance and partner correction flow.
- More UI complexity: usability test and staged rollout.
- Incentive/safety side effects: safety guardrails and no speed-based rider incentive.

## 11. Rollout
Research → prototype → internal QA → limited eligible cohort → experiment → staged expansion only after guardrails pass.

## 12. Open questions
- Which ETA service can expose calibrated uncertainty?
- What price components can be itemised consistently across markets?
- How are menu attributes collected and audited?
- Which support events are reliable enough to trigger proactive recovery?
- What is the baseline contribution/order and acceptable non-inferiority margin?
