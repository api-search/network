---
description: An Amazon Lookout for Equipment dataset containing equipment sensor data.
layout: schema
name: Dataset
properties_list:
- description: The name of the dataset.
  name: DatasetName
  type: string
- description: The Amazon Resource Name (ARN) of the dataset.
  name: DatasetArn
  type: string
- description: The current status of the dataset.
  name: Status
  type: string
- description: The time at which the dataset was created.
  name: CreatedAt
  type: string
- description: The time at which the dataset was last updated.
  name: LastUpdatedAt
  type: string
provider_name: Amazon Lookout for Equipment
provider_slug: amazon-lookout-for-equipment
schema_file: json-schema/amazon-lookout-for-equipment-dataset-schema.json
slug: amazon-lookout-for-equipment-dataset
tags:
- AWS
- Equipment Monitoring
- Industrial IoT
- Machine Learning
- Predictive Maintenance
title: Dataset
---
