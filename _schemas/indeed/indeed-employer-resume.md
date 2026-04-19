---
description: A candidate's resume in multiple formats. The file field contains the uploaded resume document, while text, html, and json fields provide parsed representations.
layout: schema
name: Resume
properties_list:
- description: Plain text representation of the resume content.
  name: text
  type: string
- description: HTML-formatted representation of the resume content.
  name: html
  type: string
- description: Structured JSON representation of the parsed resume, including sections for work experience, education, skills, and other fields.
  name: json
  type: object
provider_name: Indeed
provider_slug: indeed
schema_file: json-schema/indeed-employer-resume-schema.json
slug: indeed-employer-resume
tags:
- Careers
- Employment
- Hiring
- Job Search
- Jobs
- Recruiting
title: Resume
---
