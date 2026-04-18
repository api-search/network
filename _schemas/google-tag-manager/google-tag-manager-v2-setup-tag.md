---
description: Represents a setup tag relationship. A setup tag fires before the main tag.
layout: schema
name: SetupTag
properties_list:
- description: The name of the setup tag.
  name: tagName
  type: string
- description: If true, fire the main tag only if the setup tag fires successfully. If false, fire the main tag regardless of setup tag firing status.
  name: stopOnSetupFailure
  type: boolean
provider_name: Google Tag Manager
provider_slug: google-tag-manager
schema_file: json-schema/google-tag-manager-v2-setup-tag-schema.json
slug: google-tag-manager-v2-setup-tag
tags:
- Analytics
- Conversion Tracking
- Marketing
- Tag Management
- Tracking
title: SetupTag
---
