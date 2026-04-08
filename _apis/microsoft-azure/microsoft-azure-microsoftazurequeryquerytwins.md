---
aid: microsoft-azure:microsoft-azure-microsoftazurequeryquerytwins
name: Microsoft Azure Post Query
tags:
- Query
humanURL: 
properties: []
description: >-
  Executes a query that allows traversing relationships and filtering by property values.<br>Status codes:<br>* 200 OK<br>* 400 Bad Request<br>  * BadRequest - The continuation token is invalid.<br>  * SqlQueryError - The query contains some errors.<br>  * TimeoutError - The query execution timed out after 60 seconds. Try simplifying the query or adding conditions to reduce the result size.<br> * 429 Too Many Requests<br>  * QuotaReachedError - The maximum query rate limit has been reached.

---
