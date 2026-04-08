---
aid: vtex:vtex-editsession
name: VTex Edit session
tags:
- Session
humanURL: 
properties: []
description: >-
  Edits information from a previously created sesssion.  This endpoint works the same way as the [Create new session](https://developers.vtex.com/docs/api-reference/session-manager-api#post-/api/sessions) endpoint, but when the request is sent with a `vtex_session` and the `vtex_segment` cookies in the header, it retrieves the session first and then applies the changes instead of generating a new one.  Only keys inside the `public` namespace in the request body are considered, and query par...

---
