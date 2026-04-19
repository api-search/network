---
class_count: 5
classes:
- Environment
- KxEnvironment
- KxCluster
- KxDatabase
- KxUser
context_file: json-ld/amazon-finspace-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-finspace/refs/heads/main/json-ld/amazon-finspace-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Finspace from Amazon FinSpace.
layout: jsonld
name: Amazon Finspace Context
namespaces:
- prefix: finspace
  uri: https://aws.amazon.com/finspace/vocabulary/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: environmentId
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: environmentUrl
  type: anyURI
- container: ''
  name: environmentArn
  type: string
- container: ''
  name: awsAccountId
  type: string
- container: ''
  name: kmsKeyId
  type: string
- container: ''
  name: federationMode
  type: string
- container: ''
  name: clusterName
  type: string
- container: ''
  name: clusterType
  type: string
- container: ''
  name: capacityConfiguration
  type: ''
- container: ''
  name: databaseName
  type: string
- container: ''
  name: databaseArn
  type: string
- container: ''
  name: userArn
  type: string
- container: ''
  name: userName
  type: string
- container: ''
  name: iamRole
  type: string
- container: ''
  name: tags
  type: ''
- container: ''
  name: createdTimestamp
  type: dateTime
- container: ''
  name: lastModifiedTimestamp
  type: dateTime
- container: ''
  name: createTimestamp
  type: dateTime
- container: ''
  name: updateTimestamp
  type: dateTime
property_count: 22
provider_name: Amazon FinSpace
provider_slug: amazon-finspace
slug: amazon-finspace-context
tags:
- AWS
- Capital Markets
- Data Analytics
- Data Management
- Financial Services
- JSON-LD
- Linked Data
- Semantic Web
---
