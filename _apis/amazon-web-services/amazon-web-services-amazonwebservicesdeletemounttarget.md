---
aid: amazon-web-services:amazon-web-services-amazonwebservicesdeletemounttarget
name: Deletemounttarget
tags:
- API
humanURL: 
properties: []
description: >-
  Deletes the specified mount target. This operation forcibly breaks any mounts of the file system by using the mount target that is being deleted, which might disrupt instances or applications using those mounts. To avoid applications getting cut off abruptly, you might consider unmounting any mounts of the mount target, if feasible. The operation also deletes the associated network interface. Uncommitted writes might be lost, but breaking a mount target using this operation does not corrupt t...

---
