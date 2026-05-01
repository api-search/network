---
image: /assets/images/blog/network-update.png
layout: post
tags:
- Network Update
- Catalog Refresh
- Federal Government
- Providers
- APIs
title: 235 Providers and 717 APIs Added in Latest Rebuild
---


The APIs.io catalog grew by **235 providers and 717 APIs** in this rebuild — the largest single-cycle expansion since the agent-readiness work shipped two weeks ago. The running totals now sit at **1,699 providers** and **7,810 APIs** across the network, with 6,342 of those APIs carrying enough machine-readable description to land in the [`/.well-known/api-catalog`](https://apis.apis.io/.well-known/api-catalog) linkset (2,802 with full OpenAPI, AsyncAPI, or Postman specs).

The headline cluster this cycle is federal government. Roughly **60 of the new providers** are US federal departments, bureaus, agencies, and military components — Department of Energy, Department of Justice, Department of Veterans Affairs, Defense Logistics Agency, Drug Enforcement Administration, Energy Information Administration, Environmental Protection Agency, and dozens more. Where these providers publish open APIs (FDA openFDA, EPA Envirofacts, BJS data tools, Treasury Fiscal Data, EIA energy data) the catalog now lists them alongside their Fortune 500 peers — same apis.json structure, same canonical capability classification, same agent-readiness on every page. Where they don't yet publish APIs the profile still goes in as a breadcrumb, since government data discovery is one of the hardest problems an agent-facing catalog can help with.

The rest of the growth is broad: Microsoft 365 and Endpoint Manager join the existing Microsoft cluster; Oracle Hyperion and R12, Salesforce Lightning, Adobe Premiere Pro, Azure Data Factory and Machine Learning, Bloomberg Economics and Enterprise Data, Databricks Asset Bundles, plus a long tail of data tooling (Dagster, dbt, DataHub, Dataiku, DBOS, DatoCMS) and Fortune 500 companies (Danaher, Darden, Davita, Dean Foods, Delta, Dow). Schemas grew by **134**, JSON-LD documents by **72**, AsyncAPI specs by **17**, and Spectral rulesets by **40** — each new provider inheriting the agent-readiness scaffolding (RFC 9727 catalog membership, markdown content negotiation, source widgets, automatic categorization) without any per-provider intervention.

The pipeline picks them up; the network grows.
