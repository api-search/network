---
description: Schema representing an Amazon S3 object. An object is the fundamental entity stored in Amazon S3. Objects consist of object data and metadata. The metadata is a set of name-value pairs that describe the object. An object is uniquely identified within a bucket by a key (name) and a version ID.
layout: schema
name: Amazon S3 Object
properties_list:
- description: The name that you assign to an object. The object key is used to retrieve the object. Object keys can be up to 1,024 bytes long and can contain any UTF-8 character.
  name: Key
  type: string
- description: The name of the bucket that contains the object.
  name: BucketName
  type: string
- description: Size of the object in bytes. The maximum size of an individual object is 5 TiB.
  name: Size
  type: integer
- description: The entity tag is an opaque identifier assigned by a web server to a specific version of a resource. For objects not uploaded as multipart, the ETag is the MD5 digest of the object. For multipart uplo
  name: ETag
  type: string
- description: The date and time at which the object was last modified.
  name: LastModified
  type: string
- description: Version ID of the object. When versioning is enabled on a bucket, Amazon S3 assigns a version number to each object added to the bucket.
  name: VersionId
  type: string
- description: The storage class of the object. Amazon S3 offers a range of storage classes designed for different use cases.
  name: StorageClass
  type: string
- description: The owner of the object.
  name: Owner
  type: object
- description: A standard MIME type describing the format of the object data.
  name: ContentType
  type: string
- description: Size of the body in bytes.
  name: ContentLength
  type: integer
- description: Specifies what content encodings have been applied to the object.
  name: ContentEncoding
  type: string
- description: The language the content is in.
  name: ContentLanguage
  type: string
- description: Specifies presentational information for the object.
  name: ContentDisposition
  type: string
- description: Specifies caching behavior along the request/reply chain.
  name: CacheControl
  type: string
- description: The date and time at which the object is no longer cacheable.
  name: Expires
  type: string
- description: A map of metadata to store with the object in S3. User-defined metadata keys must begin with x-amz-meta-.
  name: Metadata
  type: object
- description: The server-side encryption algorithm used when storing this object in Amazon S3.
  name: ServerSideEncryption
  type: string
- description: If present, specifies the ID of the AWS KMS symmetric encryption customer managed key that was used for the object.
  name: SSEKMSKeyId
  type: string
- description: If server-side encryption with a customer-provided encryption key was requested, the response will include this header to confirm the encryption algorithm used.
  name: SSECustomerAlgorithm
  type: string
- description: Indicates whether the object uses an S3 Bucket Key for server-side encryption with AWS KMS (SSE-KMS).
  name: BucketKeyEnabled
  type: boolean
- description: The algorithm that was used to create a checksum of the object.
  name: ChecksumAlgorithm
  type: string
- description: The base64-encoded, 32-bit CRC32 checksum of the object.
  name: ChecksumCRC32
  type: string
- description: The base64-encoded, 32-bit CRC32C checksum of the object.
  name: ChecksumCRC32C
  type: string
- description: The base64-encoded, 160-bit SHA-1 digest of the object.
  name: ChecksumSHA1
  type: string
- description: The base64-encoded, 256-bit SHA-256 digest of the object.
  name: ChecksumSHA256
  type: string
- description: The Object Lock mode currently in place for this object.
  name: ObjectLockMode
  type: string
- description: The date and time when the Object Lock retention period expires.
  name: ObjectLockRetainUntilDate
  type: string
- description: Indicates whether the object has a legal hold in place.
  name: ObjectLockLegalHoldStatus
  type: string
- description: Amazon S3 can return this if your request involves a bucket that is either a source or destination in a replication rule.
  name: ReplicationStatus
  type: string
- description: Specifies whether the object is a delete marker (versioning enabled buckets only).
  name: IsDeleteMarker
  type: boolean
- description: If the object expiration is configured, the response includes this header with the expiry-date and rule-id key-value pairs.
  name: Expiration
  type: string
- description: Provides information about object restoration action and expiration time of the restored object copy.
  name: Restore
  type: string
- description: The number of tags, if any, on the object.
  name: TagCount
  type: integer
- description: The tag-set associated with the object. Maximum of 10 tags per object.
  name: Tags
  type: array
- description: Access control list for the object.
  name: ACL
  type: object
- description: The count of parts this object has. This value is only returned if you specify partNumber in your request and the object was uploaded as a multipart upload.
  name: PartsCount
  type: integer
- description: This is set to the number of metadata entries not returned in x-amz-meta headers. This can happen if you create metadata using an API like SOAP that supports more flexible metadata than the REST API.
  name: MissingMeta
  type: integer
- description: If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL.
  name: WebsiteRedirectLocation
  type: string
- description: Indicates that a range of bytes was specified.
  name: AcceptRanges
  type: string
provider_name: Amazon S3
provider_slug: amazon-s3
schema_file: json-schema/amazon-s3-object-schema.json
slug: amazon-s3-object
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
title: Amazon S3 Object
---
