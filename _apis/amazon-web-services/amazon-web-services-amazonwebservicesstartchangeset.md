---
aid: amazon-web-services:amazon-web-services-amazonwebservicesstartchangeset
name: Startchangeset
tags:
- API
humanURL: 
properties: []
description: >-
  Allows you to request changes for your entities. Within a single ChangeSet, you can't start the same change type against the same entity multiple times. Additionally, when a ChangeSet is running, all the entities targeted by the different changes are locked until the change set has completed (either succeeded, cancelled, or failed). If you try to start a change set containing a change against an entity that is already locked, you will receive a ResourceInUseException error. For example, you c...

---
