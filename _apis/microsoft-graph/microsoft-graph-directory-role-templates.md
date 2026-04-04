---
aid: microsoft-graph:microsoft-graph-directory-role-templates
name: Microsoft Graph Directory Role Templates
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/directoryroletemplates-openapi-original.yml
    type: OpenAPI
description: >-
  Microsoft Graph directory role templates are read-only blueprints that
  represent each built-in Microsoft Entra ID (formerly Azure AD) administrator
  role, such as Global Administrator or User Administrator. Exposed via the
  directoryRoleTemplate resource, they let you discover the full set of
  available roles and their stable template IDs, along with names and
  descriptions. You can use a templates ID to activate that role in your tenant
  by creating a directoryRole (POST to /directoryRoles with the roleTemplateId),
  after which the role appears in the directoryRoles collection and can have
  members assigned. Templates themselves cant be modified or assigned; they
  exist to enumerate built-in roles and enable consistent, automated activation
  across tenants.

---