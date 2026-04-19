---
description: Represents an audit event recording an action performed by a team member within the 1Password account.
layout: schema
name: AuditEvent
properties_list:
- description: The unique identifier for the audit event.
  name: uuid
  type: string
- description: When the action was performed.
  name: timestamp
  type: string
- description: The UUID of the user who performed the action.
  name: actor_uuid
  type: string
- description: ''
  name: actor_details
  type: object
- description: The type of action that was performed.
  name: action
  type: string
- description: The type of object the action was performed on.
  name: object_type
  type: string
- description: The UUID of the object the action was performed on.
  name: object_uuid
  type: string
- description: Additional details about the object of the action.
  name: object_details
  type: object
- description: An auxiliary identifier providing additional context.
  name: aux_id
  type: integer
- description: An auxiliary UUID providing additional context.
  name: aux_uuid
  type: string
- description: Additional auxiliary details about the event.
  name: aux_details
  type: object
- description: Additional auxiliary information about the event.
  name: aux_info
  type: string
- description: Information about the session in which the action occurred.
  name: session
  type: object
- description: ''
  name: location
  type: object
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-events-audit-event-schema.json
slug: 1password-events-audit-event
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: AuditEvent
---
