---
image: /assets/images/blog/network-update-2.png
layout: post
tags:
- Network Update
- Catalog Refresh
- Federal Government
- Financial Services
- Data Engineering
- Providers
- APIs
title: Another 245 Providers and 599 APIs Added
---


The APIs.io catalog added another **245 providers and 599 APIs** in a second rebuild cycle today, pushing the running totals to **1,944 providers** and **8,409 APIs** — the first time the network has crossed 8,000 APIs. The [`/.well-known/api-catalog`](https://apis.apis.io/.well-known/api-catalog) linkset now covers **6,731 APIs**, with **2,973 carrying machine-readable OpenAPI, AsyncAPI, or Postman descriptions**.

This cycle is alphabetically anchored in the F-section of the index. The new entries include a second wave of **US federal agencies** — Food and Drug Administration, Food Safety and Inspection Service, Fish and Wildlife Service, Forest Service, Foreign Agricultural Service, and the Foreign Claims Settlement Commission — extending the government cluster from the morning's rebuild and pushing the federal footprint in the catalog well past 80 agencies. For a catalog that aims to be useful to agents working with public data, having every major federal data publisher indexed in the same structure as Stripe or Salesforce is the point.

**Financial services** fill in more of the picture this round: Fiserv, FIS, First American Financial, First Citizens Bancshares, and First Data add payment infrastructure and banking rails that were previously gaps in the catalog's coverage of the financial stack. **Data engineering** is also well-represented — Fivetran, Flatfile, Flyte, Fluent Bit, Fluentd, and FluxCD join the growing data tooling section alongside the prior cycle's Dagster, dbt, and DataHub entries. On the cloud-native side, Flannel, Flask, Flatcar Container Linux, Fly.io, and FMC round out the open-source infrastructure tier. Azure Data Factory and Azure Machine Learning slot into the existing Azure cluster, filling two notable gaps.

Other build metrics this cycle: **+182 schemas**, **+10 AsyncAPI specs**, **+115 JSON-LD documents**, **+14 Spectral rulesets**, and **+2 capabilities** (the catalog's first two new capability bundles since the HubSpot profiling work). The pipeline picks them up; the network grows.
