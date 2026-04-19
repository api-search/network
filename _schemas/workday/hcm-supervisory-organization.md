---
description: ''
layout: schema
name: SupervisoryOrganization
properties_list:
- description: The Workday ID of the organization.
  name: id
  type: string
- description: A display descriptor for the organization.
  name: descriptor
  type: string
- description: The name of the supervisory organization.
  name: name
  type: string
- description: The organization reference ID.
  name: code
  type: string
- description: Whether the organization is inactive.
  name: isInactive
  type: boolean
- description: The staffing model for the organization.
  name: staffingModel
  type: string
provider_name: Workday
provider_slug: workday
schema_file: json-schema/hcm-supervisory-organization-schema.json
slug: hcm-supervisory-organization
tags:
- Cloud Computing
- Enterprise Software
- Financial Management
- HCM
- SaaS
title: SupervisoryOrganization
---
