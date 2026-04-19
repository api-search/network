---
description: Input for creating or updating an employer on Indeed.
layout: schema
name: PatchEmployerInput
properties_list:
- description: A globally unique employer identifier composed of the ATS identifier and the employer's ID within that system.
  name: id
  type: string
- description: The employer's display name. Required when creating a new employer, optional when updating an existing one.
  name: employerName
  type: string
provider_name: Indeed
provider_slug: indeed
schema_file: json-schema/indeed-employer-patch-employer-input-schema.json
slug: indeed-employer-patch-employer-input
tags:
- Careers
- Employment
- Hiring
- Job Search
- Jobs
- Recruiting
title: PatchEmployerInput
---
