# 18 — Prioritisation (illustrative RICE)

RICE = Reach × Impact × Confidence / Effort. For this first pass:
- Reach: estimated number of eligible users per quarter in thousands (assumption).
- Impact: 0.25 low, 0.5 medium, 1 high, 2 very high.
- Confidence: 0.5 low, 0.7 medium, 0.9 high.
- Effort: person-months (assumption).

| Opportunity | Reach (000s) | Impact | Confidence | Effort (person-months) | RICE |
|---|---:|---:|---:|---:|---:|
| O1 Meal Confidence | 300 | 1.0 | 0.6 | 4 | 45.0 |
| O2 Contextual reorder | 250 | 0.5 | 0.6 | 3 | 25.0 |
| O3 Verified dietary attributes | 100 | 1.0 | 0.4 | 5 | 8.0 |
| O4 Guided recovery | 120 | 1.0 | 0.5 | 5 | 12.0 |
| O5 Group order coordination | 80 | 0.5 | 0.4 | 4 | 4.0 |
| O6 Conversational discovery | 150 | 1.0 | 0.5 | 6 | 12.5 |
| O7 Multilingual voice | 100 | 1.0 | 0.4 | 8 | 5.0 |
| O8 Menu-quality dashboard | 200 | 1.0 | 0.5 | 6 | 16.7 |
| O9 ETA exception intervention | 250 | 1.5 | 0.4 | 8 | 18.8 |
| O10 Ad relevance controls | 150 | 0.5 | 0.4 | 4 | 7.5 |

These scores are **illustrative analyst estimates** and should not be mistaken for Swiggy's internal reach or effort data. The ranking is a hypothesis for deciding what to validate first.

## Why O1 leads
1. It targets a high-frequency decision before the order becomes operationally expensive.
2. It can begin with transparent display and rules-based confidence rather than a large AI build.
3. It creates measurable user and business outcomes while preserving guardrails for partner economics.

## Decision gate
Do not fund full build from this table alone. Run problem interviews, baseline measurement, and a prototype test; update reach, impact, confidence, and effort with observed data.
