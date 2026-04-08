---
aid: tyk:tyk-hotreloadgroup
name: Hot-reload a group of Tyk nodes.
tags:
- Hot Reload
humanURL: 
properties: []
description: >-
  To reload a whole group of Tyk nodes (without using the Dashboard or host manager). You can send an API request to a single node, this node will then send a notification through the pub/sub infrastructure to all other listening nodes (including the host manager if it is being used to manage Nginx) which will then trigger a global reload.

---
