---
description: A Quay organization.
layout: schema
name: Organization
properties_list:
- description: The name of the organization.
  name: name
  type: string
- description: The organization contact email.
  name: email
  type: string
- description: Whether invoices are sent to the organization email.
  name: invoice_email
  type: boolean
- description: Whether the current user is an admin of this organization.
  name: is_admin
  type: boolean
- description: Whether the current user is a member of this organization.
  name: is_member
  type: boolean
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-quay-organization-schema.json
slug: red-hat-quay-organization
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: Organization
---
