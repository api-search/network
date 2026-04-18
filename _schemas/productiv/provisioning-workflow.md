---
description: Represents a provisioning workflow configured for an application in the Productiv platform.
layout: schema
name: ProvisioningWorkflow
properties_list:
- description: The unique identifier of the workflow.
  name: workflowId
  type: string
- description: The name of the workflow.
  name: workflowName
  type: string
- description: The application associated with the workflow.
  name: applicationId
  type: string
- description: The status of the workflow.
  name: status
  type: string
provider_name: Productiv
provider_slug: productiv
schema_file: json-schema/provisioning-workflow.json
slug: provisioning-workflow
tags:
- Application Portfolio
- Provisioning
- SaaS Management
- Spend Management
- Usage Analytics
title: ProvisioningWorkflow
---
