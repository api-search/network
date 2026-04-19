---
description: DomainStatus schema
layout: schema
name: DomainStatus
properties_list:
- description: ''
  name: DomainId
  type: string
- description: ''
  name: DomainName
  type: string
- description: ''
  name: ARN
  type: string
- description: ''
  name: Created
  type: boolean
- description: ''
  name: Deleted
  type: boolean
- description: ''
  name: Processing
  type: boolean
- description: ''
  name: RequiresIndexDocuments
  type: boolean
- description: ''
  name: SearchInstanceCount
  type: integer
- description: ''
  name: SearchInstanceType
  type: string
- description: ''
  name: DocService
  type: object
- description: ''
  name: SearchService
  type: object
provider_name: Amazon CloudSearch
provider_slug: amazon-cloudsearch
schema_file: json-schema/cloudsearch-domain-status-schema.json
slug: cloudsearch-domain-status
tags:
- AWS
- CloudSearch
- Search
- Full-Text Search
- Managed
title: DomainStatus
---
