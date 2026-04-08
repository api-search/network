---
aid: neo4j:neo4j-executequery
name: Execute a Cypher query
tags:
- Query
humanURL: 
properties: []
description: >-
  Executes a Cypher query against the specified database using an implicit transaction. The server wraps the submitted Cypher query in a transaction automatically so that if any part of the query fails the database is reverted to its state before the query was executed. Multiple statements can be sent in a single request and the server runs them in sequence.

---
