---
description: An AWS Supply Chain instance
layout: schema
name: Instance
properties_list:
- description: The unique identifier of the instance
  name: instanceId
  type: string
- description: The name of the instance
  name: instanceName
  type: string
- description: The description of the instance
  name: instanceDescription
  type: string
- description: The state of the instance
  name: instanceState
  type: string
- description: The KMS key ARN used to encrypt instance data
  name: kmsKeyArn
  type: string
- description: The DNS domain for the web application
  name: webAppDnsDomain
  type: string
- description: The creation timestamp
  name: createdTime
  type: string
- description: The last modification timestamp
  name: lastModifiedTime
  type: string
provider_name: Amazon Supply Chain
provider_slug: amazon-supply-chain
schema_file: json-schema/amazon-supply-chain-instance-schema.json
slug: amazon-supply-chain-instance
tags:
- AWS
- ERP Integration
- Logistics
- Machine Learning
- Supply Chain
title: Instance
---
