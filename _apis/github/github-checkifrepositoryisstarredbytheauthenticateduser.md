---
aid: github:github-checkifrepositoryisstarredbytheauthenticateduser
name: Check If Repository Is Starred By The Authenticated User
tags:
- Checks
- Repositories
- Starred
- Authenticated
- Users
humanURL: 
properties: []
description: >-
  This API endpoint allows you to verify whether the currently authenticated user has starred a specific GitHub repository. By making a GET request to /user/starred/{owner}/{repo}, where {owner} is the repository owner's username and {repo} is the repository name, the API will return a 204 No Content status if the repository is starred by the user, or a 404 Not Found status if it is not starred. This endpoint requires authentication and is useful for applications that need to display or track a...

---
