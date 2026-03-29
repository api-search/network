---
aid: atlassian:atlassian-listcommitsforrevision
name: List Commits For Revision
tags:
- Lists
- Commits
humanURL: 
properties: []
description: >-
  This API endpoint retrieves a paginated list of commits for a specific revision in a Bitbucket repository. By making a GET request to /repositories/{workspace}/{repo_slug}/commits/{revision}, you can access commit history starting from the specified revision, which can be a branch name, tag, or commit SHA. The endpoint returns commit details including author information, commit messages, timestamps, and parent commit references. The response is paginated to handle repositories with extensive ...

---
