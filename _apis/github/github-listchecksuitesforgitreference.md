---
aid: github:github-listchecksuitesforgitreference
name: List Check Suites For Git Reference
tags:
- Check Suites
humanURL: 
properties: []
description: >-
  Lists check suites for a commit `ref`. The `ref` can be a SHA, branch name, or a tag name.  **Note:** The endpoints to manage checks only look for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array and a `null` value for `head_branch`.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint on a private repository.

---
