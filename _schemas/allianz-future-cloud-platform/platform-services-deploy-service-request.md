---
description: Request body for triggering a service deployment
layout: schema
name: DeployServiceRequest
properties_list:
- description: Version tag to deploy
  name: version
  type: string
- description: Container image with version tag
  name: image
  type: string
- description: Deployment strategy
  name: strategy
  type: string
provider_name: Allianz Future Cloud Platform
provider_slug: allianz-future-cloud-platform
schema_file: json-schema/platform-services-deploy-service-request-schema.json
slug: platform-services-deploy-service-request
tags:
- Cloud Platform
- Enterprise
- Financial Services
- Insurance
- Platform Engineering
- Kubernetes
title: DeployServiceRequest
---
