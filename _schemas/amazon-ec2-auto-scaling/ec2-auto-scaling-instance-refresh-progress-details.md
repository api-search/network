---
description: Reports progress on replacing instances in an Auto Scaling group that has a warm pool. This includes separate details for instances in the warm pool and instances in the Auto Scaling group (the live pool).
layout: schema
name: InstanceRefreshProgressDetails
properties_list:
- description: ''
  name: LivePoolProgress
  type: object
- description: ''
  name: WarmPoolProgress
  type: object
provider_name: Amazon EC2 Auto Scaling
provider_slug: amazon-ec2-auto-scaling
schema_file: json-schema/ec2-auto-scaling-instance-refresh-progress-details-schema.json
slug: ec2-auto-scaling-instance-refresh-progress-details
tags:
- Amazon Web Services
- Auto Scaling
- AWS
- Compute
- EC2
- High Availability
- Scaling
title: InstanceRefreshProgressDetails
---
