---
description: Individual job posting element
layout: schema
name: JobPostingElement
properties_list:
- description: External identifier for the job posting
  name: externalJobPostingId
  type: string
- description: Job title
  name: title
  type: string
- description: Full job description
  name: description
  type: string
- description: Organization URN for the job posting
  name: integrationContext
  type: string
- description: Operation type for the job posting
  name: jobPostingOperationType
  type: string
- description: Type of job listing
  name: listingType
  type: string
- description: Timestamp when the job was listed
  name: listedAt
  type: integer
- description: Job location
  name: location
  type: string
- description: URL for company's application page
  name: companyApplyUrl
  type: string
- description: ''
  name: onsiteApplyConfiguration
  type: object
provider_name: LinkedIn
provider_slug: linkedin
schema_file: json-schema/linkedin-talent-job-posting-job-posting-element-schema.json
slug: linkedin-talent-job-posting-job-posting-element
tags:
- Business
- Careers
- Marketing
- Professional Networking
- Recruiting
- Social Media
title: JobPostingElement
---
