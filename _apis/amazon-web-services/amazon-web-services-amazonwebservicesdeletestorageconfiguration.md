---
aid: amazon-web-services:amazon-web-services-amazonwebservicesdeletestorageconfiguration
name: Deletestorageconfiguration
tags:
- API
humanURL: 
properties: []
description: >-
  Deletes the storage configuration for the specified ARN. If you try to delete a storage configuration that is used by a Composition, you will get an error (409 ConflictException). To avoid this, for all Compositions that reference the storage configuration, first use StopComposition and wait for it to complete, then use DeleteStorageConfiguration.

---
