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
- eco get savings analysis aws
- finops
- cloud infrastructure
- list commitment plans
- cost optimization
- list aws reserved instances
- billing accounts
- billing
- eco list commitment plans azure
- list billing engine accounts
- eco list reserved instances aws
- list billing account families
- get billing cost analysis
- billing list account families
- get cost analysis
- get azure savings analysis
- savings analysis
- get aws savings analysis
- eco get commitment plan aws
- list aws savings plans
- eco get savings analysis azure
- eco list commitment plans aws
- list azure commitment plans
- list gcp commitment plans
- get a specific aws commitment plan
- containers
- spot
- list aws commitment plans
- cost analysis
- get unused aws reserved instances
- cloud commitment plans
- billing get cost analysis
- eco list commitment plans gcp
- eco list savings plans aws
- spot instances
- get gcp savings analysis
- eco get savings analysis gcp
- eco get unused ris aws
- get savings analysis
- admin list accounts
- list billing accounts
- autoscaling
- list spot accounts for context
- get aws commitment analysis
- eco get commitment analysis aws
- billing list accounts
- kubernetes
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
