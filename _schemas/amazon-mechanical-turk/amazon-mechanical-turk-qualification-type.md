---
description: The QualificationType data structure represents a Qualification type, a description of a property of a Worker that must match the requirements of a HIT for the Worker to be able to accept the HIT. The type also describes how a Worker can obtain a Qualification of that type, such as through a Qualification test.
layout: schema
name: QualificationType
properties_list:
- description: ''
  name: QualificationTypeId
  type: object
- description: ''
  name: CreationTime
  type: object
- description: ''
  name: Name
  type: object
- description: ''
  name: Description
  type: object
- description: ''
  name: Keywords
  type: object
- description: ''
  name: QualificationTypeStatus
  type: object
- description: ''
  name: Test
  type: object
- description: ''
  name: TestDurationInSeconds
  type: object
- description: ''
  name: AnswerKey
  type: object
- description: ''
  name: RetryDelayInSeconds
  type: object
- description: ''
  name: IsRequestable
  type: object
- description: ''
  name: AutoGranted
  type: object
- description: ''
  name: AutoGrantedValue
  type: object
provider_name: Amazon Mechanical Turk
provider_slug: amazon-mechanical-turk
schema_file: json-schema/amazon-mechanical-turk-qualification-type-schema.json
slug: amazon-mechanical-turk-qualification-type
tags:
- AWS
- Crowdsourcing
- Human Intelligence
- Labor
- Machine Learning
- Tasks
title: QualificationType
---
