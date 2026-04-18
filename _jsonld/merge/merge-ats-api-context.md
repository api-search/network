---
class_count: 11
classes:
- Candidate
- Application
- Job
- Offer
- ScheduledInterview
- JobInterviewStage
- Scorecard
- Department
- Office
- Activity
- RemoteUser
context_file: json-ld/merge-ats-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/merge/refs/heads/main/json-ld/merge-ats-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Merge Ats Api from Merge.
layout: jsonld
name: Merge Ats Api Context
namespaces:
- prefix: merge
  uri: https://api.merge.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: string
- container: ''
  name: remoteId
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: company
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: isPrivate
  type: boolean
- container: ''
  name: canEmail
  type: boolean
- container: set
  name: emailAddresses
  type: ''
- container: set
  name: phoneNumbers
  type: ''
- container: set
  name: tags
  type: string
- container: set
  name: applications
  type: reference
- container: ''
  name: candidate
  type: reference
- container: ''
  name: job
  type: reference
- container: ''
  name: appliedAt
  type: dateTime
- container: ''
  name: rejectedAt
  type: dateTime
- container: ''
  name: source
  type: string
- container: ''
  name: currentStage
  type: reference
- container: ''
  name: name
  type: string
- container: ''
  name: status
  type: string
- container: set
  name: departments
  type: reference
- container: set
  name: offices
  type: reference
- container: set
  name: hiringManagers
  type: reference
- container: set
  name: recruiters
  type: reference
- container: ''
  name: overallRecommendation
  type: string
- container: ''
  name: activityType
  type: string
- container: ''
  name: subject
  type: string
- container: ''
  name: body
  type: string
- container: ''
  name: email
  type: string
- container: ''
  name: accessRole
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: modifiedAt
  type: dateTime
- container: ''
  name: remoteWasDeleted
  type: boolean
property_count: 33
provider_name: Merge
provider_slug: merge
slug: merge-ats-api-context
tags:
- Integrations
- Platform
- Unified API
- JSON-LD
- Linked Data
- Semantic Web
---
