---
description: An object in the infostore repository (folder, report, etc.)
layout: schema
name: InfostoreEntry
properties_list:
- description: Unique infostore object identifier
  name: id
  type: integer
- description: Cluster unique identifier
  name: cuid
  type: string
- description: Display name of the object
  name: name
  type: string
- description: Object type (e.g., Folder, CrystalReport)
  name: type
  type: string
- description: Object description
  name: description
  type: string
- description: Relative URI to access this object
  name: uri
  type: string
provider_name: Crystal Reports
provider_slug: crystal-reports
schema_file: json-schema/crystal-reports-infostore-entry-schema.json
slug: crystal-reports-infostore-entry
tags:
- Business Intelligence
- Crystal Reports
- Data Analytics
- Enterprise Software
- Reporting
- SAP
title: InfostoreEntry
---
