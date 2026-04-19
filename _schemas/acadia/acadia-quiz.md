---
description: A quiz or assessment
layout: schema
name: Quiz
properties_list:
- description: Quiz identifier
  name: id
  type: string
- description: Quiz title
  name: title
  type: string
- description: Quiz status
  name: status
  type: string
- description: Number of questions in the quiz
  name: questionCount
  type: integer
- description: Minimum passing score percentage
  name: passingScore
  type: integer
- description: Quiz creation timestamp
  name: createdAt
  type: string
provider_name: Acadia
provider_slug: acadia
schema_file: json-schema/acadia-quiz-schema.json
slug: acadia-quiz
tags:
- Connected Worker
- Knowledge Management
- Manufacturing
- Skills Management
- Training
- Workforce Development
title: Quiz
---
