---
aid: box:box-get-events
name: List user and enterprise events
tags:
- - - - Events
humanURL: 
properties: []
description: >-
  Returns up to a year of past events for a given user or for the entire enterprise.  By default this returns events for the authenticated user. To retrieve events for the entire enterprise, set the `stream_type` to `admin_logs_streaming` for live monitoring of new events, or `admin_logs` for querying across historical events. The user making the API call will need to have admin privileges, and the application will need to have the scope `manage enterprise properties` checked.

---
