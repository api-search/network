---
description: NotebookInstance schema from Amazon SageMaker API
layout: schema
name: NotebookInstance
properties_list:
- description: The Amazon Resource Name (ARN) of the notebook instance.
  name: NotebookInstanceArn
  type: string
- description: The name of the notebook instance.
  name: NotebookInstanceName
  type: string
- description: The status of the notebook instance.
  name: NotebookInstanceStatus
  type: string
- description: The type of ML compute instance running the notebook.
  name: InstanceType
  type: string
- description: The ARN of the IAM role associated with the instance.
  name: RoleArn
  type: string
- description: The ID of the VPC subnet.
  name: SubnetId
  type: string
- description: The security groups associated with the instance.
  name: SecurityGroups
  type: array
- description: The URL that you use to connect to the Jupyter notebook.
  name: Url
  type: string
- description: The size of the ML storage volume in GB.
  name: VolumeSizeInGB
  type: integer
- description: A timestamp indicating when the notebook instance was created.
  name: CreationTime
  type: string
- description: A timestamp indicating when the notebook instance was last modified.
  name: LastModifiedTime
  type: string
provider_name: Amazon SageMaker
provider_slug: amazon-sagemaker
schema_file: json-schema/amazon-sagemaker-notebook-instance-schema.json
slug: amazon-sagemaker-notebook-instance
tags:
- AI
- AWS
- Inference
- Machine Learning
- MLOps
- Training
title: NotebookInstance
---
