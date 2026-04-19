---
description: A service deployment record on the platform
layout: schema
name: Deployment
properties_list:
- description: Unique identifier for the deployment
  name: deployment_id
  type: string
- description: Service this deployment belongs to
  name: service_id
  type: string
- description: Version being deployed
  name: version
  type: string
- description: Container image with tag
  name: image
  type: string
- description: Current deployment status
  name: status
  type: string
- description: Deployment strategy used
  name: strategy
  type: string
- description: Timestamp when the deployment completed
  name: deployed_at
  type: string
- description: Actor that triggered the deployment
  name: deployed_by
  type: string
- description: Timestamp when the deployment was initiated
  name: initiated_at
  type: string
provider_name: Allianz Future Cloud Platform
provider_slug: allianz-future-cloud-platform
schema_file: json-schema/platform-services-deployment-schema.json
slug: platform-services-deployment
tags:
- Cloud Platform
- Enterprise
- Financial Services
- Insurance
- Platform Engineering
- Kubernetes
title: Deployment
---
