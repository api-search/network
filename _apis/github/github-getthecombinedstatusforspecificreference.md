---
aid: github:github-getthecombinedstatusforspecificreference
name: Get The Combined Status For Specific Reference
tags:
- Commit Statuses
humanURL: 
properties: []
description: >-
  Users with pull access in a repository can access a combined view of commit statuses for a given ref. The ref can be a SHA, a branch name, or a tag name.   Additionally, a combined `state` is returned. The `state` is one of:  *   **failure** if any of the contexts report as `error` or `failure` *   **pending** if there are no statuses or a context is `pending` *   **success** if the latest status for all contexts is `success`

---
