---
description: An employer entity on Indeed representing a company or organization that posts jobs and manages candidates.
layout: schema
name: Employer
properties_list:
- description: A globally unique employer identifier. For ATS partners, this typically combines the ATS system identifier with the employer's internal ID.
  name: id
  type: string
- description: The display name of the employer as it appears on Indeed job listings and company pages.
  name: employerName
  type: string
- description: The type of employer entity.
  name: employerType
  type: string
- description: The timestamp when the employer was created on Indeed.
  name: createdAt
  type: string
- description: The timestamp when the employer was last updated.
  name: updatedAt
  type: string
provider_name: Indeed
provider_slug: indeed
schema_file: json-schema/indeed-employer-employer-schema.json
slug: indeed-employer-employer
tags:
- Careers
- Employment
- Hiring
- Job Search
- Jobs
- Recruiting
title: Employer
---
