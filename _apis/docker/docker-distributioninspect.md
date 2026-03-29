---
aid: docker:docker-distributioninspect
name: Distribution Inspect
tags:
- Distribution
- Inspect
humanURL: 
properties: []
description: >-
  This API endpoint retrieves detailed distribution information for a specific Docker image in JSON format. By making a GET request to /distribution/{name}/json with the image name as a parameter, it returns manifest and descriptor data about how the image is distributed across registries, including digest information, platform details, and layer metadata. This is useful for inspecting the distribution manifest of an image without pulling it, allowing users to verify image integrity, check avai...

---
