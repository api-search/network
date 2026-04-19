---
description: Addon schema from Amazon EKS API
layout: schema
name: Addon
properties_list:
- description: The name of the add-on.
  name: addonName
  type: string
- description: The version of the add-on.
  name: addonVersion
  type: string
- description: The Amazon Resource Name (ARN) of the add-on.
  name: addonArn
  type: string
- description: The name of the cluster.
  name: clusterName
  type: string
- description: The status of the add-on.
  name: status
  type: string
- description: The Amazon Resource Name (ARN) of the IAM role.
  name: serviceAccountRoleArn
  type: string
- description: Metadata that assists with categorization and organization.
  name: tags
  type: object
- description: The Unix epoch timestamp at object creation.
  name: createdAt
  type: string
- description: The Unix epoch timestamp for the last modification.
  name: modifiedAt
  type: string
provider_name: Amazon EKS
provider_slug: amazon-eks
schema_file: json-schema/eks-openapi-addon-schema.json
slug: eks-openapi-addon
tags:
- AWS
- Container Orchestration
- Containers
- EKS
- Kubernetes
title: Addon
---
