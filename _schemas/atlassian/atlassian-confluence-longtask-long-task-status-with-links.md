---
description: 'Same as LongTaskStatus but with `_links` property. Status keys: - `ERROR_UNKNOWN` - Generic error - `ERROR_LOCK_FAILED` - Could not get the lock on destination space - `ERROR_RELINK` - Error when relink pages/attachments - `ERROR_COPY_PAGE` - Error while copying 1 page - `WARN_RENAME_PAGE` - Warning page is rename during copy - `WARN_IGNORE_COPY_PERMISSION` - Warning could not copy permission - `WARN_IGNORE_COPY_ATTACHMENT` - Warning could not copy attachment - `WARN_IGNORE_DELETE_PAGE` - Warning ignoring delete of a non agreed on page - `STATUS_COPIED_PAGES` - Message total pages are copied - `STATUS_COPYING_PAGES` - Message copy pages - `STATUS_RELINK_PAGES` - Message relink pages/attachments - `STATUS_DELETING_PAGES` - Message delete pages - `STATUS_DELETED_PAGES` - Message total pages are deleted - `STATUS_MOVING_PAGES` - Message move pages - `WARN_IGNORE_VIEW_RESTRICTED` - Permission changed - view restricted - `WARN_IGNORE_EDIT_RESTRICTED` - Permission changed - edit
  restricted - `INITIALIZING_TASK` - Message when initializing task - `UNKNOWN_STATUS` - Message when status is unknown'
layout: schema
name: LongTaskStatusWithLinks
properties_list:
- description: the ARI for the long task, based on its ID
  name: ari
  type: string
- description: ''
  name: id
  type: string
- description: ''
  name: name
  type: object
- description: ''
  name: elapsedTime
  type: integer
- description: ''
  name: percentageComplete
  type: integer
- description: ''
  name: successful
  type: boolean
- description: ''
  name: finished
  type: boolean
- description: ''
  name: messages
  type: array
- description: ''
  name: status
  type: string
- description: ''
  name: errors
  type: array
- description: ''
  name: additionalDetails
  type: object
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-confluence-longtask-long-task-status-with-links-schema.json
slug: atlassian-confluence-longtask-long-task-status-with-links
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: LongTaskStatusWithLinks
---
