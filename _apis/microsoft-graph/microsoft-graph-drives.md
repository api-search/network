---
aid: microsoft-graph:microsoft-graph-drives
name: Microsoft Graph Drives
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/drives-openapi-original.yml
    type: OpenAPI
description: >-
  Microsoft Graph Drives is the part of Microsoft Graph that lets apps discover
  and work with files across OneDrive and SharePoint using a single, consistent
  REST API. A drive represents a top-level document librarypersonal or sharedand
  exposes its files and folders (driveItems) in the same way whether they live
  in a users OneDrive, a SharePoint site, a Microsoft 365 Group, or a Team. With
  it, you can list and search items, read and write file metadata and content,
  upload large files via upload sessions, move/copy/rename, manage versions,
  generate sharing links, and control permissions. It supports change tracking
  with delta queries and subscriptions (webhooks), plus thumbnails, previews,
  and special folders like root and Documents. Drives are addressed with
  endpoints such as /me/drive, /users/{id}/drive, /sites/{id}/drive, and
  /drives/{id}, with access governed by Microsoft Entra (Azure AD) scopes like
  Files.Read or Sites.Read.All. In short, it provides a unified,
  permission-aware way to build file-centric experiences across Microsoft 365.

---