---
description: Contains information about the phone configuration settings for a user.
layout: schema
name: UserPhoneConfig
properties_list:
- description: The phone type.
  name: PhoneType
  type: string
- description: The Auto accept setting.
  name: AutoAccept
  type: boolean
- description: The After Contact Work (ACW) timeout setting, in seconds.
  name: AfterContactWorkTimeLimit
  type: integer
- description: The phone number for the user's desk phone.
  name: DeskPhoneNumber
  type: string
provider_name: Amazon Connect
provider_slug: amazon-connect
schema_file: json-schema/user-phone-config-schema.json
slug: user-phone-config
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
title: UserPhoneConfig
---
