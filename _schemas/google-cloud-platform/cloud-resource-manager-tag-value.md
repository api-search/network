---
description: A tag value, which is a child of a tag key. Tag values are the specific labels that can be attached to resources through tag bindings.
layout: schema
name: TagValue
properties_list:
- description: The resource name of the tag value in the form tagValues/{tag_value_id}. Output only.
  name: name
  type: string
- description: The resource name of the parent tag key.
  name: parent
  type: string
- description: The user-friendly short name for the tag value. Unique for a given tag key. Maximum length of 256 characters.
  name: shortName
  type: string
- description: The namespaced name of the tag value in the form {parentNamespace}/{shortName}. Output only.
  name: namespacedName
  type: string
- description: User-assigned description of the tag value. Maximum length of 256 characters.
  name: description
  type: string
- description: Timestamp when the tag value was created. Output only.
  name: createTime
  type: string
- description: Timestamp when the tag value was last modified. Output only.
  name: updateTime
  type: string
- description: Entity tag for optimistic concurrency control.
  name: etag
  type: string
provider_name: Google Cloud Platform
provider_slug: google-cloud-platform
schema_file: json-schema/cloud-resource-manager-tag-value-schema.json
slug: cloud-resource-manager-tag-value
tags:
- API Management
- Cloud Computing
- Infrastructure
- Platform as a Service
title: TagValue
---
