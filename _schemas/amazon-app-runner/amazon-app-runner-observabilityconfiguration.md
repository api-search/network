---
description: <p>Describes an App Runner observability configuration resource. Multiple revisions of a configuration have the same <code>ObservabilityConfigurationName</code> and different <code>ObservabilityConfigurationRevision</code> values.</p> <p>The resource is designed to configure multiple features (currently one feature, tracing). This type contains optional members that describe the configuration of these features (currently one member, <code>TraceConfiguration</code>). If a feature member isn't specified, the feature isn't enabled.</p>
layout: schema
name: ObservabilityConfiguration
properties_list:
- description: ''
  name: ObservabilityConfigurationArn
  type: object
- description: ''
  name: ObservabilityConfigurationName
  type: object
- description: ''
  name: TraceConfiguration
  type: object
- description: ''
  name: ObservabilityConfigurationRevision
  type: object
- description: ''
  name: Latest
  type: object
- description: ''
  name: Status
  type: object
- description: ''
  name: CreatedAt
  type: object
- description: ''
  name: DeletedAt
  type: object
provider_name: Amazon App Runner
provider_slug: amazon-app-runner
schema_file: json-schema/amazon-app-runner-observabilityconfiguration-schema.json
slug: amazon-app-runner-observabilityconfiguration
tags:
- AWS
- CI/CD
- Containers
- Deployment
- Managed Service
- Serverless
- Web Applications
title: ObservabilityConfiguration
---
