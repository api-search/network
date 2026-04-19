---
description: Schema representing an Amazon Translate batch translation job resource.
layout: schema
name: Amazon Translate Translation Job
properties_list:
- description: The ID of the translation job.
  name: JobId
  type: string
- description: The user-provided name of the translation job.
  name: JobName
  type: string
- description: The status of the translation job.
  name: JobStatus
  type: string
- description: The language code of the source language.
  name: SourceLanguageCode
  type: string
- description: The language codes of the target languages.
  name: TargetLanguageCodes
  type: array
- description: The input data configuration for the translation job.
  name: InputDataConfig
  type: object
- description: The output data configuration for the translation job.
  name: OutputDataConfig
  type: object
- description: The Amazon Resource Name (ARN) of the IAM role for S3 access.
  name: DataAccessRoleArn
  type: string
- description: The names of custom terminologies applied to the job.
  name: TerminologyNames
  type: array
- description: The time the translation job was submitted.
  name: SubmittedTime
  type: string
- description: The time the translation job ended.
  name: EndTime
  type: string
- description: A list of tags associated with the translation job.
  name: Tags
  type: array
provider_name: Amazon Translate
provider_slug: amazon-translate
schema_file: json-schema/amazon-translate-job-schema.json
slug: amazon-translate-job
tags:
- AWS
- Language Processing
- Localization
- Machine Translation
- NLP
- Translation
title: Amazon Translate Translation Job
---
