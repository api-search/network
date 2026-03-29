---
aid: box:box-get-files-id-trash
name: Get trashed file
tags:
- - - - Trashed files
humanURL: 
properties: []
description: >-
  Retrieves a file that has been moved to the trash.  Please note that only if the file itself has been moved to the trash can it be retrieved with this API call. If instead one of its parent folders was moved to the trash, only that folder can be inspected using the [`GET /folders/:id/trash`](e://get_folders_id_trash) API.  To list all items that have been moved to the trash, please use the [`GET /folders/trash/items`](e://get-folders-trash-items/) API.

---
