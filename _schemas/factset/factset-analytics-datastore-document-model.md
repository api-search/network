---
description: Document model
layout: schema
name: DocumentModel
properties_list:
- description: The resolved URL pointing to the location of the underlying report
  name: url
  type: string
- description: string property to denote what Product created this document.
  name: productType
  type: string
- description: The documents tags, represented in a key value format with the tag name as the key; and the tag's value as the value
  name: tags
  type: object
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-analytics-datastore-document-model-schema.json
slug: factset-analytics-datastore-document-model
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: DocumentModel
---
