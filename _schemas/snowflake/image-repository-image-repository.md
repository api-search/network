---
description: A Snowflake image repository.
layout: schema
name: ImageRepository
properties_list:
- description: Time the image repository was created.
  name: created_on
  type: string
- description: Current URL of the image repository.
  name: repository_url
  type: string
- description: Identifier for the current owner of the image repository.
  name: owner
  type: string
- description: Role type of the image repository owner.
  name: owner_role_type
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/image-repository-image-repository-schema.json
slug: image-repository-image-repository
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: ImageRepository
---
