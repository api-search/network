---
class_count: 9
classes:
- CreateTrailRequest
- name
- CreateTrailResponse
- DescribeTrailsResponse
- LookupEventsRequest
- LookupEventsResponse
- CreateEventDataStoreRequest
- CreateEventDataStoreResponse
- ListEventDataStoresResponse
context_file: json-ld/amazon-cloudtrail-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-cloudtrail/refs/heads/main/json-ld/amazon-cloudtrail-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Cloudtrail from Amazon CloudTrail.
layout: jsonld
name: Amazon Cloudtrail Context
namespaces:
- prefix: cloudtrail
  uri: https://aws.amazon.com/cloudtrail/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: s3BucketName
  type: string
- container: ''
  name: s3KeyPrefix
  type: string
- container: ''
  name: isMultiRegionTrail
  type: boolean
- container: ''
  name: enableLogFileValidation
  type: boolean
- container: ''
  name: cloudWatchLogsLogGroupArn
  type: string
- container: ''
  name: cloudWatchLogsRoleArn
  type: string
- container: ''
  name: trailARN
  type: string
- container: ''
  name: logFileValidationEnabled
  type: boolean
- container: set
  name: trailList
  type: string
- container: set
  name: lookupAttributes
  type: string
- container: ''
  name: startTime
  type: dateTime
- container: ''
  name: endTime
  type: dateTime
- container: ''
  name: maxResults
  type: integer
- container: ''
  name: nextToken
  type: string
- container: set
  name: events
  type: string
- container: ''
  name: retentionPeriod
  type: integer
- container: ''
  name: multiRegionEnabled
  type: boolean
- container: ''
  name: eventDataStoreArn
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: createdTimestamp
  type: dateTime
- container: set
  name: eventDataStores
  type: string
property_count: 21
provider_name: Amazon CloudTrail
provider_slug: amazon-cloudtrail
slug: amazon-cloudtrail-context
tags:
- AWS
- CloudTrail
- Audit
- Compliance
- Governance
- Security
- JSON-LD
- Linked Data
- Semantic Web
---
