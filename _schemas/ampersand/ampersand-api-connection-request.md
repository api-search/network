---
description: ConnectionRequest schema from Ampersand API
layout: schema
name: ConnectionRequest
properties_list:
- description: The ID of the provider workspace that this connection belongs to.
  name: providerWorkspaceRef
  type: string
- description: ''
  name: providerMetadata
  type: object
- description: The name of the user group that has access to this installation.
  name: groupName
  type: string
- description: The ID of the user group that has access to this installation.
  name: groupRef
  type: string
- description: The name of the consumer that has access to this installation.
  name: consumerName
  type: string
- description: The consumer reference.
  name: consumerRef
  type: string
- description: The provider name (e.g. "salesforce", "hubspot")
  name: provider
  type: string
- description: The API key to use for the connection.
  name: apiKey
  type: string
- description: Values used for custom auth input variables.
  name: customAuth
  type: object
- description: ''
  name: basicAuth
  type: object
- description: ''
  name: oauth2ClientCredentials
  type: object
- description: ''
  name: oauth2PasswordCredentials
  type: object
- description: ''
  name: oauth2AuthorizationCode
  type: object
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-connection-request-schema.json
slug: ampersand-api-connection-request
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: ConnectionRequest
---
