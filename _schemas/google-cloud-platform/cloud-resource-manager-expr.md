---
description: Represents a textual expression in the Common Expression Language (CEL) syntax. Used for conditional access policies.
layout: schema
name: Expr
properties_list:
- description: 'The CEL expression string. Example: request.time < timestamp("2024-01-01T00:00:00Z").'
  name: expression
  type: string
- description: An optional title for the expression.
  name: title
  type: string
- description: An optional description of the expression.
  name: description
  type: string
- description: An optional string indicating the location of the expression for error reporting.
  name: location
  type: string
provider_name: Google Cloud Platform
provider_slug: google-cloud-platform
schema_file: json-schema/cloud-resource-manager-expr-schema.json
slug: cloud-resource-manager-expr
tags:
- API Management
- Cloud Computing
- Infrastructure
- Platform as a Service
title: Expr
---
