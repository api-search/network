---
description: Schema representing an Amazon Elastic Container Registry repository, which stores Docker container images and OCI artifacts.
layout: schema
name: Amazon ECR Repository
properties_list:
- description: The Amazon Resource Name (ARN) that identifies the repository.
  name: repositoryArn
  type: string
- description: The AWS account ID associated with the registry that contains the repository.
  name: registryId
  type: string
- description: The name of the repository.
  name: repositoryName
  type: string
- description: The URI for the repository, used for docker pull and push operations.
  name: repositoryUri
  type: string
- description: The date and time, in JavaScript date format, when the repository was created.
  name: createdAt
  type: string
- description: The tag mutability setting for the repository. When set to IMMUTABLE, all image tags within the repository are prevented from being overwritten.
  name: imageTagMutability
  type: string
- description: The image scanning configuration for the repository.
  name: imageScanningConfiguration
  type: object
- description: The encryption configuration for the repository.
  name: encryptionConfiguration
  type: object
- description: The number of images in the repository.
  name: imageCount
  type: integer
- description: The JSON repository policy text associated with the repository.
  name: repositoryPolicy
  type: string
- description: The lifecycle policy for the repository.
  name: lifecyclePolicy
  type: object
- description: The metadata tags applied to the repository.
  name: tags
  type: array
provider_name: Amazon ECR
provider_slug: amazon-ecr
schema_file: json-schema/amazon-ecr-repository-schema.json
slug: amazon-ecr-repository
tags:
- Amazon Web Services
- AWS
- Container Images
- Container Registry
- Containers
- Docker
- ECR
- OCI
title: Amazon ECR Repository
---
