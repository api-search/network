---
description: Registration of an employer for Candidate Sync integration, enabling candidate data synchronization between the ATS and Indeed.
layout: schema
name: EmployerRegistration
properties_list:
- description: The employer's unique identifier.
  name: employerId
  type: string
- description: The current registration status.
  name: registrationStatus
  type: string
- description: Enabled Candidate Sync features for this employer.
  name: features
  type: array
- description: When the employer was registered for Candidate Sync.
  name: registeredAt
  type: string
provider_name: Indeed
provider_slug: indeed
schema_file: json-schema/indeed-employer-employer-registration-schema.json
slug: indeed-employer-employer-registration
tags:
- Careers
- Employment
- Hiring
- Job Search
- Jobs
- Recruiting
title: EmployerRegistration
---
