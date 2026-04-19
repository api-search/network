---
description: Fields that can be updated on an organization
layout: schema
name: OrganizationUpdate
properties_list:
- description: Display name of the organization
  name: name
  type: string
- description: User ID of the new organization owner
  name: ownerId
  type: string
- description: Session timeout in minutes
  name: sessionTimeout
  type: integer
- description: Whether multi-factor authentication is required
  name: mfaRequired
  type: boolean
provider_name: MuleSoft
provider_slug: mulesoft
schema_file: json-schema/mulesoft-anypoint-platform-organization-update-schema.json
slug: mulesoft-anypoint-platform-organization-update
tags:
- API Gateway
- API Management
- Enterprise
- Integration
title: OrganizationUpdate
---
