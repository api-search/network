---
description: agreement schema from Acquia Cloud API
layout: schema
name: Agreement
properties_list:
- description: The agreement UUID.
  name: uuid
  type: string
- description: The agreement document UUID.
  name: document_uuid
  type: string
- description: The name of the agreement.
  name: title
  type: string
- description: The formatted agreement content.
  name: body
  type: string
- description: The status of the agreement.
  name: status
  type: string
- description: The date the agreement was created.
  name: created_at
  type: string
- description: The date the agreement was last updated.
  name: updated_at
  type: string
- description: ''
  name: actioned_by
  type: object
- description: A reference to the entity for this agreement.
  name: reference
  type: object
- description: ''
  name: _links
  type: object
provider_name: Acquia
provider_slug: acquia
schema_file: json-schema/acquia-cloud-agreement-schema.json
slug: acquia-cloud-agreement
tags:
- Content
- Experience
title: Agreement
---
