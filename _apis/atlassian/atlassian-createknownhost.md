---
aid: atlassian:atlassian-createknownhost
name: Create Known Host
tags:
- Create
- Known
- Hosts
humanURL: 
properties: []
description: >-
  Creates a new known host entry in the Bitbucket Pipelines SSH configuration for a specified repository, allowing the pipeline to establish secure SSH connections to external servers by adding their public key fingerprints to the trusted known hosts list. This endpoint requires authentication and accepts the workspace identifier and repository slug as path parameters, along with the host details in the request body, which typically includes the hostname and its corresponding SSH public key. On...

---
