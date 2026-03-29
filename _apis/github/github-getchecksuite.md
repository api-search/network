---
aid: github:github-getchecksuite
name: Get Check Suite
tags:
- Check Suites
humanURL: 
properties: []
description: >-
  Gets a single check suite using its `id`.  **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array and a `null` value for `head_branch`.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint on a private repository.

---
