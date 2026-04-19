---
description: CreateSbomExportRequest schema
layout: schema
name: CreateSbomExportRequest
properties_list:
- description: ''
  name: reportFormat
  type: object
- description: ''
  name: resourceFilterCriteria
  type: object
- description: Contains details of the Amazon S3 bucket and KMS key used to export findings.
  name: s3Destination
  type: object
provider_name: Amazon Inspector
provider_slug: amazon-inspector
schema_file: json-schema/inspector-create-sbom-export-request-schema.json
slug: inspector-create-sbom-export-request
tags:
- AWS
- Compliance
- Container Security
- EC2
- Lambda
- Security
- Vulnerability Scanning
title: CreateSbomExportRequest
---
