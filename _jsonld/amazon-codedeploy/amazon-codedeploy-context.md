---
class_count: 16
classes:
- CreateApplicationRequest
- CreateApplicationResponse
- ListApplicationsResponse
- GetApplicationResponse
- CreateDeploymentRequest
- CreateDeploymentResponse
- ListDeploymentsResponse
- GetDeploymentResponse
- InvalidApplicationNameException
- ApplicationAlreadyExistsException
- ApplicationDoesNotExistException
- InvalidDeploymentGroupNameException
- InvalidDeploymentIdException
- DeploymentDoesNotExistException
- InvalidNextTokenException
- description
context_file: json-ld/amazon-codedeploy-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-codedeploy/refs/heads/main/json-ld/amazon-codedeploy-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Codedeploy from Amazon CodeDeploy.
layout: jsonld
name: Amazon Codedeploy Context
namespaces:
- prefix: amazon-code-deploy
  uri: https://amazon-code-deploy.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: applicationName
  type: string
- container: ''
  name: computePlatform
  type: string
- container: ''
  name: applicationId
  type: string
- container: set
  name: applications
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: application
  type: string
- container: ''
  name: createTime
  type: dateTime
- container: ''
  name: linkedToGitHub
  type: boolean
- container: ''
  name: deploymentGroupName
  type: string
- container: ''
  name: revision
  type: string
- container: ''
  name: revisionType
  type: string
- container: ''
  name: s3Location
  type: string
- container: ''
  name: bucket
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: bundleType
  type: string
- container: ''
  name: gitHubLocation
  type: string
- container: ''
  name: repository
  type: string
- container: ''
  name: commitId
  type: string
- container: ''
  name: autoRollbackConfiguration
  type: string
- container: ''
  name: enabled
  type: boolean
- container: set
  name: events
  type: string
- container: ''
  name: deploymentId
  type: string
- container: set
  name: deployments
  type: string
- container: ''
  name: deploymentInfo
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: startTime
  type: dateTime
- container: ''
  name: completeTime
  type: dateTime
- container: ''
  name: creator
  type: string
- container: ''
  name: message
  type: string
property_count: 29
provider_name: Amazon CodeDeploy
provider_slug: amazon-codedeploy
slug: amazon-codedeploy-context
tags:
- Amazon
- AWS
- Deployment
- DevOps
- CI/CD
- Release Management
- Blue/Green Deployment
- JSON-LD
- Linked Data
- Semantic Web
---
