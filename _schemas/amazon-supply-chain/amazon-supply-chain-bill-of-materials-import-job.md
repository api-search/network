---
description: A bill of materials import job
layout: schema
name: BillOfMaterialsImportJob
properties_list:
- description: The instance identifier
  name: instanceId
  type: string
- description: The job identifier
  name: jobId
  type: string
- description: The job status
  name: status
  type: string
- description: The S3 URI of the import file
  name: s3uri
  type: string
- description: Status message
  name: message
  type: string
provider_name: Amazon Supply Chain
provider_slug: amazon-supply-chain
schema_file: json-schema/amazon-supply-chain-bill-of-materials-import-job-schema.json
slug: amazon-supply-chain-bill-of-materials-import-job
tags:
- AWS
- ERP Integration
- Logistics
- Machine Learning
- Supply Chain
title: BillOfMaterialsImportJob
---
