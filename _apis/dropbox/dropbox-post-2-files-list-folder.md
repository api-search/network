---
aid: dropbox:dropbox-post-2-files-list-folder
name: list_folder
tags:
- files
humanURL: 
properties: []
description: >-
  [list_folder](https://www.dropbox.com/developers/documentation/http/documentation#files-list_folder)  scope: `files.metadata.read`  Starts returning the contents of a folder. If the result's `ListFolderResult.has_more` field is `true`, call `list_folder/continue` with the returned `ListFolderResult.cursor` to retrieve more entries. If you're using `ListFolderArg.recursive` set to `true` to keep a local cache of the contents of a Dropbox account, iterate through each entry in order and process...

---
