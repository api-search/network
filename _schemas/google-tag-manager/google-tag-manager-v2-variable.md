---
description: Represents a Google Tag Manager Variable. A variable provides dynamic values that can be used in tags and triggers, such as page URL, click text, or custom JavaScript values.
layout: schema
name: Variable
properties_list:
- description: GTM Variable's API relative path.
  name: path
  type: string
- description: GTM Account ID.
  name: accountId
  type: string
- description: GTM Container ID.
  name: containerId
  type: string
- description: GTM Workspace ID.
  name: workspaceId
  type: string
- description: The Variable ID uniquely identifies the GTM Variable.
  name: variableId
  type: string
- description: Variable display name.
  name: name
  type: string
- description: GTM Variable Type. Common types include v (Data Layer Variable), j (1st Party Cookie), k (Custom JavaScript), jsm (Custom JavaScript Variable), u (URL), c (Constant), and e (DOM Element).
  name: type
  type: string
- description: User notes on how to apply this variable in the container.
  name: notes
  type: string
- description: The start timestamp in milliseconds to schedule a variable.
  name: scheduleStartMs
  type: string
- description: The end timestamp in milliseconds to schedule a variable.
  name: scheduleEndMs
  type: string
- description: The variable's parameters, which configure its behavior.
  name: parameter
  type: array
- description: For mobile containers only. A list of trigger IDs for enabling conditional variables. The variable is enabled if one of the enabling triggers is true while all of the disabling triggers are false.
  name: enablingTriggerId
  type: array
- description: For mobile containers only. A list of trigger IDs for disabling conditional variables.
  name: disablingTriggerId
  type: array
- description: The fingerprint of the GTM Variable as computed at storage time. This value is recomputed whenever the variable is modified.
  name: fingerprint
  type: string
- description: Parent folder ID.
  name: parentFolderId
  type: string
- description: Auto-generated link to the tag manager UI.
  name: tagManagerUrl
  type: string
provider_name: Google Tag Manager
provider_slug: google-tag-manager
schema_file: json-schema/google-tag-manager-v2-variable-schema.json
slug: google-tag-manager-v2-variable
tags:
- Analytics
- Conversion Tracking
- Marketing
- Tag Management
- Tracking
title: Variable
---
