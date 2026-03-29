---
aid: github:github-getteambyname
name: Get Team By Name
tags:
- Get
- Teams
- Name
humanURL: 
properties: []
description: >-
  Gets a team using the team's `slug`. To create the `slug`, GitHub Enterprise Server replaces special characters in the `name` string, changes all words to lowercase, and replaces spaces with a `-` separator. For example, `"My TEam Näme"` would become `my-team-name`.  **Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}`.

---
