---
aid: hashicorp:hashicorp-postsysstepdown
name: Cause the node to give up active status.
tags:
- system
humanURL: 
properties: []
description: >-
  This endpoint forces the node to give up active status. If the node does not have active status, this endpoint does nothing. Note that the node will sleep for ten seconds before attempting to grab the active lock again, but if no standby nodes grab the active lock in the interim, the same node may become the active node again.

---
