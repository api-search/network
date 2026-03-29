---
aid: amazon-web-services:amazon-web-services-amazonwebservicesputrecord
name: Putrecord
tags:
- API
humanURL: 
properties: []
description: >-
  The PutRecord API is used to ingest a list of Records into your feature group.  If a new record’s EventTime is greater, the new record is written to both the OnlineStore and OfflineStore. Otherwise, the record is a historic record and it is written only to the OfflineStore.  You can specify the ingestion to be applied to the OnlineStore, OfflineStore, or both by using the TargetStores request parameter.  You can set the ingested record to expire at a given time to live (TTL) duration after th...

---
