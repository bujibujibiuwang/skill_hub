---
name: business-algorithm-visualizer
description: Turn supply-chain and operations-research algorithms, rules, optimization models, heuristics, bad cases, trade-offs, and forecast logic into clear client-facing business diagrams and explanations. Use when a technical algorithm engineer needs to explain logic to business customers; do not use for generic decorative graphics or code-only architecture documentation.
---

# Business Algorithm Visualizer

## Purpose

Act as a bridge between technical truth and business understanding. Preserve the algorithm's actual conditions, priorities, exceptions, and limits while expressing them in language and diagrams that a non-technical client can validate.

The default deliverable is a self-contained, editable diagram specification plus a short business narrative. If the user asks for a rendered artifact, choose a suitable backend (Mermaid, SVG/HTML, Excalidraw, or Draw.io) and produce it when the environment supports it.

## Trigger conditions

Use this skill when the request includes one or more of:

- a supply-chain, logistics, inventory, routing, SND/车线, allocation, fulfillment, replenishment, forecasting, or optimization explanation;
- a request to turn rules, equations, constraints, heuristics, a bad case, a trade-off, or model output into a diagram;
- a need to present algorithm logic to a business user, client, product owner, operations team, or executive;
- a need to compare current/manual logic with an algorithmic approach.

Do not activate for a purely technical code flowchart, generic software architecture, or visual decoration unless the user explicitly wants the business-facing treatment.

## Operating workflow

1. **Extract the story.** Identify audience, business decision, objects, time horizon, inputs, actions, outcomes, objectives, constraints, priorities, exceptions, and what can be measured. Separate facts supplied by the user from assumptions.
2. **Normalize the logic.** Rewrite formulas and implementation terms into atomic business rules. Make precedence explicit: hard constraints, business priorities, soft preferences, tie-breakers, and fallback behavior.
3. **Choose one primary visual.** Use the decision tree in [references/diagram-selection.md](references/diagram-selection.md). Add one supporting visual only when it answers a different question (for example, process + before/after comparison).
4. **Translate language.** Apply [references/business-translation.md](references/business-translation.md). Use stable business nouns, observable verbs, and explicit “why this matters” annotations. Keep technical terms in a small glossary rather than in every node.
5. **Design the visual system.** Apply [references/visual-system.md](references/visual-system.md): color, shape, arrow, hierarchy, density, accessibility, and layout rules.
6. **Select the backend.** Follow [references/backend-adapters.md](references/backend-adapters.md). Prefer SVG/HTML for polished client review, Mermaid for fast editable drafts, Excalidraw for workshop-style explanation, and Draw.io for handoff/editability.
7. **Validate against source logic.** Run the checklist below. If source information is missing, show an explicit assumption or unresolved question rather than inventing a rule.

## Input contract

Accept natural language, tables, formulas, pseudocode, SQL, model constraints, screenshots, or mixed notes. When possible, request or infer this compact schema:

```text
Audience:
Business decision to explain:
Current process or pain point:
Objects and roles:
Inputs / signals:
Rules and priorities:
Hard constraints:
Soft objectives:
Exceptions / fallback:
Expected outcome or KPI:
Preferred output format:
```

If the input is incomplete, proceed with a clearly labeled “working interpretation” and list only the questions that could change the diagram.

## Default output format

Unless the user asks for another format, return:

1. **One-line takeaway** — the business rule or decision in plain language.
2. **Diagram title and audience**.
3. **Primary diagram** — preferably a client-ready SVG/HTML or a Mermaid source block if rendering is unavailable.
4. **How to read it** — 3–6 numbered points following the visual order.
5. **Business rationale** — why the rule exists and what risk it controls.
6. **Boundary conditions** — assumptions, exceptions, and unresolved data dependencies.
7. **Glossary** — only terms that appear in the source or output and could confuse the audience.

For a bad case, include “what happened → why it happened → how the algorithm changes the decision → expected business effect.” For a target-vs-constraint explanation, show the trade-off explicitly instead of calling every condition a “goal.”

## Diagram rules that must hold

- One diagram answers one primary question. Do not combine an end-to-end process, system architecture, KPI dashboard, and exception catalog into one dense canvas.
- Every arrow has an understood meaning: sequence, information flow, material flow, approval, dependency, or “blocks until.” Label ambiguous arrows.
- Every decision has visible branches and a default/fallback path.
- Every optimization output is tied to a business action, not shown as an unexplained score or variable.
- Show “not allowed,” “must satisfy,” and “preferred” differently.
- Never claim a result is optimal, fair, complete, or compliant unless the source supports that claim.
- Preserve units, direction, and scope: per order vs per route, daily vs weekly, local vs network-wide, quantity vs percentage.

## Quality checklist

Before delivering, verify:

- [ ] The audience can state the business decision after reading the title and takeaway.
- [ ] The diagram has a clear start, end, and reading direction.
- [ ] All hard constraints are visibly different from preferences/objectives.
- [ ] Branch conditions use business-observable language or include a glossary.
- [ ] Exceptions, minimums, caps, and fallback logic are not hidden in prose.
- [ ] No node contains a full paragraph or unexplained equation.
- [ ] The visual uses no more than 5–7 semantic colors and remains understandable in grayscale.
- [ ] The diagram does not imply causality or performance improvement that was not provided.
- [ ] A reviewer can trace each important visual statement back to an input rule.
- [ ] Output is editable or accompanied by editable source when practical.

For detailed anti-patterns and reusable supply-chain examples, read [references/anti-patterns-and-examples.md](references/anti-patterns-and-examples.md).
