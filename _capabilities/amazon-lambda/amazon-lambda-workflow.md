---
consumed_apis:
- lambda
description: Unified workflow capability for Amazon Lambda combining resource management and operations.
layout: capability
name: Amazon Lambda Workflow
operations: []
personas: []
provider_name: Amazon Lambda
provider_slug: amazon-lambda
search_terms:
- functions
- functions list functions
- returns details about an event source mapping.
- event-driven
- functions get function
- lists event source mappings.
- integrates api into applications
- event source mappings get event source mapping
- returns information about the function or function version.
- faas
- functions create function
- workflow
- event source mappings create event source mapping
- creates a lambda function.
- unified workflow for amazon lambda resource management
- creates a mapping between an event source and an aws lambda function.
- aws
- serverless
- Administrator
- amazon lambda
- Developer
- manages resources and configurations
- compute
- event source mappings list event source mappings
- returns a list of lambda functions, with the version-specific configuration of each.
slug: amazon-lambda-workflow
tags:
- Amazon Lambda
- AWS
- Workflow
tools:
- description: Creates a Lambda function.
  hints:
    idempotent: false
    readOnly: false
  name: functions-create-function
- description: Returns a list of Lambda functions, with the version-specific configuration of each.
  hints:
    idempotent: true
    readOnly: true
  name: functions-list-functions
- description: Returns information about the function or function version.
  hints:
    idempotent: true
    readOnly: true
  name: functions-get-function
- description: Creates a mapping between an event source and an AWS Lambda function.
  hints:
    idempotent: false
    readOnly: false
  name: event-source-mappings-create-event-source-mapping
- description: Lists event source mappings.
  hints:
    idempotent: true
    readOnly: true
  name: event-source-mappings-list-event-source-mappings
- description: Returns details about an event source mapping.
  hints:
    idempotent: true
    readOnly: true
  name: event-source-mappings-get-event-source-mapping
---
