---
description: A composite template that combines server templates and inline templates for complex envelope workflows.
layout: schema
name: CompositeTemplate
properties_list:
- description: Unique identifier for the composite template.
  name: compositeTemplateId
  type: string
- description: ''
  name: serverTemplates
  type: array
- description: ''
  name: inlineTemplates
  type: array
provider_name: Docusign
provider_slug: docusign
schema_file: json-schema/docusign-esignature-composite-template-schema.json
slug: docusign-esignature-composite-template
tags:
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
title: CompositeTemplate
---
