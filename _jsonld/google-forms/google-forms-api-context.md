---
class_count: 5
classes:
- Form
- FormResponse
- Watch
- Question
- Item
context_file: json-ld/google-forms-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/google-forms/refs/heads/main/json-ld/google-forms-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Google Forms Api from Google Forms.
layout: jsonld
name: Google Forms Api Context
namespaces:
- prefix: gforms
  uri: https://developers.google.com/forms/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: formId
  type: string
- container: ''
  name: responseId
  type: string
- container: ''
  name: questionId
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: createTime
  type: dateTime
- container: ''
  name: lastSubmittedTime
  type: dateTime
- container: ''
  name: expireTime
  type: dateTime
- container: ''
  name: respondentEmail
  type: string
- container: ''
  name: revisionId
  type: string
- container: ''
  name: responderUri
  type: reference
- container: ''
  name: linkedSheetId
  type: string
- container: ''
  name: totalScore
  type: decimal
- container: ''
  name: eventType
  type: string
- container: ''
  name: state
  type: string
- container: set
  name: items
  type: reference
- container: ''
  name: answers
  type: reference
property_count: 17
provider_name: Google Forms
provider_slug: google-forms
slug: google-forms-api-context
tags:
- Data Collection
- Forms
- Google
- Google Workspace
- Questionnaires
- Responses
- Surveys
- JSON-LD
- Linked Data
- Semantic Web
---
