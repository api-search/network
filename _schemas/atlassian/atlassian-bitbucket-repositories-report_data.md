---
description: A key-value element that will be displayed along with the report.
layout: schema
name: report_data
properties_list:
- description: The type of data contained in the value field. If not provided, then the value will be detected as a boolean, number or string.
  name: type
  type: string
- description: A string describing what this data field represents.
  name: title
  type: string
- description: The value of the data element.
  name: value
  type: object
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-bitbucket-repositories-report_data-schema.json
slug: atlassian-bitbucket-repositories-report_data
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: report_data
---
