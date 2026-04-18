---
description: The policy rules under which the key can be exported.
layout: schema
name: KeyReleasePolicy
properties_list:
- description: Content type and version of key release policy.
  name: contentType
  type: string
- description: Defines whether the policy is immutable.
  name: immutable
  type: boolean
- description: Blob encoding the policy rules (base64url-encoded).
  name: data
  type: string
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-key-vault-key-release-policy-schema.json
slug: azure-key-vault-key-release-policy
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: KeyReleasePolicy
---
