---
description: A job candidate with personal details, resume information, and application data retrieved from Indeed.
layout: schema
name: Candidate
properties_list:
- description: A unique candidate identifier. For Indeed Apply applications, this corresponds to the apply_id, a unique 64-character identifier linking the employer, candidate, and job posting.
  name: id
  type: string
- description: The candidate's full name.
  name: name
  type: string
- description: The candidate's first name.
  name: firstName
  type: string
- description: The candidate's last name.
  name: lastName
  type: string
- description: The candidate's email address.
  name: email
  type: string
- description: The candidate's phone number.
  name: phoneNumber
  type: string
- description: The candidate's location as a freeform string.
  name: location
  type: string
- description: The candidate's cover letter text, if provided.
  name: coverLetter
  type: string
- description: The current status of the candidate's application. Must map to one of Indeed's predefined disposition categories.
  name: applicationStatus
  type: string
- description: Responses to screener questions configured on the job posting.
  name: screenerQuestionResponses
  type: array
- description: The timestamp when the candidate submitted the application.
  name: appliedAt
  type: string
- description: The source of the application, such as Indeed Apply, organic application, or other channels.
  name: source
  type: string
- description: The identifier of the job posting the candidate applied to.
  name: jobPostingId
  type: string
provider_name: Indeed
provider_slug: indeed
schema_file: json-schema/indeed-employer-candidate-schema.json
slug: indeed-employer-candidate
tags:
- Careers
- Employment
- Hiring
- Job Search
- Jobs
- Recruiting
title: Candidate
---
