---
description: A Timestream database resource containing tables for time series data storage.
layout: schema
name: Database
properties_list:
- description: The Amazon Resource Name that uniquely identifies this database.
  name: Arn
  type: string
- description: The name of the Timestream database.
  name: DatabaseName
  type: string
- description: The total number of tables found within the Timestream database.
  name: TableCount
  type: integer
- description: The identifier of the KMS key used to encrypt the data stored in the database.
  name: KmsKeyId
  type: string
- description: The time when the database was created.
  name: CreationTime
  type: string
- description: The last time that this database was updated.
  name: LastUpdatedTime
  type: string
provider_name: Amazon Timestream
provider_slug: amazon-timestream
schema_file: json-schema/amazon-timestream-database-schema.json
slug: amazon-timestream-database
tags:
- AWS
- Database
- Iot
- Time Series
title: Database
---
