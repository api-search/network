---
class_count: 16
classes:
- QuestionScore
- ParticipantList
- CreateSurveyRequest
- SurveyResponse
- CreateActionPlanRequest
- ResponseList
- Participant
- AddParticipantsResponse
- Survey
- AddParticipantsRequest
- SurveyList
- Answer
- SurveyAnalytics
- ActionPlan
- ActionPlanList
- description
context_file: json-ld/allianz-engagement-survey-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/allianz-engagement-survey/refs/heads/main/json-ld/allianz-engagement-survey-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Allianz Engagement Survey from Allianz Engagement Survey.
layout: jsonld
name: Allianz Engagement Survey Context
namespaces:
- prefix: allianz
  uri: https://api.allianz.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: questionId
  type: string
- container: ''
  name: question
  type: string
- container: ''
  name: score
  type: double
- container: ''
  name: favorable
  type: double
- container: ''
  name: total
  type: integer
- container: ''
  name: responded
  type: integer
- container: ''
  name: participationRate
  type: double
- container: set
  name: items
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: surveyType
  type: string
- container: ''
  name: startDate
  type: date
- container: ''
  name: endDate
  type: date
- container: ''
  name: responseId
  type: string
- container: ''
  name: surveyId
  type: string
- container: ''
  name: submittedAt
  type: dateTime
- container: set
  name: answers
  type: string
- container: ''
  name: ownerEmployeeId
  type: string
- container: ''
  name: dueDate
  type: date
- container: ''
  name: participantId
  type: string
- container: ''
  name: employeeId
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: invitedAt
  type: dateTime
- container: ''
  name: respondedAt
  type: dateTime
- container: ''
  name: added
  type: integer
- container: ''
  name: invitationSent
  type: boolean
- container: ''
  name: failed
  type: integer
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: modifiedAt
  type: dateTime
- container: set
  name: employeeIds
  type: string
- container: ''
  name: sendInvitation
  type: boolean
- container: ''
  name: offset
  type: integer
- container: ''
  name: limit
  type: integer
- container: ''
  name: textResponse
  type: string
- container: ''
  name: engagementScore
  type: double
- container: ''
  name: favorablePercentage
  type: double
- container: set
  name: questionScores
  type: string
- container: ''
  name: planId
  type: string
- container: ''
  name: owner
  type: string
property_count: 38
provider_name: Allianz Engagement Survey
provider_slug: allianz-engagement-survey
slug: allianz-engagement-survey-context
tags:
- Analytics
- Enterprise
- Human Resources
- Insurance
- Surveys
- Employee Experience
- JSON-LD
- Linked Data
- Semantic Web
---
