---
description: Represents a B2B Data Interchange transformer — defines how X12 EDI documents are converted to and from JSON or XML using mapping templates.
layout: schema
name: Transformer
properties_list:
- description: Unique identifier for the transformer
  name: transformerId
  type: string
- description: Amazon Resource Name (ARN) for the transformer
  name: transformerArn
  type: string
- description: Name of the transformer
  name: name
  type: string
- description: Current status of the transformer
  name: status
  type: string
- description: Output file format for the transformer
  name: fileFormat
  type: string
- description: JSONata or XSLT mapping template content
  name: mappingTemplate
  type: string
- description: EDI type configuration for the transformer
  name: ediType
  type: object
- description: Timestamp when the transformer was created
  name: createdAt
  type: string
- description: Timestamp when the transformer was last modified
  name: modifiedAt
  type: string
provider_name: Amazon B2B Data Interchange
provider_slug: amazon-b2b-data-interchange
schema_file: json-schema/transformer.json
slug: transformer
tags:
- EDI
- B2B
- Data Interchange
- Supply Chain
- Healthcare
- Financial Services
- Amazon Web Services
- AWS
title: Transformer
---
