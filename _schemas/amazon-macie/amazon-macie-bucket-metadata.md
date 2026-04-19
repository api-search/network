---
description: <p>Provides statistical data and other information about an S3 bucket that Amazon Macie monitors and analyzes for your account. By default, object count and storage size values include data for object parts that are the result of incomplete multipart uploads. For more information, see <a href="https://docs.aws.amazon.com/macie/latest/user/monitoring-s3-how-it-works.html">How Macie monitors Amazon S3 data security</a> in the <i>Amazon Macie User Guide</i>.</p> <p>If an error occurs when Macie attempts to retrieve and process metadata from Amazon S3 for the bucket or the bucket's objects, the value for the versioning property is false and the value for most other properties is null. Key exceptions are accountId, bucketArn, bucketCreatedAt, bucketName, lastUpdated, and region. To identify the cause of the error, refer to the errorCode and errorMessage values.</p>
layout: schema
name: BucketMetadata
properties_list:
- description: ''
  name: accountId
  type: object
- description: ''
  name: allowsUnencryptedObjectUploads
  type: object
- description: ''
  name: bucketArn
  type: object
- description: ''
  name: bucketCreatedAt
  type: object
- description: ''
  name: bucketName
  type: object
- description: ''
  name: classifiableObjectCount
  type: object
- description: ''
  name: classifiableSizeInBytes
  type: object
- description: ''
  name: errorCode
  type: object
- description: ''
  name: errorMessage
  type: object
- description: ''
  name: jobDetails
  type: object
- description: ''
  name: lastAutomatedDiscoveryTime
  type: object
- description: ''
  name: lastUpdated
  type: object
- description: ''
  name: objectCount
  type: object
- description: ''
  name: objectCountByEncryptionType
  type: object
- description: ''
  name: publicAccess
  type: object
- description: ''
  name: region
  type: object
- description: ''
  name: replicationDetails
  type: object
- description: ''
  name: sensitivityScore
  type: object
- description: ''
  name: serverSideEncryption
  type: object
- description: ''
  name: sharedAccess
  type: object
- description: ''
  name: sizeInBytes
  type: object
- description: ''
  name: sizeInBytesCompressed
  type: object
- description: ''
  name: tags
  type: object
- description: ''
  name: unclassifiableObjectCount
  type: object
- description: ''
  name: unclassifiableObjectSizeInBytes
  type: object
- description: ''
  name: versioning
  type: object
provider_name: Amazon Macie
provider_slug: amazon-macie
schema_file: json-schema/amazon-macie-bucket-metadata-schema.json
slug: amazon-macie-bucket-metadata
tags:
- AWS
- Data Security
- Sensitive Data
- Privacy
- Compliance
- Machine Learning
- S3
title: BucketMetadata
---
