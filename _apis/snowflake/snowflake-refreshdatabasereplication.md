---
aid: snowflake:snowflake-refreshdatabasereplication
name: Refresh database replications.
tags:
- database
humanURL: 
properties: []
description: >-
  Refreshes a secondary database from a snapshot of its primary database. A snapshot includes changes to the objects and data. If you call this endpoint while another refresh for the same replica database is running, it fails and returns an error. Snowflake ensures only one refresh is executed at any given time.

---
