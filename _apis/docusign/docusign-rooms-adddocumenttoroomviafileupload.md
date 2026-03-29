---
aid: docusign:docusign-rooms-adddocumenttoroomviafileupload
name: Uploads the contents of a file as a document to a room.
tags:
- Rooms
humanURL: 
properties: []
description: >-
  This method uploads the contents of file as a room document for the room that you specify.  This is a multipart form request. You must include the following headers:  - `Content-Type: multipart/form-data` (with a `boundary`) - `Content-Disposition: form-data` - `Content-Disposition: file` (with the `filename`)   ### Related topics  - [How to attach documents via binary transfer (eSignature)](/docs/esign-rest-api/how-to/send-binary/)   An eSignature API example that illustrates how to build a ...

---
