# 15 — Funnel and cohort analysis

## Primary funnel
Home/entry → search or category → restaurant/menu view → add to cart → checkout start → payment success → order accepted → delivered → repeat order within 30 days.

## Stage conversion
For stage i: conversion(i → i+1) = distinct eligible users reaching stage i+1 within the attribution window / distinct eligible users reaching stage i.

Specify session/user/order identity and an attribution window before reporting. Do not mix order-level and user-level denominators.

## Cohort analysis
- Acquisition cohort: week of first completed order.
- Retention: share of cohort completing another order in week 1, 2, 4, etc.
- Quality cohort: compare retention by first-order fulfilment quality, ETA error, refund/contact, and price surprise.
- Value cohort: compare repeat behaviour and contribution by discount exposure and membership status.

## Key pitfalls
- Correlation is not causation: users with better experiences may differ systematically.
- Do not attribute retention to Bolt or a discount without controlling for eligibility, geography, seasonality, and user intent.
- Handle duplicate events, late-arriving events, cancellations, and order modifications consistently.
- Keep test assignment and exposure events distinct.

## Example synthetic funnel
The script `analysis/funnel_analysis.py` uses clearly labelled synthetic counts to demonstrate stage conversion. Replace them only with approved, privacy-safe event aggregates before drawing conclusions.
