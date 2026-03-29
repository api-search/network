---
aid: dropbox:dropbox-post-2-files-copy-batch-v2
name: copy_batch
tags:
- files
humanURL: 
properties: []
description: >-
  [copy_batch](https://www.dropbox.com/developers/documentation/http/documentation#files-copy_batch)  scope: `files.content.write`  Copy multiple files or folders to different locations at once in the user's Dropbox. This route will replace `copy_batch:1`. The main difference is this route will return status for each entry, while `copy_batch:1` raises failure if any entry fails. This route will either finish synchronously, or return a job ID and do the async copy job in background. Please use `...

---
