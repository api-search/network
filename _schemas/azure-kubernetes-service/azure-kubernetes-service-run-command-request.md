---
description: A run command request.
layout: schema
name: RunCommandRequest
properties_list:
- description: The command to run.
  name: command
  type: string
- description: A base64 encoded zip file containing the files required by the command.
  name: context
  type: string
- description: AuthToken issued for AKS AAD Server App.
  name: clusterToken
  type: string
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-run-command-request-schema.json
slug: azure-kubernetes-service-run-command-request
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: RunCommandRequest
---
