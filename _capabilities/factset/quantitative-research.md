---
consumed_apis:
- factset-formula
- factset-quant
- factset-qfl
- factset-screening
description: Unified workflow for quantitative research including formula-based data retrieval, screening, factor analysis, and quant engine computations. Used by quantitative analysts.
layout: capability
name: FactSet Quantitative Research
operations:
- description: Execute formula queries.
  method: GET
  name: list-formulas
  path: /v1/formulas
- description: List quant engine resources.
  method: GET
  name: list-quant
  path: /v1/quant-engine
- description: List factor library resources.
  method: GET
  name: list-factors
  path: /v1/factors
- description: List screening resources.
  method: GET
  name: list-screens
  path: /v1/screens
personas: []
provider_name: Factset
provider_slug: factset
search_terms:
- portfolio analytics
- universal screening.
- research
- list screens
- list factors
- list quant engine resources.
- list formulas
- quantitative research
- quant engine computations.
- factor library data.
- financial
- market data
- execute formula queries.
- screening
- formula-based data retrieval.
- run quant engine
- factset
- list screening resources.
- get factor library data.
- investment analytics
- run universal screening.
- get factors
- financial data
- run formula
- factor analysis
- run screen
- run quant engine computations.
- list quant
- list factor library resources.
slug: quantitative-research
tags:
- FactSet
- Quantitative Research
- Factor Analysis
- Screening
tools:
- description: Execute formula queries.
  hints:
    openWorld: true
    readOnly: true
  name: run-formula
- description: Run quant engine computations.
  hints:
    openWorld: true
    readOnly: true
  name: run-quant-engine
- description: Get factor library data.
  hints:
    openWorld: true
    readOnly: true
  name: get-factors
- description: Run universal screening.
  hints:
    openWorld: true
    readOnly: true
  name: run-screen
---
