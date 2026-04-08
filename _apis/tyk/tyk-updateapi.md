---
aid: tyk:tyk-updateapi
name: Tyk Updating an API definition with its ID.
tags:
- API
humanURL: 
properties: []
description: >-
  Updating an API definition uses the same signature and object as a `POST`, however it will first ensure that the API ID that is being updated is the same as the one in the object being `PUT`.  Updating will completely replace the file descriptor and will not change an API Definition that has already been loaded, the hot-reload endpoint will need to be called to push the new definition to live.

---
