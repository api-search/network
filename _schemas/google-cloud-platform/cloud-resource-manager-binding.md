---
description: Associates members with a role.
layout: schema
name: Binding
properties_list:
- description: 'The role that is assigned to the list of members. Example: roles/resourcemanager.projectViewer.'
  name: role
  type: string
- description: The identities requesting access. Supports user, serviceAccount, group, and domain members.
  name: members
  type: array
provider_name: Google Cloud Platform
provider_slug: google-cloud-platform
schema_file: json-schema/cloud-resource-manager-binding-schema.json
slug: cloud-resource-manager-binding
tags:
- API Management
- Cloud Computing
- Infrastructure
- Platform as a Service
title: Binding
---
