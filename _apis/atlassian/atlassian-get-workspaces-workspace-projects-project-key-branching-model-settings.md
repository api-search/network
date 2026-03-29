---
aid: atlassian:atlassian-get-workspaces-workspace-projects-project-key-branching-model-settings
name: Get the branching model config for a project
tags:
- - - - Branching model
humanURL: 
properties: []
description: >-
  Return the branching model configuration for a project. The returned object:  1. Always has a `development` property for the development branch. 2. Always a `production` property for the production branch. The    production branch can be disabled. 3. The `branch_types` contains all the branch types.   This is the raw configuration for the branching model. A client wishing to see the branching model with its actual current branches may find the [active model API](#api-workspaces-workspace-proj...

---
