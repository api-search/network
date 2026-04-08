---
aid: qdrant:qdrant-backupsrestorestatus
name: Qdrant Get restore process status
tags:
- Backups
humanURL: 
properties: []
description: >-
  Returns status of a backup restoration attempt for a set of classes. <br/><br/>All client implementations have a `wait for completion` option which will poll the backup status in the background and only return once the backup has completed (successfully or unsuccessfully). If you set the `wait for completion` option to false, you can also check the status yourself using the this endpoint.

---
