---
description: Represents an Amazon FinSpace managed kdb (kdb+/q) environment.
layout: schema
name: KxEnvironment
properties_list:
- description: ''
  name: environmentId
  type: string
- description: ''
  name: name
  type: string
- description: ''
  name: awsAccountId
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: tgwStatus
  type: string
- description: ''
  name: dnsStatus
  type: string
- description: ''
  name: errorMessage
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: environmentArn
  type: string
- description: ''
  name: kmsKeyId
  type: string
- description: ''
  name: dedicatedServiceAccountId
  type: string
- description: ''
  name: transitGatewayConfiguration
  type: object
- description: ''
  name: customDNSConfiguration
  type: array
- description: ''
  name: creationTimestamp
  type: string
- description: ''
  name: updateTimestamp
  type: string
- description: ''
  name: availabilityZoneIds
  type: array
- description: ''
  name: certificateAuthorityArn
  type: string
- description: ''
  name: tags
  type: object
provider_name: Amazon FinSpace
provider_slug: amazon-finspace
schema_file: json-schema/amazon-finspace-kx-environment-schema.json
slug: amazon-finspace-kx-environment
tags:
- AWS
- Capital Markets
- Data Analytics
- Data Management
- Financial Services
title: KxEnvironment
---
