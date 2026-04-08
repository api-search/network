---
aid: sendgrid:sendgrid-listsegment
name: Get List of Segments
tags:
- Segmenting Contacts
humanURL: 
properties: []
description: >-
  **This endpoint allows you to retrieve a list of segments.**  The query param `parent_list_ids` is treated as a filter.  Any match will be returned.  Zero matches will return a response code of 200 with an empty `results` array.  `parent_list_ids` | `no_parent_list_id` | `ids` | `result` -----------------:|:--------------------:|:-------------:|:-------------: empty | false | empty | all segments values list_ids | false | empty | segments filtered by list_ids values list_ids |true | empty | s...

---
