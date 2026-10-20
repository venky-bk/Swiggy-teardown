# 14 — North Star Metric and KPI tree

## Proposed North Star
**Weekly satisfactory fulfilled orders per weekly active ordering customer.**

Operational definition for testing:
- Fulfilled: delivered and not cancelled.
- Satisfactory: no recorded service-failure refund/complaint plus optional post-order rating above a pre-defined threshold.
- Report survey response separately to avoid treating non-responders as satisfied.
- This is a proposal, not Swiggy's internal North Star Metric.

## KPI tree
1. **Qualified demand**
   - active ordering customers
   - qualified sessions
   - search success
2. **Activation and discovery**
   - search-to-menu-view
   - menu-to-cart
   - first-order conversion
   - time to first relevant choice
3. **Transaction**
   - cart-to-checkout
   - checkout completion
   - payment success
   - total-price surprise rate
4. **Fulfilment quality**
   - restaurant acceptance
   - prep-time error
   - ETA mean absolute error and calibration
   - successful fulfilment
   - cancellation/refund/contact rate
5. **Retention**
   - 7/30-day repeat order rate
   - cohort order frequency
   - reactivation rate
6. **Economics**
   - contribution/order
   - incentive cost per incremental order
   - support cost/order
   - restaurant retention and ad value
7. **Trust and safety**
   - order accuracy
   - complaint resolution time
   - safety incidents per delivery exposure
   - dietary data correction rate
   - AI order correction/reversal rate

## Measurement definitions
- **Checkout conversion** = completed orders / checkout starts.
- **Search success** = sessions with a relevant menu view or add-to-cart after search / search sessions. Define relevance and attribution window.
- **ETA MAE** = mean absolute value of actual delivery time minus displayed ETA at a defined snapshot.
- **30-day repeat** = first-order customers with another completed order within 30 days / eligible first-order customers.
- **Contribution/order** = consistently defined order-level revenue minus variable costs.

## Segmentation
Track by city/zone, new vs repeat, time of day, cuisine/occasion, membership status, value/speed proposition, payment type, restaurant, and delivery-distance band. Apply privacy and minimum cohort-size controls.

## Cadence
Real-time monitoring for operational exceptions; daily funnel and quality review; weekly cohort and experiment review; monthly unit-economics review. These are proposed operating cadences.
