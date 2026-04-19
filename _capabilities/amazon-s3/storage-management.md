---
consumed_apis:
- s3-rest
- s3-control
- s3-tables
description: Unified capability for Amazon S3 storage management combining object storage operations, account-level controls, and tabular data management. Used by cloud engineers, data engineers, and platform teams.
layout: capability
name: Amazon S3 Storage Management
operations:
- description: List all S3 buckets
  method: GET
  name: list-buckets
  path: /v1/buckets
- description: Create an S3 bucket
  method: POST
  name: create-bucket
  path: /v1/buckets
- description: Check if a bucket exists
  method: HEAD
  name: head-bucket
  path: /v1/buckets/{bucket}
- description: Delete an S3 bucket
  method: DELETE
  name: delete-bucket
  path: /v1/buckets/{bucket}
- description: List objects in a bucket
  method: GET
  name: list-objects
  path: /v1/buckets/{bucket}/objects
- description: Get an object
  method: GET
  name: get-object
  path: /v1/buckets/{bucket}/objects/{key}
- description: Upload an object
  method: PUT
  name: put-object
  path: /v1/buckets/{bucket}/objects/{key}
- description: Delete an object
  method: DELETE
  name: delete-object
  path: /v1/buckets/{bucket}/objects/{key}
- description: List S3 access points
  method: GET
  name: list-access-points
  path: /v1/access-points
- description: Get an access point
  method: GET
  name: get-access-point
  path: /v1/access-points/{name}
- description: List Batch Operations jobs
  method: GET
  name: list-jobs
  path: /v1/batch-jobs
- description: Create a Batch Operations job
  method: POST
  name: create-job
  path: /v1/batch-jobs
- description: Get details of a Batch Operations job
  method: GET
  name: describe-job
  path: /v1/batch-jobs/{id}
- description: List Storage Lens configurations
  method: GET
  name: list-storage-lens
  path: /v1/storage-lens
- description: List S3 table buckets
  method: GET
  name: list-table-buckets
  path: /v1/table-buckets
- description: List tables in a namespace
  method: GET
  name: list-tables
  path: /v1/table-buckets/{arn}/tables
personas: []
provider_name: Amazon S3
provider_slug: amazon-s3
search_terms:
- list storage lens configs
- single s3 bucket
- list s3 table buckets
- copy object
- copy an object within s3
- create job
- get bucket encryption
- list tables
- objects in a bucket
- head bucket
- create bucket
- describe batch job
- get details of an s3 table bucket
- create a new s3 bucket
- get versioning configuration for an s3 bucket
- list batch jobs
- list s3 storage lens configurations
- single object
- get details of a batch operations job
- data storage
- s3 buckets
- upload an object
- put object
- list all s3 buckets
- delete an object
- single access point
- list namespaces
- get encryption configuration for an s3 bucket
- check if a bucket exists
- s3
- list batch operations jobs
- get bucket lifecycle
- aws
- amazon
- list access points
- list buckets
- list storage lens
- s3 access points
- backup
- delete an s3 bucket
- storage lens configurations
- tables in a table bucket
- cloud storage
- list objects in a bucket
- object storage
- list table buckets
- get an access point
- get public access block settings for the account
- delete bucket
- list s3 batch operations jobs
- upload an object to s3
- get an object
- scalable storage
- archive
- get table
- list tables in a namespace
- get configuration of an s3 access point
- get lifecycle configuration for an s3 bucket
- delete object
- get access point
- list objects
- list all s3 buckets owned by the account
- get bucket versioning
- single batch operations job
- get table bucket
- get details of a table
- list namespaces in a table bucket
- list jobs
- create an s3 bucket
- list storage lens configurations
- retrieve an object from s3
- delete multiple objects from an s3 bucket
- storage management
- create a batch operations job
- list objects in an s3 bucket
- get object
- s3 batch operations jobs
- delete an object from s3
- list s3 access points
- delete objects
- describe job
- get public access block
- s3 table buckets
- list s3 access points for the account
slug: storage-management
tags:
- Amazon
- AWS
- S3
- Storage Management
- Cloud Storage
tools:
- description: List all S3 buckets owned by the account
  hints:
    openWorld: true
    readOnly: true
  name: list-buckets
- description: Create a new S3 bucket
  hints:
    readOnly: false
  name: create-bucket
- description: Delete an S3 bucket
  hints:
    destructive: true
    readOnly: false
  name: delete-bucket
- description: List objects in an S3 bucket
  hints:
    openWorld: true
    readOnly: true
  name: list-objects
- description: Retrieve an object from S3
  hints:
    readOnly: true
  name: get-object
- description: Upload an object to S3
  hints:
    readOnly: false
  name: put-object
- description: Delete an object from S3
  hints:
    destructive: true
    readOnly: false
  name: delete-object
- description: Copy an object within S3
  hints:
    readOnly: false
  name: copy-object
- description: Delete multiple objects from an S3 bucket
  hints:
    destructive: true
    readOnly: false
  name: delete-objects
- description: Get versioning configuration for an S3 bucket
  hints:
    readOnly: true
  name: get-bucket-versioning
- description: Get encryption configuration for an S3 bucket
  hints:
    readOnly: true
  name: get-bucket-encryption
- description: Get lifecycle configuration for an S3 bucket
  hints:
    readOnly: true
  name: get-bucket-lifecycle
- description: List S3 access points for the account
  hints:
    openWorld: true
    readOnly: true
  name: list-access-points
- description: Get configuration of an S3 access point
  hints:
    readOnly: true
  name: get-access-point
- description: List S3 Batch Operations jobs
  hints:
    openWorld: true
    readOnly: true
  name: list-batch-jobs
- description: Get details of a Batch Operations job
  hints:
    readOnly: true
  name: describe-batch-job
- description: List S3 Storage Lens configurations
  hints:
    openWorld: true
    readOnly: true
  name: list-storage-lens-configs
- description: Get public access block settings for the account
  hints:
    readOnly: true
  name: get-public-access-block
- description: List S3 table buckets
  hints:
    openWorld: true
    readOnly: true
  name: list-table-buckets
- description: Get details of an S3 table bucket
  hints:
    readOnly: true
  name: get-table-bucket
- description: List namespaces in a table bucket
  hints:
    openWorld: true
    readOnly: true
  name: list-namespaces
- description: List tables in a namespace
  hints:
    openWorld: true
    readOnly: true
  name: list-tables
- description: Get details of a table
  hints:
    readOnly: true
  name: get-table
---
