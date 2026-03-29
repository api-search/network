---
aid: dropbox:dropbox-post-2-sharing-share-folder
name: share_folder
tags:
- sharing
humanURL: 
properties: []
description: >-
  [share_folder](https://www.dropbox.com/developers/documentation/http/documentation#sharing-share_folder)  scope: `sharing.write`  Share a folder with collaborators. Most sharing will be completed synchronously. Large folders will be completed asynchronously. To make testing the async case repeatable, set `ShareFolderArg.force_async`. If a `ShareFolderLaunch.async_job_id` is returned, you'll need to call `check_share_job_status` until the action completes to get the metadata for the folder.

---
