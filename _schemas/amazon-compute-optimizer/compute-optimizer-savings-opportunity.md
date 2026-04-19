---
description: <p>Describes the savings opportunity for recommendations of a given resource type or for the recommendation option of an individual resource.</p> <p>Savings opportunity represents the estimated monthly savings you can achieve by implementing a given Compute Optimizer recommendation.</p> <important> <p>Savings opportunity data requires that you opt in to Cost Explorer, as well as activate <b>Receive Amazon EC2 resource recommendations</b> in the Cost Explorer preferences page. That creates a connection between Cost Explorer and Compute Optimizer. With this connection, Cost Explorer generates savings estimates considering the price of existing resources, the price of recommended resources, and historical usage data. Estimated monthly savings reflects the projected dollar savings associated with each of the recommendations generated. For more information, see <a href="https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html">Enabling Cost Explorer</a> and <a
  href="https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html">Optimizing your cost with Rightsizing Recommendations</a> in the <i>Cost Management User Guide</i>.</p> </important>
layout: schema
name: SavingsOpportunity
properties_list:
- description: ''
  name: savingsOpportunityPercentage
  type: object
- description: ''
  name: estimatedMonthlySavings
  type: object
provider_name: Amazon Compute Optimizer
provider_slug: amazon-compute-optimizer
schema_file: json-schema/compute-optimizer-savings-opportunity-schema.json
slug: compute-optimizer-savings-opportunity
tags:
- AWS
- Cost Optimization
- FinOps
- Machine Learning
- Resource Recommendations
title: SavingsOpportunity
---
