---
description: Represents a single JSON Patch operation (RFC 6902). Only supports add, remove, and replace operations for config updates.
layout: schema
name: JSONPatchOperation
properties_list:
- description: 'The operation to perform. - "add": Adds a new field or replaces an existing one at the specified path - "remove": Removes the field at the specified path - "replace": Replaces the value at the specifi'
  name: op
  type: string
- description: JSON Pointer path to the field to operate on (RFC 6901). All paths must start with "/" (e.g., "/schedule", "/selectedFields/phone").
  name: path
  type: string
- description: The value to set for add/replace operations. Not used for remove operations.
  name: value
  type: object
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-json-patch-operation-schema.json
slug: ampersand-api-json-patch-operation
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: JSONPatchOperation
---
