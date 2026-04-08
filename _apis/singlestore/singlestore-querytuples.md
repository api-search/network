---
aid: singlestore:singlestore-querytuples
name: Execute a SQL query and return tuples
tags:
- Queries
humanURL: 
properties: []
description: >-
  Executes a SQL SELECT statement against the target workspace and database, returning results as a separate columns array and a rows array of value arrays. This format offers better performance for queries with large result sets because column names are not repeated per row. Use this endpoint when response payload size is a concern.

---
