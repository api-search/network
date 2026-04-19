---
class_count: 20
classes:
- FoundationModel
- CustomModel
- ProvisionedThroughput
- ModelCustomizationJob
- modelId
- modelArn
- modelName
- providerName
- jobArn
- jobName
- baseModelIdentifier
- customModelName
- customizationType
- trainingDataConfig
- outputDataConfig
- hyperParameters
- provisionedModelArn
- provisionedModelName
- commitmentDuration
- status
context_file: json-ld/amazon-bedrock-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-bedrock/refs/heads/main/json-ld/amazon-bedrock-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Bedrock from Amazon Bedrock.
layout: jsonld
name: Amazon Bedrock Context
namespaces:
- prefix: bedrock
  uri: https://aws.amazon.com/bedrock/ns#
- prefix: aws
  uri: https://aws.amazon.com/ns#
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: inputModalities
  type: '@vocab'
- container: ''
  name: outputModalities
  type: '@vocab'
- container: ''
  name: responseStreamingSupported
  type: boolean
- container: ''
  name: customizationsSupported
  type: '@vocab'
- container: ''
  name: inferenceTypesSupported
  type: '@vocab'
- container: ''
  name: modelUnits
  type: integer
- container: ''
  name: creationTime
  type: dateTime
- container: ''
  name: lastModifiedTime
  type: dateTime
property_count: 8
provider_name: Amazon Bedrock
provider_slug: amazon-bedrock
slug: amazon-bedrock-context
tags:
- AI
- AWS
- Foundation Models
- Generative AI
- LLM
- Machine Learning
- RAG
- Agents
- Responsible AI
- JSON-LD
- Linked Data
- Semantic Web
---
