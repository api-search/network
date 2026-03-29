---
aid: github:github-createtagobject
name: Create Tag Object
tags:
- Git Tags
humanURL: 
properties: []
description: >-
  Note that creating a tag object does not create the reference that makes a tag in Git. If you want to create an annotated tag in Git, you have to do this call to create the tag object, and then [create](https://docs.github.com/enterprise-server@3.9/rest/git/refs#create-a-reference) the `refs/tags/[tag]` reference. If you want to create a lightweight tag, you only have to [create](https://docs.github.com/enterprise-server@3.9/rest/git/refs#create-a-reference) the tag reference - this call woul...

---
