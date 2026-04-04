---
aid: microsoft-graph:microsoft-graph-service-principals
name: Microsoft Graph Service Principals
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/serviceprincipals-openapi-original.yml
    type: OpenAPI
description: >-
  In Microsoft Entra ID (formerly Azure AD), a service principal is the identity
  an application uses to access resources, and the Microsoft Graph service
  principal is the tenant-local representation of the Microsoft Graph API
  itself. It publishes the set of OAuth 2.0 delegated scopes and application
  roles (permissions) that apps can request, and it is the target against which
  your apps own service principal is granted consent. Once consented, your app
  can obtain tokens and call Microsoft Grapheither on behalf of a user
  (delegated) or as an unattended daemon/background service (application). This
  model enables secure, least-privilege, auditable access to Microsoft 365 data
  and directory resources, using certificates or client secrets, governed by
  admin consent, Conditional Access, and directory policies.

---