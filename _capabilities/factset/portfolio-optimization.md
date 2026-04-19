---
consumed_apis:
- factset-optimizer
- factset-axioma-eq
- factset-barra
- factset-northfield
- factset-open-risk
description: Unified workflow for portfolio optimization using multiple optimization engines including FactSet, Axioma, Barra, Northfield, and open risk models. Used by portfolio optimizers.
layout: capability
name: FactSet Portfolio Optimization
operations:
- description: List optimizations.
  method: GET
  name: list-optimizations
  path: /v1/optimize
- description: List risk models.
  method: GET
  name: list-risk-models
  path: /v1/risk-models
personas: []
provider_name: Factset
provider_slug: factset
search_terms:
- factset optimize
- research
- list risk models.
- run axioma equity optimization.
- northfield optimize
- list risk models
- portfolio optimization
- get open risk models.
- factset
- risk models
- financial data
- barra optimize
- get risk models
- investment analytics
- list optimizations.
- run barra optimization.
- run northfield optimization.
- market data
- portfolio analytics
- run factset portfolio optimization.
- list optimizations
- financial
- portfolio optimization.
- open risk models.
- axioma equity optimize
- asset allocation
slug: portfolio-optimization
tags:
- FactSet
- Portfolio Optimization
- Risk Models
- Asset Allocation
tools:
- description: Run FactSet portfolio optimization.
  hints:
    readOnly: true
  name: factset-optimize
- description: Run Axioma equity optimization.
  hints:
    readOnly: true
  name: axioma-equity-optimize
- description: Run Barra optimization.
  hints:
    readOnly: true
  name: barra-optimize
- description: Run Northfield optimization.
  hints:
    readOnly: true
  name: northfield-optimize
- description: Get open risk models.
  hints:
    readOnly: true
  name: get-risk-models
---
