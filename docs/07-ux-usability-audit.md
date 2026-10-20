# 07 — UX and usability audit checklist

**Status:** No live app walkthrough was conducted for this version. Items below are inspection questions, not verified defects.

| Area | Inspection question | Severity if failed | Evidence needed |
|---|---|---|---|
| Navigation | Can a new user distinguish food delivery from adjacent services? | Medium | Task-based usability test |
| Search | Do results reflect availability, location, and user intent? | High | Query-level relevance study |
| Filters | Are price, dietary, and timing filters understandable? | Medium | Usability test + event data |
| Total price | Is the final payable amount understandable before payment? | High | Screen review and price-comprehension test |
| ETA | Is the displayed estimate presented as an estimate, not a promise? | High | ETA calibration and user comprehension |
| Menu attributes | Are allergen/dietary claims sourced and uncertainty visible? | High | Partner data audit |
| Cart | Are unavailable items and substitutions handled clearly? | High | Edge-case testing |
| Payment | Are failure and retry paths understandable? | High | Payment funnel + QA |
| Order tracking | Do status changes communicate useful progress? | Medium | Event timing audit |
| Support | Can users reach an appropriate resolution without repeated effort? | High | Contact reasons and resolution analysis |
| Accessibility | Are screen-reader labels, contrast, touch targets, and language needs addressed? | High | Accessibility audit |
| Trust/privacy | Are permissions and preference controls understandable? | High | Privacy review |

## Issue template
- **Location:** [screen/journey]
- **Evidence:** [screen recording, source, interview, metric]
- **Expected behaviour:** [what the user should be able to do]
- **Observed behaviour:** [only if directly tested]
- **User impact:** [time, confusion, failure]
- **Business impact:** [conversion, retention, cost]
- **Severity:** Critical / High / Medium / Low
- **Confidence:** High / Medium / Low
- **Recommendation:** [smallest testable change]

## Initial hypotheses to test
1. Users may compare restaurants on item price but overlook differences in total payable cost.
2. Users may interpret a single ETA as more precise than the underlying uncertainty supports.
3. Users with dietary goals may struggle if attributes are incomplete or not standardised.
4. Recovery may feel fragmented if the order status, support entry point, and resolution policy are not aligned.

Do not publish these as confirmed Swiggy defects until tested.
