---
description: Worker configuration defining the compute resources allocated to a CloudHub application, including the number of workers and their size.
layout: schema
name: WorkerConfig
properties_list:
- description: Number of worker instances
  name: amount
  type: integer
- description: Worker type defining the vCore size and memory
  name: type
  type: object
provider_name: MuleSoft
provider_slug: mulesoft
schema_file: json-schema/mulesoft-anypoint-platform-worker-config-schema.json
slug: mulesoft-anypoint-platform-worker-config
tags:
- API Gateway
- API Management
- Enterprise
- Integration
title: WorkerConfig
---
