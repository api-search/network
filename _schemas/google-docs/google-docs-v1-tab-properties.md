---
description: Properties of a tab.
layout: schema
name: TabProperties
properties_list:
- description: Output only. The ID of the tab.
  name: tabId
  type: string
- description: The title of the tab.
  name: title
  type: string
- description: Output only. The ID of the parent tab. Empty if this is a root-level tab.
  name: parentTabId
  type: string
- description: The zero-based index of the tab amongst its siblings.
  name: index
  type: integer
provider_name: Google Docs
provider_slug: google-docs
schema_file: json-schema/google-docs-v1-tab-properties-schema.json
slug: google-docs-v1-tab-properties
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
title: TabProperties
---
