---
aid: atlassian:atlassian-listbranchrestrictions
name: List Branch Restrictions
tags:
- Lists
- Branches
- Restrictions
humanURL: 
properties: []
description: >-
  This operation retrieves all branch restrictions configured for a specific repository within a Bitbucket workspace. Branch restrictions are rules that control who can push to branches, require pull requests, enforce merge checks, or limit branch deletions. By sending a GET request to this endpoint with the workspace ID and repository slug, you receive a paginated list of all active restrictions including their types, patterns (which branches they apply to), and associated users or groups. Thi...

---
