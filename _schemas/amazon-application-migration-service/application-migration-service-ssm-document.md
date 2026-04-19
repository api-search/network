---
description: An SSM document configuration for post-launch automation
layout: schema
name: SsmDocument
properties_list:
- description: Name of the SSM action
  name: actionName
  type: string
- description: SSM document name
  name: ssmDocumentName
  type: string
- description: Timeout in seconds
  name: timeoutSeconds
  type: integer
- description: Whether this action must succeed for cutover to proceed
  name: mustSucceedForCutover
  type: boolean
- description: SSM document parameters
  name: parameters
  type: object
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-ssm-document-schema.json
slug: application-migration-service-ssm-document
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: SsmDocument
---
