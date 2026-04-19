---
description: Request to disassociate source servers from an application
layout: schema
name: DisassociateSourceServersRequest
properties_list:
- description: Application ID
  name: applicationID
  type: string
- description: Source server IDs to disassociate
  name: sourceServerIDs
  type: array
- description: Account ID for cross-account access
  name: accountID
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-disassociate-source-servers-request-schema.json
slug: application-migration-service-disassociate-source-servers-request
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: DisassociateSourceServersRequest
---
