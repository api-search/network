---
consumed_apis:
- kong-admin
description: API gateway management workflow for platform engineers to configure services, routes, plugins, consumers, upstreams, and TLS certificates on Kong Gateway instances.
layout: capability
name: Kong API Gateway Management
operations:
- description: Retrieve gateway node info.
  method: GET
  name: get-node-info
  path: /v1/info
- description: List all services.
  method: GET
  name: list-services
  path: /v1/services
- description: Create a new service.
  method: POST
  name: create-service
  path: /v1/services
- description: List all routes.
  method: GET
  name: list-routes
  path: /v1/routes
- description: Create a new route.
  method: POST
  name: create-route
  path: /v1/routes
- description: List all consumers.
  method: GET
  name: list-consumers
  path: /v1/consumers
- description: List all plugins.
  method: GET
  name: list-plugins
  path: /v1/plugins
personas: []
provider_name: Kong
provider_slug: kong
search_terms:
- create a new upstream service.
- plugin management.
- kong
- update route
- list all configured plugins.
- update a route.
- retrieve a specific route.
- list all tags and tagged entities.
- create consumer
- open source
- retrieve kong gateway node information.
- create a new route.
- delete service
- list certificates
- api gateway
- create route
- delete a service.
- list services
- list all plugins.
- delete an upstream.
- delete upstream
- list all configured routes.
- update a service configuration.
- retrieve kong gateway node status.
- create a new route for a service.
- create plugin
- delete route
- list all upstream load balancers.
- retrieve a specific service.
- list all api consumers.
- list upstreams
- list consumers
- get plugin
- get service
- retrieve a specific plugin configuration.
- create upstream
- list all configured upstream services.
- list all tls certificates.
- nginx
- create a new api consumer.
- update service
- delete a consumer.
- delete consumer
- list all services.
- gateway node information.
- create a new upstream for load balancing.
- get route
- create a new plugin configuration.
- route management.
- delete a plugin.
- lua
- retrieve gateway node info.
- configuration
- create a new service.
- list all enabled plugin names on the node.
- list enabled plugins
- list tags
- list all consumers.
- get node info
- list all routes.
- retrieve a specific consumer.
- delete plugin
- get node status
- api consumer management.
- list plugins
- delete a route.
- get consumer
- upstream service management.
- list routes
- create service
slug: api-gateway-management
tags:
- Kong
- API Gateway
- Configuration
tools:
- description: Retrieve Kong Gateway node information.
  hints:
    readOnly: true
  name: get-node-info
- description: Retrieve Kong Gateway node status.
  hints:
    readOnly: true
  name: get-node-status
- description: List all configured upstream services.
  hints:
    readOnly: true
  name: list-services
- description: Create a new upstream service.
  hints:
    readOnly: false
  name: create-service
- description: Retrieve a specific service.
  hints:
    readOnly: true
  name: get-service
- description: Update a service configuration.
  hints:
    idempotent: true
    readOnly: false
  name: update-service
- description: Delete a service.
  hints:
    destructive: true
  name: delete-service
- description: List all configured routes.
  hints:
    readOnly: true
  name: list-routes
- description: Create a new route for a service.
  hints:
    readOnly: false
  name: create-route
- description: Retrieve a specific route.
  hints:
    readOnly: true
  name: get-route
- description: Update a route.
  hints:
    idempotent: true
    readOnly: false
  name: update-route
- description: Delete a route.
  hints:
    destructive: true
  name: delete-route
- description: List all API consumers.
  hints:
    readOnly: true
  name: list-consumers
- description: Create a new API consumer.
  hints:
    readOnly: false
  name: create-consumer
- description: Retrieve a specific consumer.
  hints:
    readOnly: true
  name: get-consumer
- description: Delete a consumer.
  hints:
    destructive: true
  name: delete-consumer
- description: List all configured plugins.
  hints:
    readOnly: true
  name: list-plugins
- description: Create a new plugin configuration.
  hints:
    readOnly: false
  name: create-plugin
- description: Retrieve a specific plugin configuration.
  hints:
    readOnly: true
  name: get-plugin
- description: Delete a plugin.
  hints:
    destructive: true
  name: delete-plugin
- description: List all enabled plugin names on the node.
  hints:
    readOnly: true
  name: list-enabled-plugins
- description: List all upstream load balancers.
  hints:
    readOnly: true
  name: list-upstreams
- description: Create a new upstream for load balancing.
  hints:
    readOnly: false
  name: create-upstream
- description: Delete an upstream.
  hints:
    destructive: true
  name: delete-upstream
- description: List all TLS certificates.
  hints:
    readOnly: true
  name: list-certificates
- description: List all tags and tagged entities.
  hints:
    readOnly: true
  name: list-tags
---
