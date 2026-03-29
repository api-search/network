---
aid: box:box-post-files-id-content
name: Upload file version
tags:
- - - - Uploads
humanURL: 
properties: []
description: >-
  Update a file's content. For file sizes over 50MB we recommend using the Chunk Upload APIs.  # Request body order  The `attributes` part of the body must come **before** the `file` part. Requests that do not follow this format when uploading the file will receive a HTTP `400` error with a `metadata_after_file_contents` error code.

---
