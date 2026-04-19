---
description: A data lake dataset
layout: schema
name: DataLakeDataset
properties_list:
- description: The instance identifier
  name: instanceId
  type: string
- description: The namespace containing the dataset
  name: namespace
  type: string
- description: The dataset name
  name: name
  type: string
- description: The dataset description
  name: description
  type: string
- description: The dataset schema
  name: schema
  type: object
- description: The partition specification
  name: partitionSpec
  type: object
- description: ''
  name: createdTime
  type: string
- description: ''
  name: lastModifiedTime
  type: string
provider_name: Amazon Supply Chain
provider_slug: amazon-supply-chain
schema_file: json-schema/amazon-supply-chain-data-lake-dataset-schema.json
slug: amazon-supply-chain-data-lake-dataset
tags:
- AWS
- ERP Integration
- Logistics
- Machine Learning
- Supply Chain
title: DataLakeDataset
---
