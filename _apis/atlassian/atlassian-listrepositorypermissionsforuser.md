---
aid: atlassian:atlassian-listrepositorypermissionsforuser
name: List Repository Permissions For User
tags:
- Lists
- Repositories
- Permissions
- Users
humanURL: 
properties: []
description: >-
  This API endpoint retrieves a paginated list of repositories for which the authenticated user has explicit permissions in Bitbucket. It returns repository objects along with the specific permission level (read, write, or admin) that the user has been granted for each repository. The response excludes repositories where the user has inherited permissions through team or group membership, focusing only on direct permission assignments. This operation requires authentication and uses a GET reque...

---
