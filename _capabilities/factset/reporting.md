---
consumed_apis:
- factset-ent-rb
- factset-fund-rb
- factset-est-rb
- factset-cap-rb
- factset-ovw-rb
- factset-own-rb
- factset-charts
- factset-cards
- factset-bookbuilder
- factset-vermilion
description: Unified workflow for generating reports including entity, fundamentals, estimates, capital structure, overview, ownership reports, charts, and digital cards. Used by report builders.
layout: capability
name: FactSet Reporting
operations:
- description: List available reports.
  method: GET
  name: list-reports
  path: /v1/reports
- description: Generate a chart.
  method: GET
  name: generate-chart
  path: /v1/charts
personas: []
provider_name: Factset
provider_slug: factset
search_terms:
- generate capital structure report.
- reporting
- portfolio analytics
- research
- overview report
- generate a digital card.
- report generation.
- build a custom report book.
- financial
- list available reports.
- ownership report
- entity report
- visualization
- chart generation.
- build book
- generate ownership report.
- generate a chart.
- factset
- estimates report
- list reports
- report builder
- generate estimates report.
- capital structure report
- generate digital card
- generate overview report.
- generate entity report.
- investment analytics
- generate fundamentals report.
- fundamentals report
- vermilion report
- financial data
- generate chart
- generate vermilion report.
- market data
slug: reporting
tags:
- FactSet
- Reporting
- Report Builder
- Visualization
tools:
- description: Generate entity report.
  hints:
    readOnly: true
  name: entity-report
- description: Generate fundamentals report.
  hints:
    readOnly: true
  name: fundamentals-report
- description: Generate estimates report.
  hints:
    readOnly: true
  name: estimates-report
- description: Generate capital structure report.
  hints:
    readOnly: true
  name: capital-structure-report
- description: Generate overview report.
  hints:
    readOnly: true
  name: overview-report
- description: Generate ownership report.
  hints:
    readOnly: true
  name: ownership-report
- description: Generate a chart.
  hints:
    readOnly: true
  name: generate-chart
- description: Generate a digital card.
  hints:
    readOnly: true
  name: generate-digital-card
- description: Build a custom report book.
  hints:
    readOnly: true
  name: build-book
- description: Generate Vermilion report.
  hints:
    readOnly: true
  name: vermilion-report
---
