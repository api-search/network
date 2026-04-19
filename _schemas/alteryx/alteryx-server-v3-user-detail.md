---
description: Detailed representation of a user account
layout: schema
name: UserDetail
properties_list:
- description: Unique user identifier
  name: id
  type: string
- description: User's first name
  name: firstName
  type: string
- description: User's last name
  name: lastName
  type: string
- description: User's email address
  name: email
  type: string
- description: User role
  name: role
  type: string
- description: Date the user was created
  name: dateCreated
  type: string
- description: Default worker tag
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
- description: ''
  name: isAccountLocked
  type: boolean
- description: ''
  name: isActive
  type: boolean
- description: ''
  name: isValidated
  type: boolean
- description: ''
  name: timeZone
  type: string
- description: ''
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
schema_file: json-schema/alteryx-server-v3-user-detail-schema.json
slug: alteryx-server-v3-user-detail
tags:
- Analytics
- Automation
- Data Engineering
- Data Preparation
- Data Science
- ETL
- Machine Learning
- Predictive Analytics
title: UserDetail
---
