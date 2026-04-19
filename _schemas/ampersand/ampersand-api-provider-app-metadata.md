---
description: Provider-specific configuration that extends the standard OAuth flow.
layout: schema
name: ProviderAppMetadata
properties_list:
- description: Additional query parameters to include in the OAuth authorization URL (e.g., optional_scope for HubSpot).
  name: authQueryParams
  type: object
- description: Provider-specific string values keyed by names (e.g., packageInstallURL for Salesforce, gcpProjectId and gcpPubSubTopicName for Gmail).
  name: providerParams
  type: object
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-provider-app-metadata-schema.json
slug: ampersand-api-provider-app-metadata
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: ProviderAppMetadata
---
