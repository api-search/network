---
aid: microsoft-graph:microsoft-graph-directory-objects
name: Microsoft Graph Directory Objects
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/directoryobjects-openapi-original.yml
    type: OpenAPI
description: >-
  Microsoft Graph Directory Objects is the common base resource that represents
  any identity object stored in Microsoft Entra ID (Azure AD)including users,
  groups, devices, service principals, applications, and contactsand gives them
  a consistent ID, metadata, and set of relationships. Through this type and its
  child resources, apps can list and read objects, search and filter, paginate
  results, and traverse relationships such as memberOf, transitive memberships,
  owners, createdObjects, and ownedObjects. It also provides helper methods for
  directory intelligence and lifecycle tasks, such as delta queries to track
  changes, getByIds to resolve mixed sets of IDs, membership checks
  (checkMemberGroups/Objects, getMemberGroups/Objects, isMemberOf), and restore
  to recover soft-deleted items. Reference operations let you add or remove
  members and owners, enabling scenarios like access governance, entitlement
  management, and authorization. All access is enforced via Microsoft Graph
  permissions (for example, Directory.Read.All or Directory.ReadWrite.All) and
  respects directory policies and controls.

---