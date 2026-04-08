---
aid: nuget:nuget-pushpackage
name: Push a package
tags:
- Package Publish
humanURL: 
properties: []
description: >-
  Pushes a new package to the NuGet feed. The request body must be a multipart form data payload where the first item is the raw bytes of the .nupkg file. If a package with the same ID and version already exists, the push will be rejected with a 409 status code.

---
