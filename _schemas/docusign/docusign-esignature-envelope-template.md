---
description: A template that defines reusable documents, recipients, tabs, and routing for envelope workflows.
layout: schema
name: EnvelopeTemplate
properties_list:
- description: The unique identifier of the template.
  name: templateId
  type: string
- description: The URI for the template.
  name: uri
  type: string
- description: The name of the template.
  name: name
  type: string
- description: A description of the template.
  name: description
  type: string
- description: The date the template was created.
  name: created
  type: string
- description: The date the template was last modified.
  name: lastModified
  type: string
- description: The date the template was last used.
  name: lastUsed
  type: string
- description: Whether the template is shared.
  name: shared
  type: string
- description: The folder ID containing the template.
  name: folderId
  type: string
- description: The name of the folder containing the template.
  name: folderName
  type: string
- description: The default email subject for envelopes using this template.
  name: emailSubject
  type: string
- description: The default email body for envelopes using this template.
  name: emailBlurb
  type: string
- description: The signing location setting.
  name: signingLocation
  type: string
- description: The documents included in the template.
  name: documents
  type: array
- description: Template status.
  name: status
  type: string
provider_name: Docusign
provider_slug: docusign
schema_file: json-schema/docusign-esignature-envelope-template-schema.json
slug: docusign-esignature-envelope-template
tags:
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
title: EnvelopeTemplate
---
