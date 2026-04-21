---
consumed_apis:
- efs
description: Unified capability for managing EFS file systems, mount targets, and access points for storage administrators.
layout: capability
name: Amazon EFS Elastic File System Management
operations:
- description: Amazon EFS Describe File Systems
  method: GET
  name: describeFileSystems
  path: /v1/2015-02-01/file-systems
- description: Amazon EFS Create File System
  method: POST
  name: createFileSystem
  path: /v1/2015-02-01/file-systems
- description: Amazon EFS Delete File System
  method: DELETE
  name: deleteFileSystem
  path: /v1/2015-02-01/file-systems
- description: Amazon EFS Describe Mount Targets
  method: GET
  name: describeMountTargets
  path: /v1/2015-02-01/mount-targets
- description: Amazon EFS Create Mount Target
  method: POST
  name: createMountTarget
  path: /v1/2015-02-01/mount-targets
personas: []
provider_name: Amazon EFS
provider_slug: amazon-efs
search_terms:
- file system
- create mount target
- elastic file system
- describe file systems
- createFileSystem
- amazon efs create mount target
- file system management business domain for amazon efs.
- describeMountTargets
- file storage
- createMountTarget
- amazon efs describe mount targets
- serverless
- create file system
- delete file system
- describe mount targets
- nfs
- amazon efs
- storage
- amazon efs delete file system
- efs
- describeFileSystems
- amazon web services
- deleteFileSystem
- amazon efs create file system
- aws
- workflow capability for file system management.
- engineers managing amazon efs resources on aws.
- amazon efs describe file systems
slug: efs-management
tags:
- Amazon EFS
- AWS
- Storage
- File System
tools:
- description: Amazon EFS Describe File Systems
  hints:
    destructive: false
    readOnly: true
  name: describe-file-systems
- description: Amazon EFS Create File System
  hints:
    destructive: false
    readOnly: false
  name: create-file-system
- description: Amazon EFS Delete File System
  hints:
    destructive: true
    readOnly: false
  name: delete-file-system
- description: Amazon EFS Describe Mount Targets
  hints:
    destructive: false
    readOnly: true
  name: describe-mount-targets
- description: Amazon EFS Create Mount Target
  hints:
    destructive: false
    readOnly: false
  name: create-mount-target
---
