---
aid: microsoft-azure:microsoft-azure-microsoftazurefilesystemdelete
name: Microsoft Azure Delete Filesystem
tags:
- Filesystem Operations
humanURL: 
properties: []
description: >-
  Marks the filesystem for deletion.  When a filesystem is deleted, a filesystem with the same identifier cannot be created for at least 30 seconds. While the filesystem is being deleted, attempts to create a filesystem with the same identifier will fail with status code 409 (Conflict), with the service returning additional error information indicating that the filesystem is being deleted. All other operations, including operations on any files or directories within the filesystem, will fail wi...

---
