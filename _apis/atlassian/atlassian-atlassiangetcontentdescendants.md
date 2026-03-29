---
aid: atlassian:atlassian-atlassiangetcontentdescendants
name: Get Content Descendants
tags:
- Content - children and descendants
humanURL: 
properties: []
description: >-
  Returns a map of the descendants of a piece of content. This is similar<br>to [Get content children](#api-content-id-child-get), except that this<br>method returns child pages at all levels, rather than just the direct<br>child pages.<br><br>A piece of content has different types of descendants, depending on its type:<br><br>- `page`: descendant is `page`, `comment`, `attachment`<br>- `blogpost`: descendant is `comment`, `attachment`<br>- `attachment`: descendant is `comment`<br>- `comment`: ...

---
