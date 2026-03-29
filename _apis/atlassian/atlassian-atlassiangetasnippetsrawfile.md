---
aid: atlassian:atlassian-atlassiangetasnippetsrawfile
name: Get A Snippet S Raw File
tags:
- Snippets
humanURL: 
properties: []
description: >-
  Retrieves the raw contents of a specific file in the snippet. The<br>`Content-Disposition` header will be "attachment" to avoid issues with<br>malevolent executable files.<br><br>The file's mime type is derived from its filename and returned in the<br>`Content-Type` header.<br><br>Note that for text files, no character encoding is included as part of<br>the content type.

---
