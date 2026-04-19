---
description: Describes the basic configuration needed for building and running an App Runner service. This type doesn't support the full set of possible configuration options. Fur full configuration capabilities, use a <code>apprunner.yaml</code> file in the source code repository.
layout: schema
name: CodeConfigurationValues
properties_list:
- description: ''
  name: Runtime
  type: object
- description: ''
  name: BuildCommand
  type: object
- description: ''
  name: StartCommand
  type: object
- description: ''
  name: Port
  type: object
- description: ''
  name: RuntimeEnvironmentVariables
  type: object
- description: ''
  name: RuntimeEnvironmentSecrets
  type: object
provider_name: Amazon App Runner
provider_slug: amazon-app-runner
schema_file: json-schema/amazon-app-runner-codeconfigurationvalues-schema.json
slug: amazon-app-runner-codeconfigurationvalues
tags:
- AWS
- CI/CD
- Containers
- Deployment
- Managed Service
- Serverless
- Web Applications
title: CodeConfigurationValues
---
