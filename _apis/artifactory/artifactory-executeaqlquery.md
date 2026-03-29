---
aid: artifactory:artifactory-executeaqlquery
name: Execute AQL Query
tags:
- AQL Search
humanURL: 
properties: []
description: >-
  Executes an Artifactory Query Language (AQL) query and returns matching results. AQL supports querying across multiple domains including items (artifacts), builds, entries, and more. Queries can include filtering, sorting, pagination, and inclusion of related entities.  AQL query syntax follows the pattern: `domain.find(criteria).include(fields).sort(sort_criteria).offset(n).limit(n)`  Supported primary domains: - **items**: Search for artifacts (files and folders) - **builds**: Search for bu...

---
