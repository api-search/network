---
description: An object containing user property operations. Each key is an operation type and the value is an object of property names to values.
layout: schema
name: UserPropertyOperations
properties_list:
- description: Set the value of a user property. If the property already exists, the value is overwritten.
  name: $set
  type: object
- description: Set the value of a user property only if it has not already been set. Useful for properties like initial_referrer.
  name: $setOnce
  type: object
- description: Increment a numeric user property by the specified value.
  name: $add
  type: object
- description: Append a value or values to a list user property.
  name: $append
  type: object
- description: Prepend a value or values to a list user property.
  name: $prepend
  type: object
- description: Remove a user property by setting its value to the string $unset.
  name: $unset
  type: object
- description: Remove a value from a list user property.
  name: $remove
  type: object
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/identify-api-user-property-operations-schema.json
slug: identify-api-user-property-operations
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: UserPropertyOperations
---
