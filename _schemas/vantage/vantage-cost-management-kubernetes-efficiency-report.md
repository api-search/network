---
description: ''
layout: schema
name: KubernetesEfficiencyReport
properties_list:
- description: The unique token identifier for the report.
  name: token
  type: string
- description: The Kubernetes cluster name.
  name: cluster_name
  type: string
- description: The Kubernetes namespace.
  name: namespace
  type: string
- description: The idle cost for the cluster/namespace.
  name: idle_cost
  type: string
- description: The total cost for the cluster/namespace.
  name: total_cost
  type: string
- description: The efficiency percentage.
  name: efficiency
  type: number
- description: The date and time the report was generated.
  name: created_at
  type: string
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/vantage-cost-management-kubernetes-efficiency-report-schema.json
slug: vantage-cost-management-kubernetes-efficiency-report
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: KubernetesEfficiencyReport
---
