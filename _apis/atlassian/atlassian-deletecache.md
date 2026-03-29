---
aid: atlassian:atlassian-deletecache
name: Delete Cache
tags:
- Delete
- Cache
humanURL: 
properties: []
description: >-
  Deletes a specific build cache from a Bitbucket repository's pipeline configuration using the cache's unique identifier. This operation removes cached dependencies, compiled artifacts, or other stored data that pipelines use to speed up build times, requiring authentication and appropriate permissions for the specified workspace and repository. Once deleted, the cache cannot be recovered and pipelines will need to rebuild the cache on subsequent runs.

---
