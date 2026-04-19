---
description: Contract for updating an existing user
layout: schema
name: UpdateUserContract
properties_list:
- description: User ID (optional, for verification)
  name: id
  type: string
- description: ''
  name: firstName
  type: string
- description: ''
  name: lastName
  type: string
- description: ''
  name: email
  type: string
- description: ''
  name: role
  type: string
- description: ''
  name: defaultWorkerTag
  type: string
- description: ''
  name: canScheduleJobs
  type: boolean
- description: ''
  name: canPrioritizeJobs
  type: boolean
- description: ''
  name: canAssignJobs
  type: boolean
- description: ''
  name: canCreateCollections
  type: boolean
- description: ''
  name: isApiEnabled
  type: boolean
- description: ''
  name: defaultCredentialId
  type: string
- description: Whether the account is locked
  name: isAccountLocked
  type: boolean
- description: ''
  name: isActive
  type: boolean
- description: Whether the user's email has been validated
  name: isValidated
  type: boolean
- description: ''
  name: timeZone
  type: string
- description: User's preferred language
  name: language
  type: string
- description: ''
  name: canCreateAndUpdateDcm
  type: boolean
- description: ''
  name: canShareForExecutionDcm
  type: boolean
- description: ''
  name: canShareForCollaborationDcm
  type: boolean
- description: ''
  name: canManageGenericVaultsDcm
  type: boolean
provider_name: Alteryx
provider_slug: alteryx
schema_file: json-schema/alteryx-server-v3-update-user-contract-schema.json
slug: alteryx-server-v3-update-user-contract
tags:
- Analytics
- Automation
- Data Engineering
- Data Preparation
- Data Science
- ETL
- Machine Learning
- Predictive Analytics
title: UpdateUserContract
---
