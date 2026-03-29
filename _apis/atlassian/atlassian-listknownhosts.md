---
aid: atlassian:atlassian-listknownhosts
name: List Known Hosts
tags:
- Lists
- Known
- Hosts
humanURL: 
properties: []
description: >-
  This API endpoint retrieves a list of configured SSH known hosts for a specific Bitbucket repository's pipeline configuration. By making a GET request to `/repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts`, developers can view all SSH host fingerprints that have been added to the repository's pipeline settings, which are used to verify the identity of remote servers during SSH connections in CI/CD pipeline executions. The endpoint requires the workspace identifier and rep...

---
