---
aid: microsoft-graph:microsoft-graph-shares
name: Microsoft Graph Shares
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/shares-openapi-original.yml
    type: OpenAPI
description: >-
  Microsoft Graph Shares is the part of Microsoft Graph that lets apps access a
  OneDrive or SharePoint item by its sharing link or token, without needing to
  know the site, drive, or item IDs. Given a share URL, you can resolve it to a
  sharedDriveItem and then work with the underlying driveItem or listItem: read
  metadata, navigate folder children, fetch thumbnails, and download contentand,
  if the link grants edit rights, make changes. It works across OneDrive
  (personal and business) and SharePoint, including anonymous links, by using an
  encoded form of the sharing URL (often the u! token) at the
  /shares/{shareIdOrUrl} endpoint. This is distinct from listing items shared
  with a user; Shares is specifically for dereferencing and operating on a
  single shared link in a uniform way.

---