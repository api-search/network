---
class_count: 23
classes:
- QuantumTask
- quantumTaskArn
- shots
- action
- deviceParameters
- Device
- deviceArn
- deviceName
- deviceType
- deviceStatus
- providerName
- deviceCapabilities
- Job
- jobArn
- jobName
- algorithmSpecification
- instanceConfig
- hyperParameters
- status
- failureReason
- outputS3Bucket
- outputS3KeyPrefix
- tags
context_file: json-ld/context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-braket/refs/heads/main/json-ld/context.jsonld
description: JSON-LD context defining the semantic vocabulary for context from Amazon Braket.
layout: jsonld
name: context Context
namespaces:
- prefix: schema
  uri: https://schema.org/
- prefix: braket
  uri: https://aws.amazon.com/braket/vocab#
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: endedAt
  type: dateTime
- container: ''
  name: startedAt
  type: dateTime
property_count: 3
provider_name: Amazon Braket
provider_slug: amazon-braket
slug: context
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
- JSON-LD
- Linked Data
- Semantic Web
---
