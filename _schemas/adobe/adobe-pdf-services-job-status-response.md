---
description: The status and result of an asynchronous PDF operation job.
layout: schema
name: JobStatusResponse
properties_list:
- description: The current status of the job.
  name: status
  type: string
- description: The output asset information, available when status is done.
  name: asset
  type: object
- description: Error information, available when status is failed.
  name: error
  type: object
provider_name: Adobe
provider_slug: adobe
schema_file: json-schema/adobe-pdf-services-job-status-response-schema.json
slug: adobe-pdf-services-job-status-response
tags:
- Analytics
- Creative Cloud
- Digital Asset Management
- Document Services
- E-Commerce
- E-Signatures
- Experience Cloud
- Generative AI
- Marketing
- PDF
- Work Management
title: JobStatusResponse
---
