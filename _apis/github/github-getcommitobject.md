---
aid: github:github-getcommitobject
name: Get Commit Object
tags:
- Commits
humanURL: 
properties: []
description: >-
  Gets a Git [commit object](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects).  To get the contents of a commit, see "[Get a commit](/rest/commits/commits#get-a-commit)."  **Signature verification object**  The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:  | Name | Type | Description | | - | - | -- | | `verified` | `boolean` | Indicates whether GitHub consider...

---
