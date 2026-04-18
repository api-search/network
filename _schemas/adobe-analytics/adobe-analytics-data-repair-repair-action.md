---
description: The action to take on a specific variable
layout: schema
name: RepairAction
properties_list:
- description: The repair action to perform
  name: action
  type: string
- description: The value to set the variable to (required when action is 'set')
  name: setValue
  type: string
- description: Optional filter to limit which rows are affected by the repair
  name: filter
  type: object
provider_name: Adobe Analytics
provider_slug: adobe-analytics
schema_file: json-schema/adobe-analytics-data-repair-repair-action-schema.json
slug: adobe-analytics-data-repair-repair-action
tags:
- Adobe
- Analytics
- Business Intelligence
- Customer Intelligence
- Digital Marketing
- Marketing
- Web Analytics
title: RepairAction
---
