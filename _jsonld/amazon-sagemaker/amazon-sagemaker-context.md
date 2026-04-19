---
class_count: 5
classes:
- Tag
- NotebookInstance
- TrainingJob
- Model
- Endpoint
context_file: json-ld/amazon-sagemaker-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-sagemaker/refs/heads/main/json-ld/amazon-sagemaker-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Sagemaker from Amazon SageMaker.
layout: jsonld
name: Amazon Sagemaker Context
namespaces:
- prefix: aws
  uri: https://aws.amazon.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: Key
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: NotebookInstanceArn
  type: string
- container: ''
  name: NotebookInstanceName
  type: string
- container: ''
  name: NotebookInstanceStatus
  type: string
- container: ''
  name: InstanceType
  type: string
- container: ''
  name: RoleArn
  type: string
- container: ''
  name: SubnetId
  type: string
- container: set
  name: SecurityGroups
  type: string
- container: ''
  name: Url
  type: string
- container: ''
  name: VolumeSizeInGB
  type: integer
- container: ''
  name: CreationTime
  type: dateTime
- container: ''
  name: LastModifiedTime
  type: dateTime
- container: ''
  name: TrainingJobName
  type: string
- container: ''
  name: TrainingJobArn
  type: string
- container: ''
  name: TrainingJobStatus
  type: string
- container: ''
  name: SecondaryStatus
  type: string
- container: ''
  name: AlgorithmSpecification
  type: string
- container: ''
  name: TrainingImage
  type: string
- container: ''
  name: TrainingInputMode
  type: string
- container: ''
  name: AlgorithmName
  type: string
- container: set
  name: InputDataConfig
  type: string
- container: ''
  name: OutputDataConfig
  type: string
- container: ''
  name: S3OutputPath
  type: string
- container: ''
  name: KmsKeyId
  type: string
- container: ''
  name: ResourceConfig
  type: string
- container: ''
  name: InstanceCount
  type: integer
- container: ''
  name: StoppingCondition
  type: string
- container: ''
  name: MaxRuntimeInSeconds
  type: integer
- container: ''
  name: MaxWaitTimeInSeconds
  type: integer
- container: ''
  name: HyperParameters
  type: string
- container: ''
  name: ModelArtifacts
  type: string
- container: ''
  name: S3ModelArtifacts
  type: string
- container: ''
  name: TrainingStartTime
  type: dateTime
- container: ''
  name: TrainingEndTime
  type: dateTime
- container: ''
  name: BillableTimeInSeconds
  type: integer
- container: ''
  name: FailureReason
  type: string
- container: ''
  name: ModelName
  type: string
- container: ''
  name: ModelArn
  type: string
- container: ''
  name: PrimaryContainer
  type: string
- container: ''
  name: Image
  type: string
- container: ''
  name: ModelDataUrl
  type: string
- container: ''
  name: Environment
  type: string
- container: ''
  name: ExecutionRoleArn
  type: string
- container: ''
  name: EndpointName
  type: string
- container: ''
  name: EndpointArn
  type: string
- container: ''
  name: EndpointConfigName
  type: string
- container: ''
  name: EndpointStatus
  type: string
- container: set
  name: ProductionVariants
  type: string
property_count: 49
provider_name: Amazon SageMaker
provider_slug: amazon-sagemaker
slug: amazon-sagemaker-context
tags:
- AI
- AWS
- Inference
- Machine Learning
- MLOps
- Training
- JSON-LD
- Linked Data
- Semantic Web
---
