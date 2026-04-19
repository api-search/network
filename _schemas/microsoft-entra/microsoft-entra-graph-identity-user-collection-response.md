---
description: Paged collection of user objects
layout: schema
name: UserCollectionResponse
properties_list:
- description: OData context URL
  name: '@odata.context'
  type: string
- description: Total count of matching resources (if $count=true)
  name: '@odata.count'
  type: integer
- description: URL to retrieve the next page of results
  name: '@odata.nextLink'
  type: string
- description: ''
  name: value
  type: array
provider_name: Microsoft Entra
provider_slug: microsoft-entra
schema_file: json-schema/microsoft-entra-graph-identity-user-collection-response-schema.json
slug: microsoft-entra-graph-identity-user-collection-response
tags:
- Access Management
- Authentication
- Azure AD
- Entra
- Identity
- Identity Governance
- Microsoft
- Network Security
- Security
- Zero Trust
title: UserCollectionResponse
---
