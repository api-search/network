---
description: Represents an asynchronous PDF processing job in the Adobe PDF Services API. A job is created when an operation is submitted (such as creating, converting, extracting, or manipulating a PDF). The job is processed asynchronously and its status can be polled until completion. Upon completion, the job provides an output asset with a download URI.
layout: schema
name: Adobe PDF Services Job
properties_list:
- description: The current processing status of the job. A job starts as 'in progress' when submitted and transitions to 'done' upon successful completion or 'failed' if an error occurs.
  name: status
  type: string
- description: The output asset produced by the job. Available when status is 'done'.
  name: asset
  type: object
- description: Error details when the job has failed. Available when status is 'failed'.
  name: error
  type: object
provider_name: Adobe
provider_slug: adobe
schema_file: json-schema/adobe-pdf-job-schema.json
slug: adobe-pdf-job
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
title: Adobe PDF Services Job
---
