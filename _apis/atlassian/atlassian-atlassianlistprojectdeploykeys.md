---
aid: atlassian:atlassian-atlassianlistprojectdeploykeys
name: List Project Deploy Keys
tags:
- Lists
- Projects
- Deploy
- Keys
humanURL: 
properties: []
description: >-
  This GET operation retrieves a paginated list of all deploy keys configured for a specific project within a Bitbucket workspace. Deploy keys are SSH keys that grant read-only or read-write access to project repositories, commonly used for automated deployments and CI/CD pipelines. The endpoint requires both the workspace slug and project key as path parameters to identify the target project, and returns an array of deploy key objects containing details such as the key ID, label, public key va...

---
