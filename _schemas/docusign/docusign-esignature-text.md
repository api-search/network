---
description: A text input tab for free-form text entry.
layout: schema
name: Text
properties_list:
- description: ''
  name: tabId
  type: string
- description: ''
  name: tabLabel
  type: string
- description: ''
  name: documentId
  type: string
- description: ''
  name: pageNumber
  type: string
- description: ''
  name: recipientId
  type: string
- description: ''
  name: xPosition
  type: string
- description: ''
  name: yPosition
  type: string
- description: ''
  name: anchorString
  type: string
- description: ''
  name: value
  type: string
- description: When true, the recipient must fill in this tab.
  name: required
  type: string
- description: When true, the tab value cannot be changed.
  name: locked
  type: string
- description: Maximum length of text input.
  name: maxLength
  type: string
- description: ''
  name: width
  type: string
- description: ''
  name: height
  type: string
- description: ''
  name: font
  type: string
- description: ''
  name: fontSize
  type: string
- description: ''
  name: fontColor
  type: string
- description: ''
  name: bold
  type: string
- description: ''
  name: italic
  type: string
- description: ''
  name: underline
  type: string
- description: Regular expression for input validation.
  name: validationPattern
  type: string
- description: Error message displayed when validation fails.
  name: validationMessage
  type: string
- description: When true, the value is concealed on the document.
  name: concealValueOnDocument
  type: string
provider_name: Docusign
provider_slug: docusign
schema_file: json-schema/docusign-esignature-text-schema.json
slug: docusign-esignature-text
tags:
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
title: Text
---
