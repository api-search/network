---
description: Information about a data export job.
layout: schema
name: ExportJob
properties_list:
- description: The unique export job ID.
  name: id
  type: string
- description: When the export was created.
  name: created_at
  type: string
- description: The type of data being exported.
  name: type
  type: string
- description: When the export completed.
  name: finished_at
  type: string
- description: The current state of the export.
  name: state
  type: string
- description: The URL to download the export file (when complete).
  name: result_url
  type: string
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-export-job-schema.json
slug: mailchimp-transactional-export-job
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: ExportJob
---
