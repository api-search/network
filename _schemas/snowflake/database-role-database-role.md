---
description: A Snowflake database role
layout: schema
name: DatabaseRole
properties_list:
- description: Name of the database role
  name: name
  type: string
- description: User comment associated to an object in the dictionary
  name: comment
  type: string
- description: Date and time when the database role was created
  name: created_on
  type: string
- description: How many roles this database role has been granted to
  name: granted_to_roles
  type: integer
- description: How many database roles this database role has been granted to
  name: granted_to_database_roles
  type: integer
- description: How many database roles this database role has been granted
  name: granted_database_roles
  type: integer
- description: Role that owns the database role
  name: owner
  type: string
- description: The type of role that owns the database role
  name: owner_role_type
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/database-role-database-role-schema.json
slug: database-role-database-role
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: DatabaseRole
---
