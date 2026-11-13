# Backend adaptation guidance

Choose the least complex backend that satisfies the user's need. Preserve the same semantic model across backends.

## Mermaid

Best for fast drafts, source-controlled documentation, and simple flows/decision trees. Use `flowchart`, `sequenceDiagram`, `stateDiagram-v2`, or `quadrantChart` only when the semantics fit. Keep labels short, quote special characters, and include a legend for custom colors. Mermaid is not a substitute for a polished slide when layout and branding matter.

## SVG / HTML

Best default for a client-ready single-page visual. Use semantic grouping, responsive sizing, accessible text, and editable text where practical. Prefer a clean canvas with a title, legend, main path, side rationale cards, and a footer containing assumptions/source scope.

## Excalidraw

Best for workshops, discovery sessions, and explaining reasoning informally. Use hand-drawn styling sparingly; preserve a clear reading direction and add a polished export only when the audience expects formal delivery.

## Draw.io

Best when the client or delivery team needs to continue editing the diagram. Use native shapes/connectors, named layers, and a legend. Keep layout stable, avoid crossing lines, and include a page or layer for assumptions and exceptions.

## Backend selection table

| Need | Prefer | Deliver alongside |
|---|---|---|
| Fast iteration / text review | Mermaid | Plain-language narrative |
| Executive or client presentation | SVG/HTML | Source spec or Mermaid where useful |
| Collaborative whiteboard | Excalidraw | Finalized summary diagram |
| Formal editable handoff | Draw.io | PNG/SVG preview and assumptions |

If no renderer is available, return a Mermaid source block plus a textual wireframe and do not pretend it is a rendered image.
