---
aid: atlassian:atlassian-atlassiangetthebranchingmodelconfigforarepository
name: Get The Branching Model Config For A Repository
tags:
- Branching model
humanURL: 
properties: []
description: >-
  Return the branching model configuration for a repository. The returned<br>object:<br><br>1. Always has a `development` property for the development branch.<br>2. Always a `production` property for the production branch. The<br>   production branch can be disabled.<br>3. The `branch_types` contains all the branch types.<br><br>This is the raw configuration for the branching model. A client<br>wishing to see the branching model with its actual current branches may<br>find the [active model API...

---
