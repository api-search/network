---
description: The envelope definition object that contains all the properties needed to create and send an envelope.
layout: schema
name: EnvelopeDefinition
properties_list:
- description: The subject line of the email sent to recipients.
  name: emailSubject
  type: string
- description: The body text of the email sent to recipients.
  name: emailBlurb
  type: string
- description: The envelope status. Set to "sent" to send the envelope immediately, or "created" to save as a draft.
  name: status
  type: string
- description: The ID of a template to use as the basis for the envelope. When specified, the template's documents, recipients, and tabs are merged with any specified in the request.
  name: templateId
  type: string
- description: Template role assignments that map recipients to template roles when using a templateId.
  name: templateRoles
  type: array
- description: The documents to include in the envelope.
  name: documents
  type: array
- description: An array of composite template objects that combine server templates and inline templates for complex workflows.
  name: compositeTemplates
  type: array
- description: The ID of the brand to apply to the envelope.
  name: brandId
  type: string
- description: When true, the envelope ID is stamped in the document margins.
  name: envelopeIdStamping
  type: string
provider_name: Docusign
provider_slug: docusign
schema_file: json-schema/docusign-esignature-envelope-definition-schema.json
slug: docusign-esignature-envelope-definition
tags:
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
title: EnvelopeDefinition
---
