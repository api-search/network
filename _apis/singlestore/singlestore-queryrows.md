---
aid: singlestore:singlestore-queryrows
name: Execute a SQL query and return rows
tags:
- Queries
humanURL: 
properties: []
description: >-
  Executes a SQL SELECT statement against the target workspace and database, returning results as an array of JSON objects where each object represents one row with column names as keys. This format is convenient for most use cases but produces larger responses than the tuples format due to the repeated column name keys. The request body must not exceed 1 MB in size.

---
