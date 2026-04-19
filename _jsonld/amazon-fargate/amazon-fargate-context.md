---
class_count: 18
classes:
- PortMapping
- LogConfiguration
- KeyValuePair
- name
- LoadBalancer
- TaskDefinition
- Tag
- AccountSetting
- Failure
- NetworkConfiguration
- Amazon Fargate Task
- createdAt
- Service
- AwsVpcConfiguration
- ClusterSetting
- ContainerDefinition
- Cluster
- Task
context_file: json-ld/amazon-fargate-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-fargate/refs/heads/main/json-ld/amazon-fargate-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Fargate from Amazon Fargate.
layout: jsonld
name: Amazon Fargate Context
namespaces:
- prefix: fargate
  uri: https://aws.amazon.com/fargate/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: containerPort
  type: integer
- container: ''
  name: hostPort
  type: integer
- container: ''
  name: protocol
  type: string
- container: ''
  name: logDriver
  type: string
- container: ''
  name: options
  type: reference
- container: ''
  name: value
  type: string
- container: ''
  name: targetGroupArn
  type: string
- container: ''
  name: loadBalancerName
  type: string
- container: ''
  name: containerName
  type: string
- container: ''
  name: taskDefinitionArn
  type: string
- container: ''
  name: family
  type: string
- container: ''
  name: revision
  type: integer
- container: ''
  name: status
  type: string
- container: set
  name: requiresCompatibilities
  type: string
- container: ''
  name: networkMode
  type: string
- container: ''
  name: cpu
  type: string
- container: ''
  name: memory
  type: string
- container: ''
  name: executionRoleArn
  type: string
- container: ''
  name: taskRoleArn
  type: string
- container: set
  name: containerDefinitions
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: principalArn
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: reason
  type: string
- container: ''
  name: detail
  type: string
- container: ''
  name: awsvpcConfiguration
  type: string
- container: ''
  name: taskArn
  type: string
- container: ''
  name: clusterArn
  type: string
- container: ''
  name: launchType
  type: string
- container: ''
  name: lastStatus
  type: string
- container: ''
  name: desiredStatus
  type: string
- container: set
  name: containers
  type: reference
- container: ''
  name: containerArn
  type: string
- container: ''
  name: image
  type: string
- container: ''
  name: platformVersion
  type: string
- container: set
  name: tags
  type: reference
- container: ''
  name: serviceArn
  type: string
- container: ''
  name: serviceName
  type: string
- container: ''
  name: taskDefinition
  type: string
- container: ''
  name: desiredCount
  type: integer
- container: ''
  name: runningCount
  type: integer
- container: ''
  name: pendingCount
  type: integer
- container: ''
  name: networkConfiguration
  type: string
- container: set
  name: loadBalancers
  type: string
- container: set
  name: subnets
  type: string
- container: set
  name: securityGroups
  type: string
- container: ''
  name: assignPublicIp
  type: string
- container: ''
  name: essential
  type: boolean
- container: set
  name: environment
  type: string
- container: set
  name: portMappings
  type: string
- container: ''
  name: logConfiguration
  type: string
- container: ''
  name: clusterName
  type: string
- container: ''
  name: registeredContainerInstancesCount
  type: integer
- container: ''
  name: runningTasksCount
  type: integer
- container: ''
  name: pendingTasksCount
  type: integer
- container: ''
  name: activeServicesCount
  type: integer
- container: set
  name: settings
  type: string
- container: ''
  name: startedAt
  type: dateTime
- container: ''
  name: stoppedAt
  type: dateTime
- container: ''
  name: stoppedReason
  type: string
- container: set
  name: networkInterfaces
  type: reference
property_count: 61
provider_name: Amazon Fargate
provider_slug: amazon-fargate
slug: amazon-fargate-context
tags:
- AWS
- Compute
- Containers
- ECS
- EKS
- Microservices
- Serverless
- JSON-LD
- Linked Data
- Semantic Web
---
