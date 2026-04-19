---
description: An uploaded resume file.
layout: schema
name: ResumeFile
properties_list:
- description: The original filename of the uploaded resume.
  name: fileName
  type: string
- description: The MIME type of the resume file.
  name: contentType
  type: string
- description: The raw binary content of the resume file, Base64-encoded.
  name: data
  type: string
provider_name: Indeed
provider_slug: indeed
schema_file: json-schema/indeed-employer-resume-file-schema.json
slug: indeed-employer-resume-file
tags:
- Careers
- Employment
- Hiring
- Job Search
- Jobs
- Recruiting
title: ResumeFile
---
