---
aid: atlassian:atlassian-put-workspaces-workspace-projects-project-key-branching-model-settings
name: Update the branching model config for a project
tags:
- - - - Branching model
humanURL: 
properties: []
description: >-
  Update the branching model configuration for a project.  The `development` branch can be configured to a specific branch or to track the main branch. Any branch name can be supplied, but will only successfully be applied to a repository via inheritance if that branch exists for that repository. Only the passed properties will be updated. The properties not passed will be left unchanged. A request without a `development` property will leave the development branch unchanged.  The `production` b...

---
