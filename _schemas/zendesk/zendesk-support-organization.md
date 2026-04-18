---
description: A Zendesk organization representing a company or group of users.
layout: schema
name: Organization
properties_list:
- description: Automatically assigned organization ID.
  name: id
  type: integer
- description: The API URL of the organization.
  name: url
  type: string
- description: The name of the organization.
  name: name
  type: string
- description: Details about the organization.
  name: details
  type: string
- description: Notes about the organization visible only to agents.
  name: notes
  type: string
- description: Domain names associated with the organization. Users with matching email domains can be auto-assigned.
  name: domain_names
  type: array
- description: The default group assigned to tickets from this organization.
  name: group_id
  type: integer
- description: Whether end users in the organization can see each other's tickets.
  name: shared_tickets
  type: boolean
- description: Whether end users in the organization can see each other's comments on tickets.
  name: shared_comments
  type: boolean
- description: An external ID from an integrated system.
  name: external_id
  type: string
- description: Tags applied to the organization.
  name: tags
  type: array
- description: Custom organization field values (key-value pairs).
  name: organization_fields
  type: object
- description: When the organization was created (ISO 8601).
  name: created_at
  type: string
- description: When the organization was last updated (ISO 8601).
  name: updated_at
  type: string
provider_name: Zendesk
provider_slug: zendesk
schema_file: json-schema/zendesk-support-organization-schema.json
slug: zendesk-support-organization
tags:
- Chat
- CRM
- Help Center
- Sell
- Support
- T1
- Talk
- Ticketing
- Tickets
title: Organization
---
