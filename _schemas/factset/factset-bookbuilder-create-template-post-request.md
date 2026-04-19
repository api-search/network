---
description: The request body allows users to input the name of the template, ticker
layout: schema
name: createTemplatePostRequest
properties_list:
- description: name of the template
  name: tmpl_name
  type: string
- description: Type of the template (public,pc,pe,fi)
  name: tmpl_type
  type: string
- description: Content sections
  name: content
  type: array
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-bookbuilder-create-template-post-request-schema.json
slug: factset-bookbuilder-create-template-post-request
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: createTemplatePostRequest
---
