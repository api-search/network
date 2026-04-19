---
description: The request body allows users to input the name of the book, ticker
layout: schema
name: createBookPostRequest
properties_list:
- description: name of the book
  name: book_name
  type: string
- description: Identifier.
  name: ticker
  type: string
- description: options for pagination
  name: pagination
  type: object
- description: Content sections
  name: content
  type: array
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-bookbuilder-create-book-post-request-schema.json
slug: factset-bookbuilder-create-book-post-request
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: createBookPostRequest
---
