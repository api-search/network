---
description: Container for the result of the ListObjectsV2 operation.
layout: schema
name: ListBucketResult
properties_list:
- description: Set to false if all of the results were returned. Set to true if more keys are available to return.
  name: IsTruncated
  type: boolean
- description: ''
  name: Contents
  type: array
- description: Bucket name.
  name: Name
  type: string
- description: Keys that begin with the indicated prefix.
  name: Prefix
  type: string
- description: Causes keys that contain the same string between the prefix and the first occurrence of the delimiter to be rolled up into a single result element.
  name: Delimiter
  type: string
- description: Sets the maximum number of keys returned in the response.
  name: MaxKeys
  type: integer
- description: ''
  name: CommonPrefixes
  type: array
- description: Encoding type used by Amazon S3 to encode object key names.
  name: EncodingType
  type: string
- description: The number of keys returned with this request.
  name: KeyCount
  type: integer
- description: If ContinuationToken was sent with the request, it is included in the response.
  name: ContinuationToken
  type: string
- description: NextContinuationToken is sent when isTruncated is true, which indicates that there are more keys to return.
  name: NextContinuationToken
  type: string
- description: If StartAfter was sent with the request, it is included in the response.
  name: StartAfter
  type: string
provider_name: Amazon S3
provider_slug: amazon-s3
schema_file: json-schema/amazon-s3-rest-list-bucket-result-schema.json
slug: amazon-s3-rest-list-bucket-result
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
title: ListBucketResult
---
