---
aid: zluri:zluri-uploadsnapshotdata
name: Zluri Upload snapshot data
tags:
- Data Upload
humanURL: 
properties: []
description: >-
  Upload snapshot entity data within an active sync session. Snapshot data represents the current state of entities. Zluri compares new snapshots with the previous state to identify changes such as new users, deactivated users, and role changes. Data must be sent in paginated batches of up to 1000 records per page. Re-uploading a page with the same page number during an active sync will overwrite the previous data for that page. Supported entities include users, applications, contracts, and tra...

---
