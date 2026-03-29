---
aid: box:box-get-file-version-legal-holds
name: List file version legal holds
tags:
- - - - File version legal holds
humanURL: 
properties: []
description: >-
  Get a list of file versions on legal hold for a legal hold assignment.  Due to ongoing re-architecture efforts this API might not return all file versions for this policy ID.  Instead, this API will only return file versions held in the legacy architecture. Two new endpoints will available to request any file versions held in the new architecture.  For file versions held in the new architecture, the `GET /legal_hold_policy_assignments/:id/file_versions_on_hold` API can be used to return all p...

---
