---
aid: sendgrid:sendgrid-searchrecipient
name: Search recipients
tags:
- Recipients
humanURL: 
properties: []
description: >-
  Search using segment conditions without actually creating a segment. Body contains a JSON object with `conditions`, a list of conditions as described below, and an optional `list_id`, which is a valid list ID for a list to limit the search on.  Valid operators for create and update depend on the type of the field for which you are searching.  - Dates:   - `"eq"`, `"ne"`, `"lt"` (before), `"gt"` (after)     - You may use MM/DD/YYYY for day granularity or an epoch for second granularity.   - `"...

---
