---
aid: github:github-getreference
name: Get Reference
tags:
- Git Refs
humanURL: 
properties: []
description: >-
  Returns a single reference from your Git database. The `:ref` in the URL must be formatted as `heads/<branch name>` for branches and `tags/<tag name>` for tags. If the `:ref` doesn't match an existing ref, a `404` is returned.  **Note:** You need to explicitly [request a pull request](https://docs.github.com/enterprise-server@3.9/rest/pulls/pulls#get-a-pull-request) to trigger a test merge commit, which checks the mergeability of pull requests. For more information, see "[Checking mergeabilit...

---
