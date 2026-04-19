---
description: ConfigurationTag schema from Amazon Application Discovery Service API
layout: schema
name: ConfigurationTag
properties_list:
- description: A type of IT asset to tag.
  name: configurationType
  type: string
- description: The configuration ID for the item to tag.
  name: configurationId
  type: string
- description: A type of tag on which to filter.
  name: key
  type: string
- description: A value on which to filter.
  name: value
  type: string
- description: The time the configuration tag was created in Coordinated Universal Time (UTC).
  name: timeOfCreation
  type: string
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-configuration-tag-schema.json
slug: application-discovery-service-configuration-tag
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: ConfigurationTag
---
