---
description: A file on a snowflake stage.
layout: schema
name: StageFile
properties_list:
- description: Name of the file.
  name: name
  type: string
- description: Size of the file.
  name: size
  type: string
- description: md5 hash of the file.
  name: md5
  type: string
- description: Date and time when the file was last modified.
  name: last_modified
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/stage-stage-file-schema.json
slug: stage-stage-file
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: StageFile
---
