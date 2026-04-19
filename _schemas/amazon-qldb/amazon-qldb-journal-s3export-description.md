---
description: Information about a journal export job, including the ledger name, export ID, creation time, current status, and the parameters of the original export creation request.
layout: schema
name: JournalS3ExportDescription
properties_list:
- description: ''
  name: LedgerName
  type: object
- description: ''
  name: ExportId
  type: object
- description: ''
  name: ExportCreationTime
  type: object
- description: ''
  name: Status
  type: object
- description: ''
  name: InclusiveStartTime
  type: object
- description: ''
  name: ExclusiveEndTime
  type: object
- description: ''
  name: S3ExportConfiguration
  type: object
- description: ''
  name: RoleArn
  type: object
- description: ''
  name: OutputFormat
  type: object
provider_name: Amazon QLDB
provider_slug: amazon-qldb
schema_file: json-schema/amazon-qldb-journal-s3export-description-schema.json
slug: amazon-qldb-journal-s3export-description
tags:
- AWS
- Blockchain
- Database
- Ledger
title: JournalS3ExportDescription
---
