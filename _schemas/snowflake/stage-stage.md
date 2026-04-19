---
description: A Snowflake stage.
layout: schema
name: Stage
properties_list:
- description: Specifies whether the stage is permanent or temporary.
  name: kind
  type: string
- description: URL for the external stage; blank for an internal stage.
  name: url
  type: string
- description: The S3-compatible API endpoint associated with the stage; always NULL for stages that are not S3-compatible.
  name: endpoint
  type: string
- description: Specifies a comment for the stage.
  name: comment
  type: string
- description: Encryption parameters of the stage.
  name: encryption
  type: object
- description: Directory table parameters of the stage.
  name: directory_table
  type: object
- description: Date and time when the stage was created.
  name: created_on
  type: string
- description: Indicates that the external stage has access credentials; always false for an internal stage.
  name: has_credentials
  type: boolean
- description: Indicates that the external stage contains encrypted files; always false for an internal stage.
  name: has_encryption_key
  type: boolean
- description: Role that owns the stage.
  name: owner
  type: string
- description: The type of role that owns the object, either ROLE or DATABASE_ROLE. If a Snowflake Native App owns the object, the value is APPLICATION. Snowflake returns NULL if you delete the object because a dele
  name: owner_role_type
  type: string
- description: Region where the stage is located.
  name: region
  type: string
- description: Cloud provider; always NULL for an internal stage.
  name: cloud
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/stage-stage-schema.json
slug: stage-stage
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Stage
---
