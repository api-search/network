---
aid: atlassian:atlassian-atlassiangetthebranchingmodelforarepository
name: Get The Branching Model For A Repository
tags:
- Branching model
humanURL: 
properties: []
description: >-
  Return the branching model as applied to the repository. This view is<br>read-only. The branching model settings can be changed using the<br>[settings](#api-repositories-workspace-repo-slug-branching-model-settings-get) API.<br><br>The returned object:<br><br>1. Always has a `development` property. `development.branch` contains<br>   the actual repository branch object that is considered to be the<br>   `development` branch. `development.branch` will not be present<br>   if it does not exist....

---
