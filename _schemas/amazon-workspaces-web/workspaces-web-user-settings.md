---
description: A user settings resource that can be associated with a web portal. Once associated with a web portal, user settings control how users can transfer data between a streaming session and the their local devices.
layout: schema
name: UserSettings
properties_list:
- description: ''
  name: associatedPortalArns
  type: object
- description: ''
  name: copyAllowed
  type: object
- description: ''
  name: disconnectTimeoutInMinutes
  type: object
- description: ''
  name: downloadAllowed
  type: object
- description: ''
  name: idleDisconnectTimeoutInMinutes
  type: object
- description: ''
  name: pasteAllowed
  type: object
- description: ''
  name: printAllowed
  type: object
- description: ''
  name: uploadAllowed
  type: object
- description: ''
  name: userSettingsArn
  type: object
provider_name: Amazon WorkSpaces Web
provider_slug: amazon-workspaces-web
schema_file: json-schema/workspaces-web-user-settings-schema.json
slug: workspaces-web-user-settings
tags:
- AWS
- End User Computing
- Secure Browser
- Virtual Desktop
- Zero Trust
title: UserSettings
---
