---
description: Represents a Google Tag Manager Parameter. Parameters are key-value pairs that configure tags, triggers, and variables.
layout: schema
name: Parameter
properties_list:
- description: The parameter type.
  name: type
  type: string
- description: The named key that uniquely identifies a parameter. Required for top-level parameters, as well as map values. Ignored for list values.
  name: key
  type: string
- description: A parameter's value (may contain variable references) as appropriate to the specified type.
  name: value
  type: string
- description: This list parameter's parameters (keys will be ignored). Used when type is list.
  name: list
  type: array
- description: This map parameter's parameters (must have keys; keys must be unique). Used when type is map.
  name: map
  type: array
- description: Whether or not the parameter is a weak reference. Used to determine which parameters should be included in exported containers.
  name: isWeakReference
  type: boolean
provider_name: Google Tag Manager
provider_slug: google-tag-manager
schema_file: json-schema/google-tag-manager-v2-parameter-schema.json
slug: google-tag-manager-v2-parameter
tags:
- Analytics
- Conversion Tracking
- Marketing
- Tag Management
- Tracking
title: Parameter
---
