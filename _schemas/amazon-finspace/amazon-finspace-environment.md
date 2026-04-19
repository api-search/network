---
description: Represents an Amazon FinSpace environment for financial analytics workloads.
layout: schema
name: Environment
properties_list:
- description: Unique identifier for the environment.
  name: environmentId
  type: string
- description: Name of the FinSpace environment.
  name: name
  type: string
- description: AWS account ID of the environment owner.
  name: awsAccountId
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: environmentUrl
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: environmentArn
  type: string
- description: ''
  name: sageMakerStudioDomainUrl
  type: string
- description: ''
  name: kmsKeyId
  type: string
- description: ''
  name: dedicatedServiceAccountId
  type: string
- description: ''
  name: federationMode
  type: string
- description: ''
  name: tags
  type: object
provider_name: Amazon FinSpace
provider_slug: amazon-finspace
schema_file: json-schema/amazon-finspace-environment-schema.json
slug: amazon-finspace-environment
tags:
- AWS
- Capital Markets
- Data Analytics
- Data Management
- Financial Services
title: Environment
---
