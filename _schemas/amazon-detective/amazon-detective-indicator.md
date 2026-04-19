---
description: An indicator of compromise detected during an investigation
layout: schema
name: Indicator
properties_list:
- description: The type of indicator.
  name: IndicatorType
  type: string
- description: Details about the indicator of compromise.
  name: IndicatorDetail
  type: object
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-indicator-schema.json
slug: amazon-detective-indicator
tags:
- AWS
- Forensics
- Investigation
- Security
title: Indicator
---
