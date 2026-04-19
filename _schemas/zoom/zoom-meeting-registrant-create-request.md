---
description: ''
layout: schema
name: RegistrantCreateRequest
properties_list:
- description: Registrant email address.
  name: email
  type: string
- description: Registrant first name.
  name: first_name
  type: string
- description: Registrant last name.
  name: last_name
  type: string
- description: Registrant address.
  name: address
  type: string
- description: Registrant city.
  name: city
  type: string
- description: Registrant state or province.
  name: state
  type: string
- description: Registrant zip or postal code.
  name: zip
  type: string
- description: Registrant two-letter country code.
  name: country
  type: string
- description: Registrant phone number.
  name: phone
  type: string
- description: Registrant questions and comments.
  name: comments
  type: string
- description: Registrant industry.
  name: industry
  type: string
- description: Registrant job title.
  name: job_title
  type: string
- description: Registrant organization.
  name: org
  type: string
- description: Number of employees.
  name: no_of_employees
  type: string
- description: Purchasing time frame.
  name: purchasing_time_frame
  type: string
- description: Role in purchase process.
  name: role_in_purchase_process
  type: string
- description: Registrant language preference.
  name: language
  type: string
- description: Custom question responses.
  name: custom_questions
  type: array
- description: Auto-approve this registrant.
  name: auto_approve
  type: boolean
provider_name: Zoom
provider_slug: zoom
schema_file: json-schema/zoom-meeting-registrant-create-request-schema.json
slug: zoom-meeting-registrant-create-request
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
title: RegistrantCreateRequest
---
