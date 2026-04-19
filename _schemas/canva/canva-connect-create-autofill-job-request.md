---
description: Request body for creating a design autofill job
layout: schema
name: CreateAutofillJobRequest
properties_list:
- description: The brand template ID to autofill
  name: brand_template_id
  type: string
- description: Title for the generated design (1-255 characters). Defaults to the brand template title.
  name: title
  type: string
- description: Data fields to populate, keyed by field name from the brand template dataset
  name: data
  type: object
provider_name: Canva
provider_slug: canva
schema_file: json-schema/canva-connect-create-autofill-job-request-schema.json
slug: canva-connect-create-autofill-job-request
tags:
- Apps
- Automation
- Brand Management
- Collaboration
- Design
- Graphics
- Marketing
- Print
- Templates
- Visual Content
title: CreateAutofillJobRequest
---
