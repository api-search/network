---
aid: docusign:docusign-rooms-adddocumenttoroom
name: Adds a document to a room.
tags:
- Rooms
humanURL: 
properties: []
description: >-
  Adds a document to a room.  The following properties in the request body are required. The `folderId` property is optional. All other properties are ignored.  - `name` - `base64Contents`  If a document with the specified name already exists, a counter is added to the name to make it unique.  For example, to create a document named **hello.txt** that contains the text `hello, world`, the body of your request would look like this:  ``` {   "name": "hello.txt",   "base64Contents": "aGVsbG8sIHdvc...

---
