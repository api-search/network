---
description: A build is the compiled output of a library. When a library is built, all of its resources (extensions, rules, and data elements) are compiled into a deployable artifact that is assigned to an environment for delivery. Builds represent the actual JavaScript or configuration files served to end users.
layout: schema
name: Adobe Experience Platform Tags Build
properties_list:
- description: The unique identifier for the build.
  name: id
  type: string
- description: The resource type identifier.
  name: type
  type: string
- description: ''
  name: attributes
  type: object
- description: Related resources linked to this build.
  name: relationships
  type: object
- description: ''
  name: links
  type: object
provider_name: Adobe Launch
provider_slug: adobe-launch
schema_file: json-schema/build.json
slug: build
tags:
- Data Collection
- Edge Network
- Event Forwarding
- Marketing Technology
- Tag Management
title: Adobe Experience Platform Tags Build
---
