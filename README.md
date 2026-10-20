# Product Teardown: Swiggy Food Delivery — Strategy, UX, Analytics & AI Opportunities

> Independent product-management portfolio project | Research cut-off: 20 October 2026

## Executive summary
This teardown examines Swiggy's **food-delivery marketplace**: how consumers discover meals, compare options, place orders, receive delivery, recover from failures, and return. The project connects customer experience to marketplace economics, operational execution, product analytics, experimentation, and emerging AI interfaces.

**Central thesis:** Swiggy's durable product challenge is not simply making food delivery faster. It is helping customers make a confident meal decision, receive the order reliably, and feel that the total price and service outcome were worth it—while protecting restaurant partner economics and delivery-partner safety.

**Recommended product concept:** *Meal Confidence* — a transparent decision layer that combines delivery-time confidence, total payable price, dietary/menu attributes supplied by restaurants, and clear recovery options. Start with an explainable rules-based MVP; add ML only where measured prediction lift justifies it. Conversational ordering and AI-native commerce are strategically relevant, but should complement—not obscure—the trusted transaction flow.

## Project objectives
- Define the product, users, core loop, and customer jobs.
- Review publicly documented product evolution and competitive context.
- Build a proposed KPI tree, event taxonomy, funnel analysis framework, and unit-economics calculator.
- Identify AI and automation opportunities without assuming proprietary architecture.
- Prioritise opportunities, define an MVP PRD, architecture, experiments, roadmap, and risks.
- Publish a reproducible, GitHub-ready research repository.

## Scope and methodology
- **Primary product:** Swiggy Food / restaurant food delivery in India.
- **Adjacent context:** Swiggy One, Bolt, Eco Saver, 99 Store, EatRight, Dineout and conversational/voice commerce where relevant to food discovery or retention.
- **Methods:** public-source desk research, JTBD, journey mapping, heuristic checklist, competitor comparison, KPI design, RICE-style prioritisation, and proposed experiments.
- Evidence labels: **Fact**, **Inference**, **Hypothesis**, **Recommendation**, **Illustrative assumption**.
- Public claims are sourced in [`research/sources.md`](research/sources.md). No internal Swiggy data, private interviews, or live app walkthrough were available for this version.

## Key findings
1. **Convenience is an operating-system problem, not just a UI problem.** Swiggy's public Bolt materials describe a tightly scoped model: quick-preparation items, a limited radius, and operational coordination.
2. **Affordability and speed are distinct customer jobs.** The public 99 Store and Eco Saver propositions indicate a strategic focus on value as well as speed.
3. **The product spans a multi-sided marketplace.** Better consumer conversion is not sufficient if it increases restaurant burden, delivery-partner risk, refunds, or cost to serve.
4. **AI should reduce decision and coordination friction.** Swiggy announced MCP-based conversational commerce in January 2026 and multilingual voice-led commerce with Sarvam in April 2026; the product challenge shifts toward safe intent capture, transparent confirmation, and reliable execution.
5. **The most important missing evidence is funnel and reliability data by cohort.** This repository proposes the instrumentation needed to validate hypotheses; it does not claim to know Swiggy's internal conversion or retention rates.

## Proposed improvement: Meal Confidence
A pre-checkout and order-tracking layer that makes four things clear:
- **Total cost:** item total, fees, taxes, discounts, and membership benefits before commitment.
- **Arrival confidence:** a time range with a confidence indicator, updated when material conditions change.
- **Menu confidence:** verified restaurant-provided dietary/allergen and item availability information, with explicit uncertainty.
- **Recovery clarity:** the next action and support route when an order is delayed, unavailable, or incorrect.

### Proposed North Star Metric
**Weekly fulfilled orders rated satisfactory** = weekly orders delivered and not refunded/cancelled for service failure, with a post-delivery satisfaction response above a defined threshold. This is a *proposal*, not Swiggy's actual internal metric. Because survey response can bias the metric, track fulfilment, complaint, refund, and survey-response guardrails separately.

## Success metrics
- Primary: successful fulfilled orders per weekly active ordering customer.
- Quality guardrails: cancellation rate, late-delivery rate, refund/contact rate, order accuracy, partner complaints, delivery-partner safety signals.
- Business guardrails: contribution margin per order, discount cost per incremental order, repeat rate, restaurant retention.
- Trust guardrails: price surprises, ETA error, dietary-information corrections, AI checkout reversals.

## Deliverables
- [Product scope](docs/02-product-scope.md) · [User journey](docs/06-user-journey.md) · [UX audit checklist](docs/07-ux-usability-audit.md)
- [Competitive analysis](docs/08-competitive-analysis.md) · [Business model](docs/11-business-model.md) · [Unit economics](docs/12-unit-economics.md)
- [KPI tree](docs/14-north-star-and-kpis.md) · [Technology assessment](docs/16-technology-assessment.md) · [Opportunity backlog](docs/17-opportunity-backlog.md)
- [Solution proposal](docs/19-proposed-solution.md) · [PRD](docs/20-product-requirements-document.md) · [Technical design](docs/21-technical-design.md)
- [Experimentation plan](docs/22-experimentation-plan.md) · [Roadmap](docs/23-product-roadmap.md) · [Executive recommendation](docs/25-executive-recommendation.md)
- [Event tracking CSV](data/event_tracking_plan.csv) · [Risk register CSV](data/risk-register.csv) · [Analysis scripts](analysis/README.md)

## Tools
Markdown, CSV, Python standard library, and Mermaid. Python scripts use synthetic/example inputs only and are designed to run locally.

## Limitations
- This is public-source desk research, not an official Swiggy document.
- Product surfaces and policies can change by location, app version, account, and time.
- Public company announcements are not independent verification of every performance claim.
- No internal order-level data, customer interviews, experiments, or live app screenshots were supplied.
- Opportunity scores are analyst estimates and must be recalibrated with actual reach, impact, and effort data.

## Disclaimer
Independent educational portfolio project. Not affiliated with, endorsed by, or prepared on behalf of Swiggy Limited. Swiggy and related marks belong to their respective owners. Do not interpret this analysis as investment advice.

## Author
**Project author:** Venkatesh Borkute  
**LinkedIn / portfolio:** [Add your profile URL]

## Repository map
See [`docs/`](docs/) for the analysis, [`research/`](research/) for source notes, [`data/`](data/) for tracking and risk artifacts, [`diagrams/`](diagrams/) for editable Mermaid diagrams, and [`analysis/`](analysis/) for reproducible calculations.

## Run the illustrative analysis
```bash
python analysis/unit_economics.py
python analysis/funnel_analysis.py
```
No proprietary or customer data is required.
