---
aid: atlassian:atlassian-post-workspaces-workspace-projects
name: Create a project in a workspace
tags:
- - - - Projects
humanURL: 
properties: []
description: >-
  Creates a new project.  Note that the avatar has to be embedded as either a data-url or a URL to an external image as shown in the examples below:  ``` $ body=$(cat << EOF {     "name": "Mars Project",     "key": "MARS",     "description": "Software for colonizing mars.",     "links": {         "avatar": {             "href": "data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/..."         }     },     "is_private": false } EOF ) $ curl -H "Content-Type: applicati...

---
