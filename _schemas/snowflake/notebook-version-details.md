---
description: The version details of a file based entity
layout: schema
name: VersionDetails
properties_list:
- description: The last version name
  name: name
  type: string
- description: The default/last version alias of a file based entity.
  name: alias
  type: string
- description: The default/last version location.
  name: location_url
  type: string
- description: The default/last version source location.
  name: source_location_uri
  type: string
- description: The default/last version git commit#
  name: git_commit_hash
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/notebook-version-details-schema.json
slug: notebook-version-details
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: VersionDetails
---
