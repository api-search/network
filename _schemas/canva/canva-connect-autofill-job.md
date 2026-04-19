---
description: An autofill job for generating designs from brand templates
layout: schema
name: AutofillJob
properties_list:
- description: The autofill job ID
  name: id
  type: string
- description: The current status of the autofill job
  name: status
  type: string
- description: The autofill result (present when status is success)
  name: result
  type: object
- description: Error details (present when status is failed)
  name: error
  type: object
provider_name: Canva
provider_slug: canva
schema_file: json-schema/canva-connect-autofill-job-schema.json
slug: canva-connect-autofill-job
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
title: AutofillJob
---
