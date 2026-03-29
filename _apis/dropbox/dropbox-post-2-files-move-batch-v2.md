---
aid: dropbox:dropbox-post-2-files-move-batch-v2
name: move_batch
tags:
- files
humanURL: 
properties: []
description: >-
  [move_batch](https://www.dropbox.com/developers/documentation/http/documentation#files-move_batch)  scope: `files.content.write`  Move multiple files or folders to different locations at once in the user's Dropbox. Note that we do not currently support case-only renaming. This route will replace `move_batch:1`. The main difference is this route will return status for each entry, while `move_batch:1` raises failure if any entry fails. This route will either finish synchronously, or return a jo...

---
