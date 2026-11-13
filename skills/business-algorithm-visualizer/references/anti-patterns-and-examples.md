# Anti-patterns and reusable supply-chain examples

## Common anti-patterns

### 1. “Black-box optimizer”

Bad: `订单 → 优化引擎 → 最优方案`.

Why it fails: the client cannot see what was protected, what was traded off, or why a plan was rejected.

Repair: show `需求/资源 → mandatory gates → priority decisions → executable plan → KPI`, with at least one “why” callout and a fallback path.

### 2. Technical soup

Bad: every node contains variable names, solver terms, and equations.

Repair: show the business action in the node, keep the exact formula in a companion note/glossary, and retain units/scope.

### 3. False certainty

Bad: “预测值就是未来销量” or “模型保证最优”.

Repair: distinguish estimate, policy, constraint, and observed result; state the evaluation scope.

### 4. Equal-looking priorities

Bad: service level, cost, utilization, and freshness shown as four equal goals.

Repair: show a priority stack: hard constraints first, primary objective second, secondary preferences third, fallback last.

### 5. Missing exception path

Bad: a single happy path from forecast to replenishment.

Repair: add insufficient stock, capacity shortage, late data, and manual override paths only when relevant.

## Reusable example 1: inventory and replenishment

**Business question:** Why does the recommended order differ from forecast demand?

**Primary visual:** signal → policy → executable order pipeline.

```text
Demand history + promotion + lead time
              ↓
        Demand estimate
              ↓
 Safety stock / service target
              ↓
 On-hand + in-transit + open orders
              ↓
   Order multiple / MOQ / capacity gate
       ┌──────┴──────┐
   feasible        constrained
       ↓              ↓
 recommended order  exception / review
```

Business takeaway: “The forecast estimates need; the replenishment policy converts that estimate into an order that can be purchased and delivered.”

## Reusable example 2: route / truckline / SND

**Business question:** Why does long-distance direct demand get protected before short-distance volume?

**Primary visual:** network diagram plus priority decision.

```text
Network demand
   ├─ A→C direct long-haul demand ── protect first
   └─ A→B short-haul demand ─────── fill to operating minimum
                         ↓
          If direct long-haul demand is cleared
                         ↓
             use remaining capacity for A→B
```

Business takeaway: “The rule protects the demand that has fewer routing alternatives; short-haul volume uses residual capacity after the direct long-haul requirement is met.”

Show the distinction between: `must dispatch`, `minimum stop/service requirement`, `preferred direct shipment`, and `residual capacity`. Do not call every threshold an optimization objective.

## Reusable example 3: allocation / split shipment

**Business question:** Why did one customer not receive all requested quantity?

**Primary visual:** allocation waterfall.

```text
Available stock
   ↓ reserve mandatory demand / critical customers
   ↓ satisfy minimum allocation or service floor
   ↓ distribute remaining stock by priority
   ↓ respect pack size / truck capacity
   ↓ output allocation + unfulfilled remainder
```

Show the unfulfilled remainder as a visible outcome, not a hidden negative number. If priority is configurable, label it “configured priority,” not “fairness.”

## Reusable example 4: 允发 / 允收

**Business question:** Why was an order quantity reduced or a receipt rejected?

**Primary visual:** two-sided eligibility gate.

```text
Order request
   ↓ supplier / inventory / route / policy checks
允发 quantity ─────────→ transit / appointment checks ─────────→ 允收 quantity
   ↓ blocked or reduced                                      ↓ blocked / rescheduled
 reason code + next action                                  reason code + next action
```

Keep “can ship” and “can receive” as separate decisions. A shipment being allowed does not imply the destination can receive it at that time.

## Reusable example 5: forecast white-boxing

**Business question:** What signals influenced the forecast, and how does uncertainty affect action?

**Primary visual:** signal contribution + uncertainty-to-policy pipeline.

```text
baseline demand
 + seasonality
 + promotion / price
 + holiday / calendar
 + stockout correction
 + external signal
        ↓
 expected demand + uncertainty range
        ↓
 policy decides safety stock / review / exception
```

State that contribution is an explanation of model behavior, not necessarily a causal claim. Show whether the signal is configured, learned, or manually overridden.

## Reusable example 6: objective conflict

**Business question:** Why did cost improve while service level did not improve equally?

**Primary visual:** priority stack or trade-off matrix.

```text
Hard: safety / regulatory / capacity feasibility
  ↓
Primary: service target or delivery promise
  ↓
Secondary: cost, utilization, carbon, stability
  ↓
Fallback: manual review / exception queue
```

Explain that improving one metric may consume capacity or violate another preference. Use actual measured results if available; otherwise label the diagram as a decision logic, not a performance claim.
