---
description: Standard response header returned by all Transact API operations
layout: schema
name: ResponseHeader
properties_list:
- description: Unique identifier for the resource
  name: id
  type: string
- description: Status of the operation (success, error)
  name: status
  type: string
- description: Transaction lifecycle status
  name: transactionStatus
  type: string
- description: ''
  name: audit
  type: object
provider_name: Temenos Transact
provider_slug: temenos-transact
schema_file: json-schema/temenos-transact-core-banking-response-header-schema.json
slug: temenos-transact-core-banking-response-header
tags:
- Banking
- Core Banking
- Digital Banking
- Enterprise
- Financial Services
- Fintech
title: ResponseHeader
---
