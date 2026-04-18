---
description: A D1 serverless SQL database object from the Cloudflare API, representing an SQLite-compatible database running on Cloudflare's global network with support for time travel and automatic replication.
layout: schema
name: Cloudflare D1 Database
properties_list:
- description: The unique identifier of the D1 database.
  name: uuid
  type: string
- description: The name of the database.
  name: name
  type: string
- description: The internal version of the database.
  name: version
  type: string
- description: The number of tables in the database.
  name: num_tables
  type: integer
- description: The size of the database file in bytes.
  name: file_size
  type: integer
- description: The region where the primary database is running.
  name: running_in_region
  type: string
- description: When the database was created.
  name: created_at
  type: string
provider_name: Cloudflare
provider_slug: cloudflare
schema_file: json-schema/cloudflare-d1-database-schema.json
slug: cloudflare-d1-database
tags:
- AI Gateway
- API Gateway
- Artificial Intelligence
- CDN
- Cloud
- Containers
- DDoS Protection
- DNS
- Edge
- Edge Computing
- Object Storage
- Platform
- Real-Time Communication
- Security
- Serverless
- Web Performance
title: Cloudflare D1 Database
---
