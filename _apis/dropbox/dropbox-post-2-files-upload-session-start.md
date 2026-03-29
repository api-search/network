---
aid: dropbox:dropbox-post-2-files-upload-session-start
name: upload_session/start
tags:
- files
humanURL: 
properties: []
description: >-
  [upload_session/start](https://www.dropbox.com/developers/documentation/http/documentation#files-upload_session-start)  scope: `files.content.write`  Upload sessions allow you to upload a single file in one or more requests, for example where the size of the file is greater than 150 MB.  This call starts a new upload session with the given data. You can then use `upload_session/append:2` to add more data and `upload_session/finish` to save all the data to a file in Dropbox. A single request s...

---
