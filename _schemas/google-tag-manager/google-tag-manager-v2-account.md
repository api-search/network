---
description: Represents a Google Tag Manager Account.
layout: schema
name: Account
properties_list:
- description: GTM Account's API relative path.
  name: path
  type: string
- description: The Account ID uniquely identifies the GTM Account.
  name: accountId
  type: string
- description: Account display name.
  name: name
  type: string
- description: Whether the account shares data anonymously with Google and others. This flag enables benchmarking by sharing your data in an anonymous form.
  name: shareData
  type: boolean
- description: The fingerprint of the GTM Account as computed at storage time. This value is recomputed whenever the account is modified.
  name: fingerprint
  type: string
- description: Auto-generated link to the tag manager UI.
  name: tagManagerUrl
  type: string
provider_name: Google Tag Manager
provider_slug: google-tag-manager
schema_file: json-schema/google-tag-manager-v2-account-schema.json
slug: google-tag-manager-v2-account
tags:
- Analytics
- Conversion Tracking
- Marketing
- Tag Management
- Tracking
title: Account
---
