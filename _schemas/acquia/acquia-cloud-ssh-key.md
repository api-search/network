---
description: Details an SSH key.
layout: schema
name: Ssh Key
properties_list:
- description: The unique identifier of the SSH key.
  name: uuid
  type: string
- description: The human-readable key label.
  name: label
  type: string
- description: The public key.
  name: public_key
  type: string
- description: The public key fingerprint.
  name: fingerprint
  type: string
- description: The key creation date.
  name: created_at
  type: string
- description: ''
  name: _links
  type: object
provider_name: Acquia
provider_slug: acquia
schema_file: json-schema/acquia-cloud-ssh-key-schema.json
slug: acquia-cloud-ssh-key
tags:
- Content
- Experience
title: Ssh Key
---
