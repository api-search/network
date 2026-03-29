---
aid: atlassian:atlassian-get-workspaces-workspace-projects-project-key-branching-model
name: Get the branching model for a project
tags:
- - - - Branching model
humanURL: 
properties: []
description: >-
  Return the branching model set at the project level. This view is read-only. The branching model settings can be changed using the [settings](#api-workspaces-workspace-projects-project-key-branching-model-settings-get) API.  The returned object:  1. Always has a `development` property. `development.name` is    the user-specified branch that can be inherited by an individual repository's    branching model. 2. Might have a `production` property. `production` will not    be present when `produc...

---
