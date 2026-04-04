---
aid: microsoft-graph:microsoft-graph-permission-grants
name: Microsoft Graph Permission Grants
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/permissiongrants-openapi-original.yml
    type: OpenAPI
description: >-
  Microsoft Graph permission grants are the records and APIs in Microsoft Entra
  ID that represent the consent an application has to access resources. They
  link a client app (service principal) to a resource API and the specific
  permissions approved, and are used during token issuance to determine what the
  app can do. There are two main forms: delegated permission grants
  (oAuth2PermissionGrant), which capture user-consented scopes or tenant-wide
  admin consent, and app role assignments, which capture application permissions
  for app-only access. Using Microsoft Graph, administrators can list, audit,
  create, and revoke these grants to manage app access, respond to risk, and
  enforce least-privilege practices. In short, permission grants operationalize
  consent by making it inspectable and controllable across the tenant.

---