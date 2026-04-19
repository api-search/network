---
description: Contract for creating a new user
layout: schema
name: CreateUserContract
properties_list:
- description: User's first name
  name: firstName
  type: string
- description: User's last name
  name: lastName
  type: string
- description: User's email address
  name: email
  type: string
- description: User role determining access level
  name: role
  type: string
- description: Default worker tag for the user
  name: defaultWorkerTag
  type: string
- description: Whether the user can create schedules
  name: canScheduleJobs
  type: boolean
- description: Whether the user can set job priority
  name: canPrioritizeJobs
  type: boolean
- description: Whether the user can assign jobs to workers
  name: canAssignJobs
  type: boolean
- description: Whether the user can create collections
  name: canCreateCollections
  type: boolean
- description: Whether API access is enabled for the user
  name: isApiEnabled
  type: boolean
- description: Default credential ID for the user
  name: defaultCredentialId
  type: string
- description: Whether the user account is active
  name: isActive
  type: boolean
- description: User's preferred time zone
  name: timeZone
  type: string
- description: Whether the user can create and update DCM connections
  name: canCreateAndUpdateDcm
  type: boolean
- description: Whether the user can share DCM connections for execution
  name: canShareForExecutionDcm
  type: boolean
- description: Whether the user can share DCM connections for collaboration
  name: canShareForCollaborationDcm
  type: boolean
- description: Whether the user can manage generic DCM vaults
  name: canManageGenericVaultsDcm
  type: boolean
provider_name: Alteryx
provider_slug: alteryx
schema_file: json-schema/alteryx-server-v3-create-user-contract-schema.json
slug: alteryx-server-v3-create-user-contract
tags:
- Analytics
- Automation
- Data Engineering
- Data Preparation
- Data Science
- ETL
- Machine Learning
- Predictive Analytics
title: CreateUserContract
---
