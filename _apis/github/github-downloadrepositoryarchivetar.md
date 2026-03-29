---
aid: github:github-downloadrepositoryarchivetar
name: Download Repository Archive (tar)
tags:
- Archives
humanURL: 
properties: []
description: >-
  Gets a redirect URL to download a tar archive for a repository. If you omit `:ref`, the repositorys default branch (usually `main`) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use the `Location` header to make a second `GET` request. **Note**: For private repositories, these links are temporary and expire after five minutes.

---
