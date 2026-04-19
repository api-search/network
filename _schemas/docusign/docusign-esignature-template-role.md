---
description: Maps a recipient to a role defined in a template. Used when creating an envelope from a template.
layout: schema
name: TemplateRole
properties_list:
- description: The recipient's full name.
  name: name
  type: string
- description: The recipient's email address.
  name: email
  type: string
- description: The role name that matches a role defined in the template.
  name: roleName
  type: string
- description: The client user ID for embedded signing.
  name: clientUserId
  type: string
- description: When true, this is the default recipient for the role.
  name: defaultRecipient
  type: string
- description: The routing order for the recipient.
  name: routingOrder
  type: string
- description: Access code for authentication.
  name: accessCode
  type: string
provider_name: Docusign
provider_slug: docusign
schema_file: json-schema/docusign-esignature-template-role-schema.json
slug: docusign-esignature-template-role
tags:
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
title: TemplateRole
---
