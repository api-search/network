---
description: Represents an Azure Active Directory directory object. This is the base type for most directory resources.
layout: schema
name: DirectoryObject
properties_list:
- description: The OData type of the directory object.
  name: '@odata.type'
  type: string
- description: The unique identifier for the object. Globally unique across all directory objects.
  name: id
  type: string
- description: Date and time when this object was deleted.
  name: deletedDateTime
  type: string
provider_name: Azure Active Directory
provider_slug: azure-active-directory
schema_file: json-schema/microsoft-graph-identity-directory-object-schema.json
slug: microsoft-graph-identity-directory-object
tags:
- Authentication
- Authorization
- Identity
- Microsoft
- Microsoft Entra
- OAuth
- OpenID Connect
- SAML
- SCIM
- Single Sign-On
- Zero Trust
title: DirectoryObject
---
