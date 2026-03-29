---
aid: docusign:docusign-rooms-revokeroomuseraccess
name: Revokes the specified user's access to the room.
tags:
- Rooms
humanURL: 
properties: []
description: >-
  Revokes the specified user's access to the room. If successful, the HTTP result is 204 (No content), and the response is empty.  To revoke access immediately, leave the request body empty.  To revoke access on a specific date, use the request body to specify a date.   **Note** If a user doesn't have access to a room, and you revoke their access at a future date, the user will be granted access until the revocation date.

---
