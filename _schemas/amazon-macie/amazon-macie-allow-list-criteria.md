---
description: Specifies the criteria for an allow list. The criteria must specify a regular expression (regex) or an S3 object (s3WordsList). It can't specify both.
layout: schema
name: AllowListCriteria
properties_list:
- description: ''
  name: regex
  type: object
- description: ''
  name: s3WordsList
  type: object
provider_name: Amazon Macie
provider_slug: amazon-macie
schema_file: json-schema/amazon-macie-allow-list-criteria-schema.json
slug: amazon-macie-allow-list-criteria
tags:
- AWS
- Data Security
- Sensitive Data
- Privacy
- Compliance
- Machine Learning
- S3
title: AllowListCriteria
---
