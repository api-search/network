---
aid: atlassian:atlassian-post-workspaces-workspace-hooks
name: Create a webhook for a workspace
tags:
- - - - Workspaces
      - Webhooks
humanURL: 
properties: []
description: >-
  Creates a new webhook on the specified workspace.  Workspace webhooks are fired for events from all repositories contained by that workspace.  Example:  ``` $ curl -X POST -u credentials -H 'Content-Type: application/json'   https://api.bitbucket.org/2.0/workspaces/my-workspace/hooks   -d '     {       "description": "Webhook Description",       "url": "https://example.com/",       "active": true,       "secret": "this is a really bad secret",       "events": [         "repo:push",         "i...

---
