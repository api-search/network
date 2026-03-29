---
aid: github:github-downloadrepositoryarchivezip
name: Download Repository Archive (zip)
tags:
- Archives
humanURL: 
properties: []
description: >-
  Gets a redirect URL to download a zip archive for a repository. If you omit `:ref`, the repositorys default branch (usually `main`) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use the `Location` header to make a second `GET` request.  **Note**: For private repositories, these links are temporary and expire after five minutes. If the repository is empty, you will receive a 404 when you follow the redirect.

---
