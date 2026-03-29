---
aid: dropbox:dropbox-post-2-files-get-temporary-upload-link
name: get_temporary_upload_link
tags:
- files
humanURL: 
properties: []
description: >-
  [get_temporary_upload_link](https://www.dropbox.com/developers/documentation/http/documentation#files-get_temporary_upload_link)  scope: `files.content.write`  Get a one-time use temporary upload link to upload a file to a Dropbox location.  This endpoint acts as a delayed `upload`. The returned temporary upload link may be used to make a POST request with the data to be uploaded. The upload will then be perfomed with the `CommitInfo` previously provided to `get_temporary_upload_link` but eva...

---
