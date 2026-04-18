---
description: An Identity and Access Management (IAM) policy which specifies access controls for Google Cloud resources. A Policy is a collection of bindings that associate members with roles.
layout: schema
name: Policy
properties_list:
- description: Specifies the format of the policy. Valid values are 0, 1, and 3. Version 3 supports conditional role bindings.
  name: version
  type: integer
- description: Associates a list of members to a role, optionally with a condition.
  name: bindings
  type: array
- description: etag is used for optimistic concurrency control to help prevent simultaneous updates of a policy from overwriting each other.
  name: etag
  type: string
provider_name: Google Cloud Platform
provider_slug: google-cloud-platform
schema_file: json-schema/cloud-resource-manager-policy-schema.json
slug: cloud-resource-manager-policy
tags:
- API Management
- Cloud Computing
- Infrastructure
- Platform as a Service
title: Policy
---
