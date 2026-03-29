---
aid: github:github-createcommit
name: Create Commit
tags:
- Commits
humanURL: 
properties: []
description: >-
  Creates a new Git [commit object](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects).  **Signature verification object**  The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:  | Name | Type | Description | | - | - | -- | | `verified` | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified. | | `reason` | `string` | The reason f...

---
