---
aid: factset:factset-postfundamentals
name: Returns company fundamental data for a list of identifiers.
tags:
- Financial Statements
humanURL: 
properties: []
description: >-
  Retrieves FactSet Fundamental standardized data for specified securities using a POST request body. Use the `/metrics` endpoint to retrieve a full list of valid metrics or data items.  The `/fundamentals` endpoint currently supports Long Running asynchronous requests up to **20 minutes** via batch parameter. Id limits are increased to 30,000 ids per request when using batch capability. This 30,000 id limit has been derived based on single metric for one day.

---
