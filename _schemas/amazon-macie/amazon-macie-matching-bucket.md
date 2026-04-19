---
description: <p>Provides statistical data and other information about an S3 bucket that Amazon Macie monitors and analyzes for your account. By default, object count and storage size values include data for object parts that are the result of incomplete multipart uploads. For more information, see <a href="https://docs.aws.amazon.com/macie/latest/user/monitoring-s3-how-it-works.html">How Macie monitors Amazon S3 data security</a> in the <i>Amazon Macie User Guide</i>.</p> <p>If an error occurs when Macie attempts to retrieve and process information about the bucket or the bucket's objects, the value for most of these properties is null. Key exceptions are accountId and bucketName. To identify the cause of the error, refer to the errorCode and errorMessage values.</p>
layout: schema
name: MatchingBucket
properties_list:
- description: ''
  name: accountId
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
  name: objectCount
  type: object
- description: ''
  name: objectCountByEncryptionType
  type: object
- description: ''
  name: sensitivityScore
  type: object
- description: ''
  name: sizeInBytes
  type: object
- description: ''
  name: sizeInBytesCompressed
  type: object
- description: ''
  name: unclassifiableObjectCount
  type: object
- description: ''
  name: unclassifiableObjectSizeInBytes
  type: object
provider_name: Amazon Macie
provider_slug: amazon-macie
schema_file: json-schema/amazon-macie-matching-bucket-schema.json
slug: amazon-macie-matching-bucket
tags:
- AWS
- Data Security
- Sensitive Data
- Privacy
- Compliance
- Machine Learning
- S3
title: MatchingBucket
---
