---
description: Describes Network File System (NFS) file share default values. Files and folders stored as Amazon S3 objects in S3 buckets don't, by default, have Unix file permissions assigned to them. Upon discovery in an S3 bucket by Storage Gateway, the S3 objects that represent files and folders are assigned these default Unix permissions. This operation is only supported for S3 File Gateways.
layout: schema
name: NFSFileShareDefaults
properties_list:
- description: ''
  name: FileMode
  type: object
- description: ''
  name: DirectoryMode
  type: object
- description: ''
  name: GroupId
  type: object
- description: ''
  name: OwnerId
  type: object
provider_name: Amazon Storage Gateway
provider_slug: amazon-storage-gateway
schema_file: json-schema/amazon-storage-gateway-nfs-file-share-defaults-schema.json
slug: amazon-storage-gateway-nfs-file-share-defaults
tags:
- AWS
- Backup
- File Storage
- Gateway
- Hybrid Cloud
- Storage
title: NFSFileShareDefaults
---
