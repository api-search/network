---
aid: qdrant:qdrant-batchobjectsdelete
name: Qdrant Batch delete objects.
tags:
- Batch
humanURL: 
properties: []
description: >-
  Batch delete objects that match a particular filter. <br/><br/>The request body takes a single `where` filter and will delete all objects matched. <br/><br/>Note that there is a limit to the number of objects to be deleted at once using this filter, in order to protect against unexpected memory surges and very-long-running requests. The default limit is 10,000 and may be configured by setting the `QUERY_MAXIMUM_RESULTS` environment variable. <br/><br/>Objects are deleted in the same order tha...

---
