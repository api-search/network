---
description: ImportTask schema from Amazon Application Discovery Service API
layout: schema
name: ImportTask
properties_list:
- description: The unique ID for a specific import task.
  name: importTaskId
  type: string
- description: A unique token used to prevent the same import request from occurring more than once.
  name: clientRequestToken
  type: string
- description: A descriptive name for an import task.
  name: name
  type: string
- description: The URL for your import file that you've uploaded to Amazon S3.
  name: importUrl
  type: string
- description: The status of the import task.
  name: status
  type: string
- description: The time that the import task request was made, presented in the Unix time stamp format.
  name: importRequestTime
  type: string
- description: The time that the import task request finished, presented in the Unix time stamp format.
  name: importCompletionTime
  type: string
- description: The time that the import task request was deleted, presented in the Unix time stamp format.
  name: importDeletedTime
  type: string
- description: The total number of server records in the import file that were successfully imported.
  name: serverImportSuccess
  type: integer
- description: The total number of server records in the import file that failed to be imported.
  name: serverImportFailure
  type: integer
- description: The total number of application records in the import file that were successfully imported.
  name: applicationImportSuccess
  type: integer
- description: The total number of application records in the import file that failed to be imported.
  name: applicationImportFailure
  type: integer
- description: A link to a compressed archive folder (in the ZIP format) of all errors and failed entries that were detected, organized according to the type of error.
  name: errorsAndFailedEntriesZip
  type: string
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-import-task-schema.json
slug: application-discovery-service-import-task
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: ImportTask
---
