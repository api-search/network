---
aid: atlassian:atlassian-atlassianupdateasnippet
name: Update A Snippet
tags:
- Snippets
humanURL: 
properties: []
description: >-
  Used to update a snippet. Use this to add and delete files and to<br>change a snippet's title.<br><br>To update a snippet, one can either PUT a full snapshot, or only the<br>parts that need to be changed.<br><br>The contract for PUT on this API is that properties missing from the<br>request remain untouched so that snippets can be efficiently<br>manipulated with differential payloads.<br><br>To delete a property (e.g. the title, or a file), include its name in<br>the request, but omit its val...

---
