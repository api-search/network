---
aid: dropbox:dropbox-post-2-files-create-folder-batch
name: create_folder_batch
tags:
- files
humanURL: 
properties: []
description: >-
  [create_folder_batch](https://www.dropbox.com/developers/documentation/http/documentation#files-create_folder_batch)  scope: `files.content.write`  Create multiple folders at once. This route is asynchronous for large batches, which returns a job ID immediately and runs the create folder batch asynchronously. Otherwise, creates the folders and returns the result synchronously for smaller inputs. You can force asynchronous behaviour by using the `CreateFolderBatchArg.force_async` flag.  Use `c...

---
