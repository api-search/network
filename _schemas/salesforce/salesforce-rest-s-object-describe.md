---
description: Metadata describing a Salesforce SObject type, including its fields, relationships, and capabilities.
layout: schema
name: SObjectDescribe
properties_list:
- description: The API name of the SObject type.
  name: name
  type: string
- description: The user-facing singular label for this object type.
  name: label
  type: string
- description: The user-facing plural label for this object type.
  name: labelPlural
  type: string
- description: The three-character key prefix used in record IDs for this type.
  name: keyPrefix
  type: string
- description: Whether records of this type can be queried with SOQL.
  name: queryable
  type: boolean
- description: Whether records of this type can be searched with SOSL.
  name: searchable
  type: boolean
- description: Whether new records of this type can be created via the API.
  name: createable
  type: boolean
- description: Whether existing records of this type can be updated via the API.
  name: updateable
  type: boolean
- description: Whether records of this type can be deleted via the API.
  name: deletable
  type: boolean
- description: Detailed metadata for each field on this SObject type.
  name: fields
  type: array
- description: Map of REST endpoint URLs for this SObject type.
  name: urls
  type: object
provider_name: Salesforce
provider_slug: salesforce
schema_file: json-schema/salesforce-rest-s-object-describe-schema.json
slug: salesforce-rest-s-object-describe
tags:
- AI
- Analytics
- Cloud
- Commerce
- CRM
- Customer Service
- Enterprise
- Marketing
- Platform
- Sales
title: SObjectDescribe
---
