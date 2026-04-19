---
description: A Snowflake notebook
layout: schema
name: Notebook
properties_list:
- description: Name of the notebook
  name: name
  type: string
- description: User specified version alias
  name: version
  type: string
- description: Location to copy the file from. This must be a Snowflake stage location.
  name: fromLocation
  type: string
- description: Name + path of the file for the Notebook
  name: main_file
  type: string
- description: user comment associated to an object in the dictionary
  name: comment
  type: string
- description: The default version name of a file based entity.
  name: default_version
  type: string
- description: Warehouse against which the queries issued by the Streamlit app are run against
  name: query_warehouse
  type: string
- description: Date and time when the notebook was created.
  name: created_on
  type: string
- description: Database in which the notebook is stored
  name: database_name
  type: string
- description: Schema in which the notebook is stored
  name: schema_name
  type: string
- description: Role that owns the notebook
  name: owner
  type: string
- description: The type of role that owns the notebook
  name: owner_role_type
  type: string
- description: Unique ID associated with the notebook object.
  name: url_id
  type: string
- description: User facing title of the Streamlit app or an Organization Profile
  name: title
  type: string
- description: Default packages of the notebook
  name: default_packages
  type: string
- description: User packages of the notebook
  name: user_packages
  type: string
- description: The runtime to run the Streamlit or Notebook on. If this is not set, the warehouse is assumed
  name: runtime_name
  type: string
- description: Compute pool name where the snowservice runs
  name: compute_pool
  type: string
- description: List of urls
  name: import_urls
  type: array
- description: List of external access integrations attached to this function
  name: external_access_integrations
  type: array
- description: Secrets to be used with this function for external access
  name: external_access_secrets
  type: string
- description: Sets the time in seconds for when to shutdown an idle Notebook.
  name: idle_auto_shutdown_time_seconds
  type: integer
- description: The current version location
  name: live_version_location_uri
  type: string
- description: Name of the budget if the notebook is monitored by a budget
  name: budget
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/notebook-notebook-schema.json
slug: notebook-notebook
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Notebook
---
