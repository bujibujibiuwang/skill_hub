# Visual semantics and layout

Use a restrained, business-document visual language. The goal is fast comprehension in a meeting, not visual novelty.

## Semantic shapes

| Shape | Meaning |
|---|---|
| Rounded rectangle | Business action or processing step |
| Rectangle with small system tag | System-generated or automated action |
| Diamond | Explicit yes/no or multi-branch decision |
| Hexagon / shield | Gate, mandatory policy, eligibility, or compliance check |
| Cylinder | Inventory, master data, or persistent dataset |
| Document shape | Input/output artifact: order, plan, forecast, report |
| Dashed container | Scope, phase, scenario, or optional module |
| Callout | Rationale, risk controlled, or clarification |

Do not use a shape only for decoration. If a visual does not have a stable meaning, use a rounded rectangle.

## Color semantics

Use color as a secondary channel and label meaning in text or shape. A safe default palette:

- Navy `#17324D`: primary path / stable business process
- Blue `#2F6FED`: information or system step
- Green `#2E8B57`: feasible, accepted, or improved outcome
- Amber `#D99000`: preference, warning, or trade-off
- Red `#C0392B`: blocked, risk, exception, or bad case
- Purple `#6F4DBF`: model/forecast/analytics layer
- Gray `#6B7280`: context, reference, or unchanged state

Use at most 5–7 colors on a canvas. Ensure contrast and provide labels/icons for red-green distinctions.

## Arrow semantics

- Solid arrow: normal sequence or material movement.
- Blue arrow: information/data flow.
- Dashed arrow: optional, conditional, or dependency relationship.
- Red blunt-ended line: blocked/not allowed.
- Green check arrow: accepted/eligible path.
- Double-headed arrow: comparison or feedback loop; label it.

Always label arrows when “feeds,” “approves,” “triggers,” and “depends on” could be confused.

## Hierarchy and density

- Title: state the decision or outcome, not just the algorithm name.
- Subtitle: audience and scope.
- Main path: 5–9 major nodes where possible.
- Detail: put rules in short labels, side cards, or a companion table.
- Use whitespace to separate mandatory path, optional path, and exception path.
- Keep node labels to one idea; use a verb + object pattern (“Protect minimum service”, “Allocate residual capacity”).

## Client-readiness checks

The visual should remain understandable when projected, printed in grayscale, or pasted into a slide. Use consistent terminology, aligned spacing, visible legends, and an explicit “example” label for sample numbers.
