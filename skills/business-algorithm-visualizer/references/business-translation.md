# Technical language → business language

Translate the decision and its consequence, not just the vocabulary. Keep mathematical precision in the underlying source and surface only the minimum needed for trust.

## Core transformations

| Technical expression | Business-facing expression | Preserve explicitly |
|---|---|---|
| Objective function | What the plan is trying to improve | Direction, KPI, time scope |
| Hard constraint | Must satisfy / cannot exceed / not allowed | Threshold, unit, scope |
| Soft constraint / penalty | Preferred; violating it is allowed but costly | Priority or penalty meaning |
| Decision variable | What the operation can choose | Available choices and granularity |
| Feasible solution | A plan that can actually be executed | Operational prerequisites |
| Infeasible | No plan satisfies all mandatory conditions | Which conditions conflict |
| Greedy heuristic | Make the best local choice first | What it may miss globally |
| Iterative improvement | Repeatedly adjust weak spots | Stop condition / convergence caveat |
| Relaxation | Temporarily loosen a rule to find a workable plan | Which rule, why, and risk |
| Penalty weight | Relative importance used to balance trade-offs | Not a percentage unless it is |
| Forecast confidence interval | Expected range, not a promise | Coverage, horizon, uncertainty |
| Feature importance | Signals that most influenced this estimate | Association is not causation |
| Service level | Chance or share of demand served as defined | Exact denominator and period |
| Fill rate | Share of requested quantity fulfilled | Order-line vs unit definition |
| ETA / travel time | Expected arrival or transit duration | Variability and assumptions |

## Sentence patterns

Prefer:

- “The system first protects the minimum service requirement, then uses remaining capacity to reduce cost.”
- “If the network still has direct long-distance demand, short-distance volume is limited to the operating minimum.”
- “This is a preference, not a hard block; the plan may violate it when capacity is insufficient.”
- “The forecast is an estimate of expected demand. The replenishment rule adds lead time, safety stock, and order constraints before creating a purchase suggestion.”

Avoid:

- “The optimizer maximizes a weighted objective under constraints.”
- “The model decided this because the score was high.”
- “The algorithm guarantees the best result” unless optimality is proven and scoped.
- “The model learns the business rule” when the rule is actually configured or hard-coded.

## Business narrative template

```text
The business problem is [observable pain / decision].
The algorithm first protects [mandatory requirement], because [business risk].
It then chooses among [actions] to improve [KPI], while respecting [capacity / timing / policy].
When [exception], it falls back to [fallback], so that [operational consequence].
The result should be evaluated by [KPI + scope + period], not by [misleading proxy].
```

## “Why” annotations

Attach a short reason to each non-obvious rule:

- Rule: “Minimum two stops before route release.”
- Why: “Avoids dispatching a vehicle below the operational threshold.”
- Risk controlled: “Under-filled vehicle / poor utilization.”

Do not turn the annotation into a speculative claim about savings unless the user provides evidence.
