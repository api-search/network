---
description: Request body for executing a connector action
layout: schema
name: ExecuteActionRequest
properties_list:
- description: Identifier of the user executing the action
  name: userId
  type: string
- description: Credential identifier to use for authentication
  name: credentialId
  type: string
- description: Action-specific parameters
  name: parameters
  type: object
provider_name: Alloy Automation
provider_slug: alloy-automation
schema_file: json-schema/alloy-connectivity-execute_action_request-schema.json
slug: alloy-connectivity-execute_action_request
tags:
- Automation
- Embedded Integrations
- Integrations
- iPaaS
- Unified API
- Workflows
title: ExecuteActionRequest
---
