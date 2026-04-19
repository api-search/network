---
description: Schema for a Google Cloud Storage bucket resource as returned by the Cloud Storage JSON API v1. A bucket is a container for objects stored in Cloud Storage. Buckets are associated with a project, have globally unique names, and provide configuration for storage class, location, access control, lifecycle management, versioning, and encryption.
layout: schema
name: Google Cloud Storage Bucket
properties_list:
- description: The kind of item this is. For buckets, this is always storage#bucket.
  name: kind
  type: string
- description: The ID of the bucket. For buckets, this is the same value as the name property. Read-only.
  name: id
  type: string
- description: The URI of this bucket. Read-only.
  name: selfLink
  type: string
- description: The project number of the project the bucket belongs to. Read-only.
  name: projectNumber
  type: string
- description: The name of the bucket. Bucket names must be globally unique across all of Cloud Storage, contain only lowercase letters, numbers, hyphens, underscores, and dots, and must be between 3 and 63 characte
  name: name
  type: string
- description: The creation time of the bucket in RFC 3339 format. Read-only.
  name: timeCreated
  type: string
- description: The modification time of the bucket metadata in RFC 3339 format. Read-only.
  name: updated
  type: string
- description: The metadata generation of this bucket. Used for preconditions and for detecting changes in metadata. Every update to the bucket's metadata increments this value. Read-only.
  name: metageneration
  type: string
- description: 'The location of the bucket. Object data for objects in the bucket resides in physical storage within this region. Can be a multi-region (e.g., US, EU, ASIA), dual-region (e.g., US-EAST1+US-WEST1), or '
  name: location
  type: string
- description: The type of location that the bucket resides in. Read-only.
  name: locationType
  type: string
- description: The default storage class of the bucket, used for newly created objects when no storage class is specified. Objects can be stored in Standard, Nearline, Coldline, or Archive storage.
  name: storageClass
  type: string
- description: HTTP 1.1 Entity tag for the bucket. Read-only.
  name: etag
  type: string
- description: Whether or not to automatically apply an event-based hold to new objects added to the bucket. Event-based holds remain on an object until explicitly removed.
  name: defaultEventBasedHold
  type: boolean
- description: The Recovery Point Objective (RPO) of this bucket. Set to ASYNC_TURBO to enable Turbo Replication on dual-region buckets, providing a lower RPO of 15 minutes instead of the default.
  name: rpo
  type: string
- description: Access controls on the bucket, containing one or more bucketAccessControls resources. Not returned in list responses unless projection=full is specified.
  name: acl
  type:
  - array
  - 'null'
- description: Default access controls to apply to new objects when no ACL is provided.
  name: defaultObjectAcl
  type:
  - array
  - 'null'
- description: ''
  name: iamConfiguration
  type: object
- description: Encryption configuration for the bucket. Specifies a default Cloud KMS key for encrypting objects inserted into this bucket.
  name: encryption
  type:
  - object
  - 'null'
- description: The bucket's lifecycle configuration. Lifecycle management lets you set a Time to Live (TTL) for objects, or automatically transition objects to different storage classes based on conditions.
  name: lifecycle
  type:
  - object
  - 'null'
- description: The bucket's logging configuration, which defines the destination bucket and optional name prefix for the current bucket's access logs.
  name: logging
  type:
  - object
  - 'null'
- description: The bucket's versioning configuration. When enabled, Cloud Storage retains a noncurrent object version each time a live object version is replaced or deleted.
  name: versioning
  type:
  - object
  - 'null'
- description: The bucket's website configuration, controlling how the service behaves when accessing bucket contents as a web site.
  name: website
  type:
  - object
  - 'null'
- description: The bucket's Cross-Origin Resource Sharing (CORS) configuration to support requests from web applications running in browsers.
  name: cors
  type:
  - array
  - 'null'
- description: The bucket's retention policy, which defines the minimum age an object in the bucket must reach before it can be deleted or replaced.
  name: retentionPolicy
  type:
  - object
  - 'null'
- description: The bucket's soft delete policy. When enabled, deleted objects are retained for a specified period and can be recovered.
  name: softDeletePolicy
  type:
  - object
  - 'null'
- description: The bucket's Autoclass configuration. When enabled, Autoclass automatically transitions objects in the bucket to appropriate storage classes based on each object's access pattern.
  name: autoclass
  type:
  - object
  - 'null'
- description: The bucket's hierarchical namespace configuration. When enabled, the bucket supports folders and managed folders as organizational structures.
  name: hierarchicalNamespace
  type:
  - object
  - 'null'
- description: User-provided labels, in key/value pairs. Labels are used to organize and filter buckets. Keys and values must be 63 characters or less and conform to RFC 1035.
  name: labels
  type:
  - object
  - 'null'
- description: The bucket's custom placement configuration for Custom Dual Regions.
  name: customPlacementConfig
  type:
  - object
  - 'null'
- description: Whether the bucket satisfies zone separation requirements. Read-only.
  name: satisfiesPZS
  type: boolean
provider_name: Google Cloud Storage
provider_slug: gcp-cloud-storage
schema_file: json-schema/gcp-cloud-storage-bucket-schema.json
slug: gcp-cloud-storage-bucket
tags:
- Archival
- Backup
- Blob Storage
- Cloud Storage
- Data
- File Storage
- Google Cloud
- Object Storage
- Storage
title: Google Cloud Storage Bucket
---
