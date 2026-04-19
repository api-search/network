---
description: <p>The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.</p> <note> <p>Provided <code>securityGroupIds</code> and <code>subnetIds</code> must be part of the same VPC.</p> <p>Connecting to a private VPC is not yet available in the Asia Pacific (Seoul) Region (ap-northeast-2).</p> </note>
layout: schema
name: VpcConfiguration
properties_list:
- description: ''
  name: securityGroupIds
  type: object
- description: ''
  name: subnetIds
  type: object
provider_name: Amazon Managed Grafana
provider_slug: amazon-managed-grafana
schema_file: json-schema/amazon-managed-grafana-vpc-configuration-schema.json
slug: amazon-managed-grafana-vpc-configuration
tags:
- AWS
- Dashboards
- Monitoring
- Observability
- Visualization
title: VpcConfiguration
---
