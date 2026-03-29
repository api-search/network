---
aid: atlassian:atlassian-atlassianlisttags
name: List Tags
tags:
- Refs
humanURL: 
properties: []
description: >-
  Returns the tags in the repository.<br><br>By default, results will be in the order the underlying source control system returns them and identical to<br>the ordering one sees when running "$ git tag --list". Note that this follows simple<br>lexical ordering of the ref names.<br><br>This can be undesirable as it does apply any natural sorting semantics, meaning for instance that tags are<br>sorted ["v10", "v11", "v9"] instead of ["v9", "v10", "v11"].<br><br>Sorting can be changed using the ?s...

---
