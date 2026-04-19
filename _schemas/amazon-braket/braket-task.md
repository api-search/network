---
description: A quantum task submitted to an Amazon Braket device (QPU or simulator)
layout: schema
name: Quantum Task
properties_list:
- description: ARN of the quantum task
  name: quantumTaskArn
  type: string
- description: ARN of the quantum device the task is submitted to
  name: deviceArn
  type: string
- description: Number of times the circuit is executed
  name: shots
  type: integer
- description: S3 bucket for task result output
  name: outputS3Bucket
  type: string
- description: S3 key prefix for task result output
  name: outputS3KeyPrefix
  type: string
- description: Current status of the quantum task
  name: status
  type: string
- description: Reason for task failure if status is FAILED
  name: failureReason
  type: string
- description: Timestamp when the task was created
  name: createdAt
  type: string
- description: Timestamp when the task ended
  name: endedAt
  type: string
- description: Metadata tags for the quantum task
  name: tags
  type: object
provider_name: Amazon Braket
provider_slug: amazon-braket
schema_file: json-schema/braket-task-schema.json
slug: braket-task
tags:
- Quantum Computing
- Quantum Hardware
- Hybrid Quantum-Classical
- QPU
- Quantum Simulation
- AWS
- Amazon Web Services
- Research
- HPC
title: Quantum Task
---
