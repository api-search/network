---
description: CreateProjectRequest schema from Amazon Monitron API
layout: schema
name: CreateProjectRequest
properties_list:
- description: A unique case-sensitive identifier used to idempotently create a resource.
  name: clientToken
  type: string
- description: The ID of the AWS Key Management Service (KMS) key to use to encrypt your project data.
  name: kmsKeyId
  type: string
- description: The name of the project.
  name: projectName
  type: string
- description: Resource tags to add to the project.
  name: tags
  type: object
provider_name: Amazon Monitron
provider_slug: amazon-monitron
schema_file: json-schema/monitron-api-create-project-request-schema.json
slug: monitron-api-create-project-request
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: CreateProjectRequest
---
