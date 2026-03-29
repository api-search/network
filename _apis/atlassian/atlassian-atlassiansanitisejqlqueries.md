---
aid: atlassian:atlassian-atlassiansanitisejqlqueries
name: Sanitize Jql Queries
tags:
- JQL
humanURL: 
properties: []
description: >-
  Sanitizes one or more JQL queries by converting readable details into IDs where a user doesn't have permission to view the entity.<br><br>For example, if the query contains the clause *project = 'Secret project'*, and a user does not have browse permission for the project "Secret project", the sanitized query replaces the clause with *project = 12345"* (where 12345 is the ID of the project). If a user has the required permission, the clause is not sanitized. If the account ID is null, sanitiz...

---
