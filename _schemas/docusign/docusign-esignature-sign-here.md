---
description: A signature tab placed on a document.
layout: schema
name: SignHere
properties_list:
- description: Unique identifier for the tab.
  name: tabId
  type: string
- description: Label used to identify the tab.
  name: tabLabel
  type: string
- description: The document ID where this tab is placed.
  name: documentId
  type: string
- description: The page number where this tab is placed.
  name: pageNumber
  type: string
- description: The recipient this tab is assigned to.
  name: recipientId
  type: string
- description: The X position of the tab on the page.
  name: xPosition
  type: string
- description: The Y position of the tab on the page.
  name: yPosition
  type: string
- description: Anchor text string used to automatically position the tab.
  name: anchorString
  type: string
- description: X offset from the anchor string position.
  name: anchorXOffset
  type: string
- description: Y offset from the anchor string position.
  name: anchorYOffset
  type: string
- description: Units for anchor offsets (pixels, inches, mms, cms).
  name: anchorUnits
  type: string
- description: Scale value for the signature.
  name: scaleValue
  type: string
- description: When true, the tab is optional for the recipient.
  name: optional
  type: string
- description: The type of stamp for the signature.
  name: stampType
  type: string
provider_name: Docusign
provider_slug: docusign
schema_file: json-schema/docusign-esignature-sign-here-schema.json
slug: docusign-esignature-sign-here
tags:
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
title: SignHere
---
