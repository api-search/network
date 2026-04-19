---
class_count: 4
classes:
- Amazon ECR Repository
- CreateRepositoryResponse
- DescribeRepositoriesResponse
- Repository
context_file: json-ld/amazon-ecr-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-ecr/refs/heads/main/json-ld/amazon-ecr-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Ecr from Amazon ECR.
layout: jsonld
name: Amazon Ecr Context
namespaces:
- prefix: aws
  uri: https://aws.amazon.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: pan
  uri: https://aws.amazon.com/schema/
properties:
- container: ''
  name: repositoryArn
  type: string
- container: ''
  name: registryId
  type: string
- container: ''
  name: repositoryName
  type: string
- container: ''
  name: repositoryUri
  type: reference
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: imageTagMutability
  type: string
- container: ''
  name: imageScanningConfiguration
  type: reference
- container: ''
  name: scanOnPush
  type: boolean
- container: ''
  name: encryptionConfiguration
  type: reference
- container: ''
  name: encryptionType
  type: string
- container: ''
  name: kmsKey
  type: string
- container: ''
  name: imageCount
  type: integer
- container: ''
  name: repositoryPolicy
  type: string
- container: ''
  name: lifecyclePolicy
  type: reference
- container: ''
  name: lifecyclePolicyText
  type: string
- container: ''
  name: lastEvaluatedAt
  type: dateTime
- container: set
  name: tags
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: repository
  type: string
- container: set
  name: repositories
  type: string
- container: ''
  name: nextToken
  type: string
property_count: 22
provider_name: Amazon ECR
provider_slug: amazon-ecr
slug: amazon-ecr-context
tags:
- Amazon Web Services
- AWS
- Container Images
- Container Registry
- Containers
- Docker
- ECR
- OCI
- JSON-LD
- Linked Data
- Semantic Web
---
