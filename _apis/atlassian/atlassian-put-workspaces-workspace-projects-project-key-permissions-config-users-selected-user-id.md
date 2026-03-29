---
aid: atlassian:atlassian-put-workspaces-workspace-projects-project-key-permissions-config-users-selected-user-id
name: Update an explicit user permission for a project
tags:
- - - - Projects
humanURL: 
properties: []
description: >-
  Updates the explicit user permission for a given user and project. The selected user must be a member of the workspace, and cannot be the workspace owner.  Only users with admin permission for the project may access this resource.  Due to security concerns, the JWT and OAuth authentication methods are unsupported. This is to ensure integrations and add-ons are not allowed to change permissions.  Permissions can be:  * `admin` * `create-repo` * `write` * `read`

---
