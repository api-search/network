---
description: A image in a Snowflake image repository.
layout: schema
name: Image
properties_list:
- description: Date and time when the image was uploaded to the image repository.
  name: created_on
  type: string
- description: Image name.
  name: image_name
  type: string
- description: Image tags.
  name: tags
  type: string
- description: SHA256 digest of the image.
  name: digest
  type: string
- description: Image path (database_name/schema_name/repository_name/image_name:image_tag).
  name: image_path
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/image-repository-image-schema.json
slug: image-repository-image
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Image
---
