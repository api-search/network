---
description: Represents a predicate that is evaluated against a data layer value or variable. Used in trigger filter conditions.
layout: schema
name: Condition
properties_list:
- description: The type of operator for this condition.
  name: type
  type: string
- description: A list of named parameters (key/value), depending on the condition's type. The first parameter is the left-hand operand, the second is the right-hand operand.
  name: parameter
  type: array
provider_name: Google Tag Manager
provider_slug: google-tag-manager
schema_file: json-schema/google-tag-manager-v2-condition-schema.json
slug: google-tag-manager-v2-condition
tags:
- Analytics
- Conversion Tracking
- Marketing
- Tag Management
- Tracking
title: Condition
---
