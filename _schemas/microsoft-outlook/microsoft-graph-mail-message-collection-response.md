---
description: Collection of message resources with optional pagination link.
layout: schema
name: MessageCollectionResponse
properties_list:
- description: The OData context URL.
  name: '@odata.context'
  type: string
- description: The total count of matching resources.
  name: '@odata.count'
  type: integer
- description: The URL for the next page of results.
  name: '@odata.nextLink'
  type: string
- description: ''
  name: value
  type: array
provider_name: Microsoft Outlook
provider_slug: microsoft-outlook
schema_file: json-schema/microsoft-graph-mail-message-collection-response-schema.json
slug: microsoft-graph-mail-message-collection-response
tags:
- Calendar
- Contacts
- Email
- Enterprise
- Microsoft
- Office 365
- Productivity
title: MessageCollectionResponse
---
