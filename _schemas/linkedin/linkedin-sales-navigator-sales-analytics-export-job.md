---
description: SalesAnalyticsExportJob from LinkedIn API
layout: schema
name: SalesAnalyticsExportJob
properties_list:
- description: A unique identifier for the job
  name: id
  type: integer
- description: Current status of the export job
  name: status
  type: string
- description: URL for downloading the exported data when job is completed
  name: downloadUrl
  type: string
- description: Expiration timestamp of the download URL
  name: expireAt
  type: integer
- description: Number of rows in the exported data
  name: rowCount
  type: integer
provider_name: LinkedIn
provider_slug: linkedin
schema_file: json-schema/linkedin-sales-navigator-sales-analytics-export-job-schema.json
slug: linkedin-sales-navigator-sales-analytics-export-job
tags:
- Business
- Careers
- Marketing
- Professional Networking
- Recruiting
- Social Media
title: SalesAnalyticsExportJob
---
