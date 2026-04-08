---
aid: tidb:tidb-resignddlowner
name: Resign DDL owner
tags:
- DDL
humanURL: 
properties: []
description: >-
  Forces the current TiDB server to resign its role as the DDL owner, triggering a new DDL owner election among all TiDB servers in the cluster. Only one TiDB server is the DDL owner at any time and is responsible for executing schema change jobs. Use this endpoint when the current DDL owner is experiencing issues.

---
