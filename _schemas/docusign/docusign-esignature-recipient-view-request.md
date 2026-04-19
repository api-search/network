---
description: Request body for generating an embedded recipient signing URL.
layout: schema
name: RecipientViewRequest
properties_list:
- description: The authentication method used to verify the recipient. Must match the authentication method used when the recipient was added.
  name: authenticationMethod
  type: string
- description: The email address of the recipient.
  name: email
  type: string
- description: The full name of the recipient.
  name: userName
  type: string
- description: The client user ID of the embedded signer.
  name: clientUserId
  type: string
- description: The recipient ID.
  name: recipientId
  type: string
- description: The URL to redirect the signer to after the signing session ends. DocuSign appends event query parameters.
  name: returnUrl
  type: string
- description: A URL that DocuSign pings during the signing session to confirm the parent frame is active.
  name: pingUrl
  type: string
- description: Frequency in seconds for ping requests.
  name: pingFrequency
  type: string
- description: URLs allowed to iframe the signing session (CSP frame-ancestors).
  name: frameAncestors
  type: array
- description: Origins allowed to receive postMessage events.
  name: messageOrigins
  type: array
- description: The security domain for the signing session.
  name: securityDomain
  type: string
provider_name: Docusign
provider_slug: docusign
schema_file: json-schema/docusign-esignature-recipient-view-request-schema.json
slug: docusign-esignature-recipient-view-request
tags:
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
title: RecipientViewRequest
---
