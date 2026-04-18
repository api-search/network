---
description: A Plugin entity represents a plugin configuration that will be executed during the HTTP request/response lifecycle. Plugins provide extra functionality such as authentication, rate limiting, and transformations.
layout: schema
name: Plugin
properties_list:
- description: The unique identifier of the Plugin.
  name: id
  type: string
- description: The name of the plugin (e.g., rate-limiting, key-auth, cors).
  name: name
  type: string
- description: An optional custom name to identify an instance of the plugin.
  name: instance_name
  type: string
- description: The configuration properties for the Plugin which vary depending on the plugin being configured.
  name: config
  type: object
- description: A list of the request protocols that will trigger this plugin.
  name: protocols
  type: array
- description: Whether the plugin is applied.
  name: enabled
  type: boolean
- description: An optional set of strings for grouping and filtering.
  name: tags
  type: array
- description: Describes a dependency to another plugin to determine plugin ordering during the access phase (Enterprise only).
  name: ordering
  type: object
- description: If set, the plugin will only activate when receiving requests via the specified Service.
  name: service
  type: object
- description: If set, the plugin will only activate when receiving requests via the specified Route.
  name: route
  type: object
- description: If set, the plugin will activate only for requests where the specified Consumer has been authenticated.
  name: consumer
  type: object
- description: If set, the plugin will activate only for requests within the specified Consumer Group.
  name: consumer_group
  type: object
- description: Unix epoch timestamp of when the entity was created.
  name: created_at
  type: integer
- description: Unix epoch timestamp of when the entity was last updated.
  name: updated_at
  type: integer
provider_name: Kong
provider_slug: kong
schema_file: json-schema/kong-gateway-admin-plugin-schema.json
slug: kong-gateway-admin-plugin
tags:
- API Gateway
- Lua
- NGINX
- Open Source
title: Plugin
---
