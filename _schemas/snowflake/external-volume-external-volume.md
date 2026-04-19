---
description: A Snowflake external volume
layout: schema
name: ExternalVolume
properties_list:
- description: String that specifies the identifier (the name) for the external volume; must be unique in your account.
  name: name
  type: string
- description: Set of named cloud storage locations in different regions and, optionally, cloud platforms.
  name: storage_locations
  type: array
- description: Specifies whether write operations are allowed for the external volume; must be set to TRUE for Iceberg tables that use Snowflake as the catalog.
  name: allow_writes
  type: boolean
- description: String (literal) that specifies a comment for the external volume.
  name: comment
  type: string
- description: Date and time when the external volume was created.
  name: created_on
  type: string
- description: Role that owns the external volume
  name: owner
  type: string
- description: The type of role that owns the external volume
  name: owner_role_type
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/external-volume-external-volume-schema.json
slug: external-volume-external-volume
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: ExternalVolume
---
