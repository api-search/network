---
description: Contains the recipient collections for an envelope, organized by recipient type.
layout: schema
name: Recipients
properties_list:
- description: List of signer recipients.
  name: signers
  type: array
- description: List of carbon copy recipients who receive a copy of the completed envelope.
  name: carbonCopies
  type: array
- description: List of certified delivery recipients who must confirm receipt of the envelope.
  name: certifiedDeliveries
  type: array
- description: List of in-person signer recipients for face-to-face signing scenarios.
  name: inPersonSigners
  type: array
- description: List of agent recipients who can designate another person to sign on their behalf.
  name: agents
  type: array
- description: List of editor recipients who can modify the envelope before it is sent.
  name: editors
  type: array
- description: List of intermediary recipients who can forward the envelope to another person for signing.
  name: intermediaries
  type: array
- description: List of witness recipients who verify the identity of a signer.
  name: witnesses
  type: array
- description: The total number of recipients in the envelope.
  name: recipientCount
  type: string
- description: The current routing order position.
  name: currentRoutingOrder
  type: string
provider_name: Docusign
provider_slug: docusign
schema_file: json-schema/docusign-esignature-recipients-schema.json
slug: docusign-esignature-recipients
tags:
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
title: Recipients
---
