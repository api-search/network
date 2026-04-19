---
consumed_apis:
- spot-eco
- spot-billing
- spot-admin
description: Unified workflow for cloud financial operations combining commitment management (Eco), billing analytics (Billing Engine), and cost optimization. Used by FinOps teams, cloud finance analysts, and platform administrators.
layout: capability
name: Spot FinOps
operations:
- description: List AWS commitment plans
  method: GET
  name: list-commitment-plans
  path: /v1/commitment-plans
- description: Get AWS savings analysis
  method: GET
  name: get-savings-analysis
  path: /v1/savings-analysis
- description: List billing accounts
  method: GET
  name: list-billing-accounts
  path: /v1/billing-accounts
- description: Get cost analysis
  method: GET
  name: get-cost-analysis
  path: /v1/cost-analysis
personas: []
provider_name: Spot
provider_slug: spot
search_terms:
- list billing account families
- list billing accounts
- savings analysis
- autoscaling
- eco list commitment plans aws
- eco get savings analysis gcp
- finops
- containers
- cloud infrastructure
- get cost analysis
- eco get commitment plan aws
- list commitment plans
- eco list commitment plans azure
- list aws reserved instances
- eco list commitment plans gcp
- spot
- list spot accounts for context
- get unused aws reserved instances
- get a specific aws commitment plan
- get azure savings analysis
- billing
- billing get cost analysis
- get gcp savings analysis
- kubernetes
- cost optimization
- list aws commitment plans
- get billing cost analysis
- eco list reserved instances aws
- spot instances
- cloud commitment plans
- cost analysis
- billing list accounts
- list aws savings plans
- get savings analysis
- eco get unused ris aws
- get aws commitment analysis
- list gcp commitment plans
- list billing engine accounts
- admin list accounts
- eco list savings plans aws
- list azure commitment plans
- eco get savings analysis azure
- eco get savings analysis aws
- eco get commitment analysis aws
- billing accounts
- billing list account families
- get aws savings analysis
slug: finops
tags:
- Spot
- FinOps
- Cost Optimization
- Billing
tools:
- description: List AWS commitment plans
  hints:
    openWorld: true
    readOnly: true
  name: eco-list-commitment-plans-aws
- description: Get a specific AWS commitment plan
  hints:
    readOnly: true
  name: eco-get-commitment-plan-aws
- description: Get AWS savings analysis
  hints:
    readOnly: true
  name: eco-get-savings-analysis-aws
- description: Get AWS commitment analysis
  hints:
    readOnly: true
  name: eco-get-commitment-analysis-aws
- description: List AWS savings plans
  hints:
    readOnly: true
  name: eco-list-savings-plans-aws
- description: List AWS reserved instances
  hints:
    readOnly: true
  name: eco-list-reserved-instances-aws
- description: Get unused AWS reserved instances
  hints:
    readOnly: true
  name: eco-get-unused-ris-aws
- description: List Azure commitment plans
  hints:
    readOnly: true
  name: eco-list-commitment-plans-azure
- description: Get Azure savings analysis
  hints:
    readOnly: true
  name: eco-get-savings-analysis-azure
- description: List GCP commitment plans
  hints:
    readOnly: true
  name: eco-list-commitment-plans-gcp
- description: Get GCP savings analysis
  hints:
    readOnly: true
  name: eco-get-savings-analysis-gcp
- description: List billing engine accounts
  hints:
    readOnly: true
  name: billing-list-accounts
- description: List billing account families
  hints:
    readOnly: true
  name: billing-list-account-families
- description: Get billing cost analysis
  hints:
    readOnly: true
  name: billing-get-cost-analysis
- description: List Spot accounts for context
  hints:
    readOnly: true
  name: admin-list-accounts
---
