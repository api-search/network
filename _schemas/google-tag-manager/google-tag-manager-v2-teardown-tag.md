---
description: Represents a teardown tag relationship. A teardown tag fires after the main tag.
layout: schema
name: TeardownTag
properties_list:
- description: The name of the teardown tag.
  name: tagName
  type: string
- description: If true, fire the teardown tag if and only if the main tag fires successfully. If false, fire the teardown tag regardless of main tag firing status.
  name: stopTeardownOnFailure
  type: boolean
provider_name: Google Tag Manager
provider_slug: google-tag-manager
schema_file: json-schema/google-tag-manager-v2-teardown-tag-schema.json
slug: google-tag-manager-v2-teardown-tag
tags:
- Analytics
- Conversion Tracking
- Marketing
- Tag Management
- Tracking
title: TeardownTag
---
