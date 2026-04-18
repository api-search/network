---
description: Represents the progress of a hook invocation.
layout: schema
name: HookProgressEvent
properties_list:
- description: The type name of the hook.
  name: HookTypeName
  type: string
- description: The version of the hook type.
  name: HookTypeVersionId
  type: string
- description: The ARN of the hook type.
  name: HookTypeArn
  type: string
- description: The point in the provisioning workflow where the hook runs.
  name: InvocationPoint
  type: string
- description: The status of the hook invocation.
  name: HookStatus
  type: string
- description: The time the hook event occurred.
  name: HookEventTime
  type: number
- description: A message about the hook status.
  name: HookStatusMessage
  type: string
- description: How the hook failure should affect the overall operation.
  name: FailureMode
  type: string
provider_name: AWS CloudFormation
provider_slug: cloudformation
schema_file: json-schema/cloud-control-hook-progress-event-schema.json
slug: cloud-control-hook-progress-event
tags:
- Automation
- AWS
- Cloud Resources
- IaC
- Infrastructure As Code
- Stack Management
title: HookProgressEvent
---
