---
aid: github:github-updaterepositoryinvitation
name: Update Repository Invitation
tags:
- Update
- Repositories
- Invitation
humanURL: 
properties: []
description: >-
  This API endpoint allows you to update an existing repository invitation by modifying its permissions level. You must authenticate as a repository owner or administrator and provide the invitation ID in the URL path. The PATCH request accepts a JSON body with a 'permissions' field that can be set to 'read', 'write', 'maintain', 'triage', or 'admin' to change the access level being offered to the invited user. Upon successful execution, it returns the updated invitation object containing detai...

---
