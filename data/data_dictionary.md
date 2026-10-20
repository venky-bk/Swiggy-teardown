# Data dictionary

## Current data assets
This repository contains no real Swiggy customer/order dataset. `event_tracking_plan.csv` is a proposed schema; `risk-register.csv` is an analyst-created risk register.

## Event plan fields
- `event_name`: stable snake_case event identifier.
- `trigger`: condition that emits the event.
- `required_properties`: semicolon-separated event attributes; avoid personal data.
- `identity`: recommended pseudonymous identity scope.
- `funnel_stage`: stage used in analysis.
- `metric`: intended KPI.
- `quality_checks`: validation rule or monitoring check.
- `evidence_status`: proposed instrumentation, not an existing Swiggy schema.
