---
description: GetSbomExportResponse schema
layout: schema
name: GetSbomExportResponse
properties_list:
- description: ''
  name: errorCode
  type: object
- description: ''
  name: errorMessage
  type: object
- description: ''
  name: filterCriteria
  type: object
- description: ''
  name: format
  type: object
- description: ''
  name: reportId
  type: object
- description: Contains details of the Amazon S3 bucket and KMS key used to export findings.
  name: s3Destination
  type: object
- description: ''
  name: status
  type: object
provider_name: Amazon Inspector
provider_slug: amazon-inspector
schema_file: json-schema/inspector-get-sbom-export-response-schema.json
slug: inspector-get-sbom-export-response
tags:
- AWS
- Compliance
- Container Security
- EC2
- Lambda
- Security
- Vulnerability Scanning
title: GetSbomExportResponse
---
