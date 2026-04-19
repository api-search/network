---
description: Schema defining the structure of an Amazon Personalize dataset group resource, including datasets, solutions, campaigns, and recommenders for building personalized recommendation systems.
layout: schema
name: Amazon Personalize Dataset Group Definition
properties_list:
- description: The name of the dataset group.
  name: name
  type: string
- description: The Amazon Resource Name of the dataset group.
  name: datasetGroupArn
  type: string
- description: The current status of the dataset group.
  name: status
  type: string
- description: The domain of the dataset group for domain-based recommenders.
  name: domain
  type: string
- description: The ARN of the KMS key used to encrypt the datasets.
  name: kmsKeyArn
  type: string
- description: The ARN of the IAM role that has permissions to access the datasets.
  name: roleArn
  type: string
- description: The creation date and time of the dataset group.
  name: creationDateTime
  type: string
- description: The last updated date and time of the dataset group.
  name: lastUpdatedDateTime
  type: string
- description: The datasets in the dataset group.
  name: datasets
  type: array
- description: The trained solutions in the dataset group.
  name: solutions
  type: array
- description: The deployed campaigns for real-time recommendations.
  name: campaigns
  type: array
- description: Domain-based recommenders in the dataset group.
  name: recommenders
  type: array
provider_name: Amazon Personalize
provider_slug: amazon-personalize
schema_file: json-schema/amazon-personalize-schema.json
slug: amazon-personalize
tags:
- AI
- AWS
- Customer Experience
- Machine Learning
- ML
- Personalization
- Recommendations
title: Amazon Personalize Dataset Group Definition
---
