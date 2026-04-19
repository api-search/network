---
consumed_apis:
- visio-graph
description: Workflow capability for analyzing Visio diagrams including reading pages, shapes, data items, comments, and hyperlinks. Used by business analysts and IT architects to programmatically inspect diagram content.
layout: capability
name: Microsoft Visio Diagram Analysis
operations:
- description: List all pages.
  method: GET
  name: list-pages
  path: /v1/pages
- description: List shapes on a page.
  method: GET
  name: list-shapes
  path: /v1/shapes
- description: List data items for a shape.
  method: GET
  name: list-shape-data-items
  path: /v1/shape-data
personas: []
provider_name: Microsoft Visio
provider_slug: microsoft-visio
search_terms:
- shape data operations.
- get details of a specific shape.
- diagramming
- get shape
- analyze visio diagrams programmatically.
- list shape data items
- list data items for a shape.
- list all pages in a visio diagram.
- Business Analyst
- IT Architect
- list all shapes on a diagram page.
- diagram page operations.
- diagram analysis
- list data items attached to a shape.
- shape operations.
- business analysts reviewing process flow diagrams.
- list shapes
- microsoft visio
- microsoft 365
- it architects analyzing network and system diagrams.
- list all pages.
- list shapes on a page.
- list pages
- visualization
- flowcharts
- business process
slug: diagram-analysis
tags:
- Microsoft Visio
- Diagram Analysis
- Visualization
tools:
- description: List all pages in a Visio diagram.
  hints:
    openWorld: true
    readOnly: true
  name: list-pages
- description: List all shapes on a diagram page.
  hints:
    openWorld: true
    readOnly: true
  name: list-shapes
- description: Get details of a specific shape.
  hints:
    readOnly: true
  name: get-shape
- description: List data items attached to a shape.
  hints:
    openWorld: true
    readOnly: true
  name: list-shape-data-items
---
