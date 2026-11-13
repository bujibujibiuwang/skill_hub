# Diagram selection rules

Choose the visual by the question the client needs answered, not by the algorithm's implementation style.

## Decision tree

```text
Is the main question “what happens next?”
├─ Yes → Process flow / swimlane
│       Use swimlane when roles, systems, or teams hand off work.
└─ No
   Is the main question “which condition determines the decision?”
   ├─ Yes → Decision tree / rule table
   └─ No
      Is the main question “how do entities and locations connect?”
      ├─ Yes → Network / route / SND diagram
      └─ No
         Is the main question “how did the result change?”
         ├─ Yes → Before/after, waterfall, or small multiples
         └─ No
            Is the main question “what competes with what?”
            ├─ Yes → Trade-off matrix / priority stack
            └─ No
               Is the main question “how does a forecast or score become an action?”
               ├─ Yes → Signal → interpretation → action pipeline
               └─ No → Layered system/context diagram or concise comparison
```

## Pattern catalog

| Business question | Primary visual | Use | Avoid |
|---|---|---|---|
| What happens from order to delivery? | Process flow | Sequence, gates, fallback | Architecture boxes with no action |
| Who does what and when? | Swimlane | Planner/system/warehouse/carrier responsibility | Mixing ownership with data flow |
| Why is this order allowed or blocked? | Decision tree + rule table | Explain eligibility, caps, minimums | A single “optimization engine” box |
| Why this route/vehicle/warehouse? | Route/network diagram | Show OD, hubs, capacity, direct vs transfer | Geographic detail that does not affect the decision |
| Why did the bad case occur? | Before/after + causal chain | Connect symptom to rule change | Blaming “the algorithm” without conditions |
| Why cannot all KPIs improve together? | Trade-off matrix or priority stack | Hard constraints vs soft objectives | Calling all KPIs equal |
| How does a forecast become replenishment? | Signal-to-action pipeline | Forecast, uncertainty, policy, order | Showing forecast as a final answer |
| How are quantities distributed? | Allocation waterfall or stacked bars | Reserve, minimum service, residual balancing | Pie charts for sequential allocation |

## Composition rules

- Start with the business outcome at the right or bottom; put technical mechanism beneath or behind it.
- Put “why” annotations outside the main path using callouts; keep the path scannable.
- For many rules, show the top 3–5 rules visually and place the complete rule table alongside or below.
- Use a small scenario or sample order only when it makes a branch concrete; label it as an example, not a universal rule.
- If the logic has more than two levels of nested conditions, split into overview + drill-down rather than shrinking the font.
