---
description: Contains the tab collections for an envelope recipient, organized by tab type.
layout: schema
name: EnvelopeRecipientTabs
properties_list:
- description: Signature tabs requiring the recipient to sign.
  name: signHereTabs
  type: array
- description: Initial tabs requiring the recipient to initial.
  name: initialHereTabs
  type: array
- description: Date signed tabs auto-filled with the signing date.
  name: dateSignedTabs
  type: array
- description: Text input tabs for free-form text entry.
  name: textTabs
  type: array
- description: Full name tabs auto-filled with the signer name.
  name: fullNameTabs
  type: array
- description: Email tabs for email address input.
  name: emailTabs
  type: array
- description: Checkbox tabs for boolean selection.
  name: checkboxTabs
  type: array
- description: Radio button group tabs for single-choice selection.
  name: radioGroupTabs
  type: array
- description: List tabs for dropdown selection.
  name: listTabs
  type: array
- description: Number tabs for numeric input.
  name: numberTabs
  type: array
- description: Date tabs for date selection.
  name: dateTabs
  type: array
- description: Formula tabs for calculated values.
  name: formulaTabs
  type: array
- description: Note tabs for displaying read-only text.
  name: noteTabs
  type: array
- description: Approve tabs for document approval.
  name: approveTabs
  type: array
- description: Decline tabs for document rejection.
  name: declineTabs
  type: array
provider_name: Docusign
provider_slug: docusign
schema_file: json-schema/docusign-esignature-envelope-recipient-tabs-schema.json
slug: docusign-esignature-envelope-recipient-tabs
tags:
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
title: EnvelopeRecipientTabs
---
