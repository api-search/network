---
description: <p>The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition.</p> <note> <p>Environment variables cannot start with "<code>Batch</code>". This naming convention is reserved for variables that Batch sets.</p> </note>
layout: schema
name: BatchEnvironmentVariable
properties_list:
- description: ''
  name: Name
  type: object
- description: ''
  name: Value
  type: object
provider_name: Amazon EventBridge Pipes
provider_slug: amazon-eventbridge-pipes
schema_file: json-schema/amazon-eventbridge-pipes-batch-environment-variable-schema.json
slug: amazon-eventbridge-pipes-batch-environment-variable
tags:
- Amazon Web Services
- AWS
- Event-Driven
- Integration
- Messaging
- Serverless
title: BatchEnvironmentVariable
---
