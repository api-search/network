---
class_count: 9
classes:
- ObjectSummary
- BucketSummary
- UpdateBucketDetails
- PreauthenticatedRequestSummary
- PreauthenticatedRequest
- Bucket
- ListObjects
- CreateBucketDetails
- CreatePreauthenticatedRequestDetails
context_file: json-ld/oracle-cloud-object-storage-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/json-ld/oracle-cloud-object-storage-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Oracle Cloud Object Storage from Oracle Cloud Infrastructure.
layout: jsonld
name: Oracle Cloud Object Storage Context
namespaces:
- prefix: oci
  uri: https://docs.oracle.com/en-us/iaas/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: accessType
  type: string
- container: ''
  name: accessUri
  type: string
- container: ''
  name: approximateCount
  type: integer
- container: ''
  name: approximateSize
  type: integer
- container: ''
  name: compartmentId
  type: string
- container: ''
  name: createdBy
  type: string
- container: ''
  name: definedTags
  type: ''
- container: ''
  name: etag
  type: string
- container: ''
  name: freeformTags
  type: ''
- container: ''
  name: id
  type: string
- container: ''
  name: md5
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: namespace
  type: string
- container: ''
  name: nextStartWith
  type: string
- container: ''
  name: objectEventsEnabled
  type: boolean
- container: ''
  name: objectLifecyclePolicyEtag
  type: string
- container: ''
  name: objectName
  type: string
- container: set
  name: objects
  type: reference
- container: set
  name: prefixes
  type: string
- container: ''
  name: publicAccessType
  type: string
- container: ''
  name: size
  type: integer
- container: ''
  name: storageTier
  type: string
- container: ''
  name: timeCreated
  type: dateTime
- container: ''
  name: timeExpires
  type: dateTime
- container: ''
  name: timeModified
  type: dateTime
- container: ''
  name: versioning
  type: string
property_count: 26
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
slug: oracle-cloud-object-storage-context
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
- JSON-LD
- Linked Data
- Semantic Web
---
