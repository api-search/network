---
aid: neo4j:neo4j-opentransaction
name: Open a new explicit transaction
tags:
- Transactions
humanURL: 
properties: []
description: >-
  Opens a new explicit transaction on the specified database. The response includes the transaction location URI which contains the transaction ID needed for subsequent operations. Optionally, Cypher statements can be included in the request body to be executed as part of the transaction opening. Transactions expire automatically after a period of inactivity with a default timeout of 30 seconds, configurable via server.http.transaction_idle_timeout.

---
