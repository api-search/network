---
consumed_apis:
- amazon-api-gateway
description: Workflow capability for managing API Gateway REST APIs including lifecycle management, stage deployment, and configuration.
layout: capability
name: Amazon API Gateway Management
operations:
- description: List REST APIs.
  method: GET
  name: list-rest-apis
  path: /v1/rest-apis
personas: []
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
search_terms:
- list all rest apis configured in amazon api gateway.
- rest api
- Platform Engineer
- create rest api
- websocket
- list rest apis
- manage api gateway rest apis, resources, stages, and deployments.
- api gateway
- serverless
- amazon
- list rest apis.
- http api
- gateway
- create a new rest api in amazon api gateway.
- API Developer
- developer creating and managing rest apis on amazon api gateway.
- aws
- api management
- engineer managing api infrastructure and deployments across environments.
slug: api-gateway-management
tags:
- Amazon
- API Gateway
- AWS
- API Management
tools:
- description: List all REST APIs configured in Amazon API Gateway.
  hints:
    openWorld: false
    readOnly: true
  name: list-rest-apis
- description: Create a new REST API in Amazon API Gateway.
  hints:
    openWorld: false
    readOnly: false
  name: create-rest-api
---
