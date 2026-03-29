---
aid: dynatrace:dynatrace-ingestlogs
name: Ingest log records
tags:
- Logs
humanURL: 
properties: []
description: >-
  Ingests log records into the Dynatrace Grail data lakehouse. Accepts an array of log record objects. Each record must include at least a content field (the log message). Additional fields such as severity, timestamp, and entity associations can be included. Log records are processed asynchronously. Requires the logs.ingest API token scope.

---
