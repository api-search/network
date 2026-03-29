---
aid: atlassian:atlassian-createbuildstatusforcommit
name: Create Build Status For Commit
tags:
- Create
- Builds
- Status
- Commits
humanURL: 
properties: []
description: >-
  This POST endpoint creates a build status for a specific commit in a Bitbucket repository, allowing external CI/CD systems and build tools to report the status of automated builds back to Bitbucket. The endpoint requires the workspace ID, repository slug, and commit hash as path parameters, and accepts a JSON payload containing build status information such as state (successful, failed, in progress), key, name, URL, and description. When invoked, it associates the provided build status with t...

---
