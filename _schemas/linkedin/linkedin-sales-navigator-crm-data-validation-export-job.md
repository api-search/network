---
description: CrmDataValidationExportJob from LinkedIn API
layout: schema
name: CrmDataValidationExportJob
properties_list:
- description: Export job ID
  name: jobId
  type: integer
- description: Start time of the export
  name: exportStartAt
  type: integer
- description: End time of the export
  name: exportEndAt
  type: integer
- description: Current status of the export job
  name: status
  type: string
- description: URLs for downloading the exported data
  name: downloadUrls
  type: array
- description: Suggested start time for next export
  name: nextExportStartAt
  type: integer
- description: Expiration timestamp for download URLs
  name: expireAt
  type: integer
provider_name: LinkedIn
provider_slug: linkedin
schema_file: json-schema/linkedin-sales-navigator-crm-data-validation-export-job-schema.json
slug: linkedin-sales-navigator-crm-data-validation-export-job
tags:
- Business
- Careers
- Marketing
- Professional Networking
- Recruiting
- Social Media
title: CrmDataValidationExportJob
---
