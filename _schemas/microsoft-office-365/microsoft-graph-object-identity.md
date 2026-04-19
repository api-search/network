---
description: Represents an identity used to sign in to a user account.
layout: schema
name: ObjectIdentity
properties_list:
- description: Specifies the type of user sign-in (e.g. emailAddress, userName, userPrincipalName).
  name: signInType
  type: string
- description: Specifies the issuer of the identity, for example contoso.onmicrosoft.com.
  name: issuer
  type: string
- description: Specifies the unique value associated with the issuer- signInType combination.
  name: issuerAssignedId
  type: string
provider_name: Microsoft Office 365
provider_slug: microsoft-office-365
schema_file: json-schema/microsoft-graph-object-identity-schema.json
slug: microsoft-graph-object-identity
tags:
- Cloud
- Collaboration
- Enterprise
- Microsoft
- Productivity
title: ObjectIdentity
---
