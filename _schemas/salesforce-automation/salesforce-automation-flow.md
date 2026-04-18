---
description: A Salesforce Flow definition representing an automation built with Flow Builder. Flows are the primary declarative automation tool in Salesforce, replacing Workflow Rules and Process Builder. They support screen flows (user-interactive), autolaunched flows (triggered automatically), scheduled flows, record-triggered flows, and platform event-triggered flows. This schema models the Flow metadata as returned by the Tooling API and Metadata API.
layout: schema
name: Salesforce Automation Flow
properties_list:
- description: The 18-character Salesforce record ID for this specific Flow version. Each version of a Flow has a unique ID.
  name: Id
  type: string
- description: The 18-character ID of the parent FlowDefinition record. All versions of the same flow share this DefinitionId.
  name: DefinitionId
  type: string
- description: The unique developer name (API name) for this flow. Used as the identifier in metadata deployments and API references. Cannot contain spaces or special characters.
  name: DeveloperName
  type: string
- description: The display label shown in the Flow Builder UI and flow list views.
  name: MasterLabel
  type: string
- description: An optional description of the flow's purpose and behavior.
  name: Description
  type:
  - string
  - 'null'
- description: The type of flow, which determines how and when it executes. AutoLaunchedFlow runs without user interaction (triggered by records, schedules, or invocable actions). Flow is a Screen Flow that presents
  name: ProcessType
  type: string
- description: For record-triggered flows, specifies when the flow runs relative to the DML operation.
  name: TriggerType
  type:
  - string
  - 'null'
- description: For record-triggered flows, the API name of the SObject that triggers the flow (e.g., Account, Contact, Opportunity, CustomObject__c).
  name: TriggerObject
  type:
  - string
  - 'null'
- description: For record-triggered flows, specifies which record operations trigger the flow.
  name: RecordTriggerType
  type:
  - string
  - 'null'
- description: The status of this flow version. Active means this version is the currently running version. Draft is a version under development. Obsolete is a previously active version that has been superseded. Inv
  name: Status
  type: string
- description: The version number within the FlowDefinition. Increments with each new version. The active version number is stored on the FlowDefinition record.
  name: VersionNumber
  type: integer
- description: The Salesforce API version this flow was created with (e.g., 63.0). Determines which flow features are available.
  name: ApiVersion
  type: string
- description: The context in which the flow runs. SystemModeWithSharing runs with full object/field access but respects sharing rules. SystemModeWithoutSharing runs with full access and no sharing restrictions. Def
  name: RunInMode
  type:
  - string
  - 'null'
- description: The full flow metadata containing all elements, connectors, variables, and configuration. This is the complete definition of the flow's logic.
  name: Metadata
  type: object
- description: The fully qualified name including namespace prefix if applicable (e.g., MyNamespace__MyFlow-1)
  name: FullName
  type: string
- description: Whether this flow is a template that can be used to create new flows
  name: IsTemplate
  type: boolean
- description: Whether this flow can be overridden by a flow in a subscriber org
  name: IsOverridable
  type: boolean
- description: The date and time this flow version was created, in ISO 8601 format
  name: CreatedDate
  type: string
- description: The 18-character ID of the user who created this flow version
  name: CreatedById
  type: string
- description: The date and time this flow version was last modified
  name: LastModifiedDate
  type: string
- description: The 18-character ID of the user who last modified this flow version
  name: LastModifiedById
  type: string
provider_name: Salesforce Automation
provider_slug: salesforce-automation
schema_file: json-schema/salesforce-automation-flow-schema.json
slug: salesforce-automation-flow
tags:
- Automation
- Cloud
- CRM
- Enterprise
- Sales
title: Salesforce Automation Flow
---
