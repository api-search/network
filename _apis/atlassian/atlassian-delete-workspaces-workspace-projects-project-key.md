---
aid: atlassian:atlassian-delete-workspaces-workspace-projects-project-key
name: Delete a project for a workspace
tags:
- - - - Projects
humanURL: 
properties: []
description: >-
  Deletes this project. This is an irreversible operation.  You cannot delete a project that still contains repositories. To delete the project, [delete](/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-delete) or transfer the repositories first.  Example: ``` $ curl -X DELETE https://api.bitbucket.org/2.0/workspaces/bbworkspace1/projects/PROJ ```

---
