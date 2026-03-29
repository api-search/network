---
aid: cloudflare:cloudflare-waiting-room-get-waiting-room-status
name: Get waiting room status
tags:
- - - - - - - Waiting Room
humanURL: 
properties: []
description: >-
  Fetches the status of a configured waiting room. Response fields include: 1. `status`: String indicating the status of the waiting room. The possible status are: 	- **not_queueing** indicates that the configured thresholds have not been met and all users are going through to the origin. 	- **queueing** indicates that the thresholds have been met and some users are held in the waiting room. 	- **event_prequeueing** indicates that an event is active and is currently prequeueing users before it ...

---
