---
description: A candidate object from the Indeed Employer API, representing a job applicant who has applied to a position through Indeed or Indeed Apply. Contains personal details, resume, application status, and responses to screener and EEO questions.
layout: schema
name: Indeed Candidate
properties_list:
- description: A unique candidate application identifier. For Indeed Apply applications, this is a 64-character string (apply_id) that uniquely connects the employer, candidate, and job posting.
  name: id
  type: string
- description: The candidate's full name as provided in their application.
  name: name
  type: string
- description: The candidate's first (given) name.
  name: firstName
  type: string
- description: The candidate's last (family) name.
  name: lastName
  type: string
- description: The candidate's email address.
  name: email
  type: string
- description: The candidate's phone number, typically in E.164 or national format.
  name: phoneNumber
  type: string
- description: The candidate's location as a freeform text string, such as city and state.
  name: location
  type: string
- description: The candidate's resume in multiple formats. Not all formats are always available; use a robust parser that treats missing fields as empty.
  name: resume
  type: object
- description: The candidate's cover letter text, if provided with the application.
  name: coverLetter
  type: string
- description: The current disposition status of the candidate's application within the hiring pipeline. Must map to one of Indeed's six predefined categories.
  name: applicationStatus
  type: string
- description: The candidate's responses to screener questions configured on the job posting.
  name: screenerQuestionResponses
  type: array
- description: Equal Employment Opportunity (EEO) compliance responses provided by the candidate. Only available for US employers that have EEO questions enabled on their job postings.
  name: eeoResponses
  type: object
- description: The ISO 8601 timestamp when the candidate submitted their application.
  name: appliedAt
  type: string
- description: The channel through which the candidate submitted their application, such as indeed_apply, organic, or other integration sources.
  name: source
  type: string
- description: The unique identifier of the job posting the candidate applied to.
  name: jobPostingId
  type: string
- description: The title of the job posting the candidate applied to.
  name: jobTitle
  type: string
- description: The unique identifier of the employer who posted the job.
  name: employerId
  type: string
- description: Whether this candidate application has been acknowledged by the ATS. Unacknowledged applications are returned first in Retrieve Candidates API queries.
  name: acknowledged
  type: boolean
- description: The ISO 8601 timestamp when the candidate record was last updated.
  name: updatedAt
  type: string
provider_name: Indeed
provider_slug: indeed
schema_file: json-schema/indeed-candidate-schema.json
slug: indeed-candidate
tags:
- Careers
- Employment
- Hiring
- Job Search
- Jobs
- Recruiting
title: Indeed Candidate
---
