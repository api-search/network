---
aid: microsoft-azure:microsoft-azure-microsoftazureassessmentscreate
name: Microsoft Azure Create Or Update Assessment
tags:
- Subscriptions
humanURL: 
properties: []
description: >-
  Create a new assessment with the given name and the specified settings. Since name of an assessment in a project is a unique identifier, if an assessment with the name provided already exists, then the existing assessment is updated.<br><br>Any PUT operation, resulting in either create or update on an assessment, will cause the assessment to go in a "InProgress" state. This will be indicated by the field 'computationState' on the Assessment object. During this time no other PUT operation will...

---
