---
aid: atlassian:atlassian-atlassiangetidsofworklogsmodifiedsince
name: Get Ids Of Updated Worklogs
tags:
- Issue worklogs
humanURL: 
properties: []
description: >-
  Returns a list of IDs and update timestamps for worklogs updated after a date and time.<br><br>This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from oldest to youngest. If the number of items in the date range exceeds 1000, `until` indicates the timestamp of the youngest item on the page. Also, `nextPage` provides the URL for the next page of worklogs. The `lastPage` parameter is set to true on the last page of worklogs.<br><br>This resource does no...

---
