---
description: A bucket is a container for objects stored in Cloud Storage. Buckets are associated with a project and have globally unique names.
layout: schema
name: Bucket
properties_list:
- description: The kind of item this is. For buckets, this is always storage#bucket.
  name: kind
  type: string
- description: The ID of the bucket. For buckets, this is the same as the name.
  name: id
  type: string
- description: The URI of this bucket.
  name: selfLink
  type: string
- description: The project number of the project the bucket belongs to.
  name: projectNumber
  type: string
- description: The name of the bucket. Bucket names must be globally unique and conform to naming requirements (3-63 characters, lowercase letters, numbers, hyphens, and dots).
  name: name
  type: string
- description: The creation time of the bucket in RFC 3339 format.
  name: timeCreated
  type: string
- description: The modification time of the bucket in RFC 3339 format.
  name: updated
  type: string
- description: The metadata generation of this bucket. Used for preconditions and for detecting changes in metadata.
  name: metageneration
  type: string
- description: The location of the bucket. Object data for objects in the bucket resides in physical storage within this region.
  name: location
  type: string
- description: The type of location the bucket resides in.
  name: locationType
  type: string
- description: The default storage class of the bucket, used for newly created objects.
  name: storageClass
  type: string
- description: HTTP 1.1 Entity tag for the bucket.
  name: etag
  type: string
- description: Whether or not to automatically apply an event-based hold to new objects added to the bucket.
  name: defaultEventBasedHold
  type: boolean
- description: The Recovery Point Objective (RPO) of this bucket. Set to ASYNC_TURBO to turn on Turbo Replication for dual-region buckets.
  name: rpo
  type: string
- description: Access controls on the bucket.
  name: acl
  type: array
- description: Default access controls to apply to new objects when no ACL is provided.
  name: defaultObjectAcl
  type: array
- description: The bucket's IAM configuration.
  name: iamConfiguration
  type: object
- description: Encryption configuration for a bucket.
  name: encryption
  type: object
- description: The bucket's lifecycle configuration. Lifecycle rules automatically manage objects based on conditions.
  name: lifecycle
  type: object
- description: The bucket's logging configuration.
  name: logging
  type: object
- description: The bucket's versioning configuration. When enabled, Cloud Storage retains a noncurrent object version when the live object is deleted or overwritten.
  name: versioning
  type: object
- description: The bucket's website configuration for static website hosting.
  name: website
  type: object
- description: The bucket's Cross-Origin Resource Sharing (CORS) configuration.
  name: cors
  type: array
- description: The bucket's retention policy, which defines the minimum age an object must reach before it can be deleted or replaced.
  name: retentionPolicy
  type: object
- description: The bucket's soft delete policy.
  name: softDeletePolicy
  type: object
- description: The bucket's Autoclass configuration. Autoclass automatically transitions objects to appropriate storage classes based on access patterns.
  name: autoclass
  type: object
- description: The bucket's hierarchical namespace configuration for folder support.
  name: hierarchicalNamespace
  type: object
- description: User-provided labels, in key/value pairs. Keys and values must both be 63 characters or less and must conform to RFC 1035.
  name: labels
  type: object
- description: The bucket's custom placement configuration for dual-region buckets.
  name: customPlacementConfig
  type: object
- description: Whether the bucket satisfies the zone separation requirements for compliance.
  name: satisfiesPZS
  type: boolean
provider_name: Google Cloud Storage
provider_slug: gcp-cloud-storage
schema_file: json-schema/gcp-cloud-storage-json-bucket-schema.json
slug: gcp-cloud-storage-json-bucket
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
title: Bucket
---
