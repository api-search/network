---
aid: atlassian:atlassian-deletesshkey
name: Delete Ssh Key
tags:
- Delete
- Ssh
- Keys
humanURL: 
properties: []
description: >-
  This API operation allows you to delete a specific SSH key associated with a Bitbucket user account by providing the username and the unique key identifier in the endpoint path. When executed via a DELETE request to `/users/{selected_user}/ssh-keys/{key_id}`, it permanently removes the specified SSH key from the user's account, revoking that key's access to Bitbucket repositories. This is commonly used when rotating security credentials, removing access for compromised keys, or cleaning up un...

---
