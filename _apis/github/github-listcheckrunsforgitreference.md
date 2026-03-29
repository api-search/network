---
aid: github:github-listcheckrunsforgitreference
name: List Check Runs For Git Reference
tags:
- Check Runs
humanURL: 
properties: []
description: >-
  Lists check runs for a commit ref. The `ref` can be a SHA, branch name, or a tag name.  **Note:** The endpoints to manage checks only look for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.  If there are more than 1000 check suites on a single git reference, this endpoint will limit check runs to the 1000 most recent check suites. To iterate over all possible check ...

---
