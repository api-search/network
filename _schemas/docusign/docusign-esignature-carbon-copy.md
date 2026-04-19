---
description: A carbon copy recipient who receives a copy of the completed documents but does not need to take any action.
layout: schema
name: CarbonCopy
properties_list:
- description: Unique identifier for the recipient.
  name: recipientId
  type: string
- description: The full name of the recipient.
  name: name
  type: string
- description: The email address of the recipient.
  name: email
  type: string
- description: The routing order of the recipient.
  name: routingOrder
  type: string
- description: The role name for template matching.
  name: roleName
  type: string
- description: The status of the recipient.
  name: status
  type: string
- description: A note for the recipient.
  name: note
  type: string
provider_name: Docusign
provider_slug: docusign
schema_file: json-schema/docusign-esignature-carbon-copy-schema.json
slug: docusign-esignature-carbon-copy
tags:
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
title: CarbonCopy
---
