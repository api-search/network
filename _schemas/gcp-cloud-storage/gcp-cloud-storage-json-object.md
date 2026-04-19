---
description: An object in Cloud Storage. Objects are the individual pieces of data that you store in Cloud Storage.
layout: schema
name: Object
properties_list:
- description: The kind of item this is. For objects, this is always storage#object.
  name: kind
  type: string
- description: The ID of the object, including the bucket name, object name, and generation number.
  name: id
  type: string
- description: The link to this object.
  name: selfLink
  type: string
- description: The link to download the object's data.
  name: mediaLink
  type: string
- description: The name of the object.
  name: name
  type: string
- description: The name of the bucket containing this object.
  name: bucket
  type: string
- description: The content generation of this object. Used for object versioning.
  name: generation
  type: string
- description: The version of the metadata for this object. Used for preconditions and detecting metadata changes.
  name: metageneration
  type: string
- description: Content-Type of the object data.
  name: contentType
  type: string
- description: The creation time of the object in RFC 3339 format.
  name: timeCreated
  type: string
- description: The modification time of the object metadata in RFC 3339 format.
  name: updated
  type: string
- description: The deletion time of the object in RFC 3339 format. Set only when the object is noncurrent.
  name: timeDeleted
  type: '[''string'', ''null'']'
- description: Whether the object is under a temporary hold.
  name: temporaryHold
  type: boolean
- description: Whether the object is under an event-based hold.
  name: eventBasedHold
  type: boolean
- description: The earliest time that the object can be deleted or replaced, based on the retention policy.
  name: retentionExpirationTime
  type: '[''string'', ''null'']'
- description: Storage class of the object.
  name: storageClass
  type: string
- description: The time at which the object's storage class was last changed.
  name: timeStorageClassUpdated
  type: string
- description: Content-Length of the data in bytes.
  name: size
  type: string
- description: MD5 hash of the data, encoded using base64. Not available for composite objects.
  name: md5Hash
  type: string
- description: CRC32c checksum, encoded using base64.
  name: crc32c
  type: string
- description: HTTP 1.1 Entity tag for the object.
  name: etag
  type: string
- description: Number of underlying components that make up a composite object.
  name: componentCount
  type: integer
- description: Content-Encoding of the object data.
  name: contentEncoding
  type: string
- description: Content-Disposition of the object data.
  name: contentDisposition
  type: string
- description: Content-Language of the object data.
  name: contentLanguage
  type: string
- description: Cache-Control directive for the object data.
  name: cacheControl
  type: string
- description: User-provided metadata in key/value pairs.
  name: metadata
  type: object
- description: Access controls on the object.
  name: acl
  type: array
- description: The owner of the object.
  name: owner
  type: object
- description: Metadata of customer-supplied encryption key, if the object is encrypted by such a key.
  name: customerEncryption
  type: object
- description: Cloud KMS key used to encrypt the object, if one has been specified.
  name: kmsKeyName
  type: string
- description: A timestamp in RFC 3339 format specified by the user for an object. Typically set to enable lifecycle management conditions based on custom time.
  name: customTime
  type: string
- description: The time at which the object was soft-deleted, if applicable.
  name: softDeleteTime
  type: '[''string'', ''null'']'
- description: The time at which the soft-deleted object will be permanently deleted.
  name: hardDeleteTime
  type: '[''string'', ''null'']'
provider_name: Google Cloud Storage
provider_slug: gcp-cloud-storage
schema_file: json-schema/gcp-cloud-storage-json-object-schema.json
slug: gcp-cloud-storage-json-object
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
title: Object
---
