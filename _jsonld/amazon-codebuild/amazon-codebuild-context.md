---
class_count: 11
classes:
- CreateProjectRequest
- CreateProjectResponse
- ListProjectsResponse
- Project
- StartBuildRequest
- StartBuildResponse
- StopBuildResponse
- BatchGetBuildsResponse
- Build
- name
- description
context_file: json-ld/amazon-codebuild-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-codebuild/refs/heads/main/json-ld/amazon-codebuild-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Codebuild from Amazon CodeBuild.
layout: jsonld
name: Amazon Codebuild Context
namespaces:
- prefix: amazon-code-build
  uri: https://amazon-code-build.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: source
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: buildspec
  type: string
- container: ''
  name: environment
  type: string
- container: ''
  name: image
  type: string
- container: ''
  name: computeType
  type: string
- container: set
  name: environmentVariables
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: serviceRole
  type: string
- container: ''
  name: timeoutInMinutes
  type: integer
- container: ''
  name: project
  type: string
- container: set
  name: projects
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: created
  type: dateTime
- container: ''
  name: lastModified
  type: dateTime
- container: ''
  name: projectName
  type: string
- container: ''
  name: sourceVersion
  type: string
- container: set
  name: environmentVariablesOverride
  type: string
- container: ''
  name: build
  type: string
- container: set
  name: builds
  type: string
- container: set
  name: buildsNotFound
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: buildNumber
  type: integer
- container: ''
  name: startTime
  type: dateTime
- container: ''
  name: endTime
  type: dateTime
- container: ''
  name: currentPhase
  type: string
- container: ''
  name: buildStatus
  type: string
property_count: 29
provider_name: Amazon CodeBuild
provider_slug: amazon-codebuild
slug: amazon-codebuild-context
tags:
- Amazon
- AWS
- CI/CD
- Build
- Continuous Integration
- DevOps
- Testing
- JSON-LD
- Linked Data
- Semantic Web
---
