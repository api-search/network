---
description: Summary of an envelope update operation.
layout: schema
name: EnvelopeUpdateSummary
properties_list:
- description: The envelope ID.
  name: envelopeId
  type: string
- description: Bulk envelope status information, if applicable.
  name: bulkEnvelopeStatus
  type: object
- description: ''
  name: listCustomFieldUpdateResults
  type: array
- description: ''
  name: recipientUpdateResults
  type: array
- description: ''
  name: textCustomFieldUpdateResults
  type: array
provider_name: Docusign
provider_slug: docusign
schema_file: json-schema/docusign-esignature-envelope-update-summary-schema.json
slug: docusign-esignature-envelope-update-summary
tags:
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
title: EnvelopeUpdateSummary
---
