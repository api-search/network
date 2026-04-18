---
description: Represents a permission assignment granting a group access to a Dynatrace environment or account-level capability.
layout: schema
name: Permission
properties_list:
- description: The name of the permission, e.g., tenant-viewer, tenant-operator, tenant-admin, account-company-info.
  name: permissionName
  type: string
- description: The scope identifier the permission applies to. For environment permissions, this is the environment ID. For account permissions, this is the account UUID.
  name: scope
  type: string
- description: The type of scope. ACCOUNT for account-level permissions, TENANT for environment-level permissions.
  name: scopeType
  type: string
- description: The ID of the group this permission is assigned to.
  name: groupId
  type: string
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/dynatrace-account-management-permission-schema.json
slug: dynatrace-account-management-permission
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
title: Permission
---
