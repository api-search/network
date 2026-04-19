---
description: Response from listing investigations
layout: schema
name: ListInvestigationsResponse
properties_list:
- description: Lists the summary of uncommon behavior or malicious activity which indicates a compromise.
  name: InvestigationDetails
  type: array
- description: Lists investigations for a behavior graph based on the maximum number of investigations in a page.
  name: NextToken
  type: string
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-list-investigations-response-schema.json
slug: amazon-detective-list-investigations-response
tags:
- AWS
- Forensics
- Investigation
- Security
title: ListInvestigationsResponse
---
