---
description: Repository schema from Amazon ECR Amazon Elastic Container Registry (ECR) API
layout: schema
name: Repository
properties_list:
- description: The Amazon Resource Name (ARN) of the repository.
  name: repositoryArn
  type: string
- description: The AWS account ID associated with the registry.
  name: registryId
  type: string
- description: The name of the repository.
  name: repositoryName
  type: string
- description: The URI for the repository.
  name: repositoryUri
  type: string
- description: The date and time the repository was created.
  name: createdAt
  type: string
- description: The tag mutability setting for the repository.
  name: imageTagMutability
  type: string
- description: The image scanning configuration for the repository.
  name: imageScanningConfiguration
  type: object
- description: The encryption configuration for the repository.
  name: encryptionConfiguration
  type: object
provider_name: Amazon ECR
provider_slug: amazon-ecr
schema_file: json-schema/ecr-openapi-repository-schema.json
slug: ecr-openapi-repository
tags:
- Amazon Web Services
- AWS
- Container Images
- Container Registry
- Containers
- Docker
- ECR
- OCI
title: Repository
---
