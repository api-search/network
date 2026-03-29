---
aid: etcd:etcd-watchevents
name: Watch for key change events
tags:
- Watch
humanURL: 
properties: []
description: >-
  Opens a streaming watch connection to receive notifications of key-value changes in the etcd cluster. Clients send WatchCreateRequest messages to subscribe to key ranges and WatchCancelRequest messages to unsubscribe. The server streams WatchResponse messages containing events that describe each key change including the event type (PUT or DELETE) and the updated key-value pair. Watches can be started from a specific revision to receive historical events.

---
