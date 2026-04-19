---
description: A signer recipient who must sign the envelope documents.
layout: schema
name: Signer
properties_list:
- description: Unique identifier for the recipient. Assigned by the sender.
  name: recipientId
  type: string
- description: The GUID for the recipient.
  name: recipientIdGuid
  type: string
- description: The full legal name of the signer.
  name: name
  type: string
- description: The email address of the signer.
  name: email
  type: string
- description: The routing order of the signer. Lower numbers are processed first. Recipients with the same routing order sign in parallel.
  name: routingOrder
  type: string
- description: The role name associated with the signer, used with templates.
  name: roleName
  type: string
- description: The client user ID for embedded signing. When set, the recipient is an embedded signer and must sign through your application using a generated signing URL.
  name: clientUserId
  type: string
- description: The status of the signer.
  name: status
  type: string
- description: The date and time the signer signed.
  name: signedDateTime
  type: string
- description: The date and time the envelope was delivered to the signer.
  name: deliveredDateTime
  type: string
- description: The date and time the signer declined.
  name: declinedDateTime
  type: string
- description: The reason the signer declined.
  name: declinedReason
  type: string
- description: Identity verification settings for this recipient.
  name: identityVerification
  type: object
- description: Phone authentication settings.
  name: phoneAuthentication
  type: object
- description: An access code the recipient must enter to access the envelope.
  name: accessCode
  type: string
- description: Whether ID lookup authentication is required.
  name: requireIdLookup
  type: string
- description: A private note to the signer from the sender.
  name: note
  type: string
provider_name: Docusign
provider_slug: docusign
schema_file: json-schema/docusign-esignature-signer-schema.json
slug: docusign-esignature-signer
tags:
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
title: Signer
---
