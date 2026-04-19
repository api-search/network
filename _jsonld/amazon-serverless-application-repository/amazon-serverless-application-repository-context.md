---
class_count: 7
classes:
- Application
- name
- author
- description
- ApplicationSummary
- VersionSummary
- ApplicationPolicyStatement
context_file: json-ld/amazon-serverless-application-repository-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-serverless-application-repository/refs/heads/main/json-ld/amazon-serverless-application-repository-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Serverless Application Repository from Amazon Serverless Application Repository.
layout: jsonld
name: Amazon Serverless Application Repository Context
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
  name: applicationId
  type: string
- container: ''
  name: creationTime
  type: dateTime
- container: ''
  name: homePageUrl
  type: string
- container: set
  name: labels
  type: string
- container: ''
  name: licenseUrl
  type: string
- container: ''
  name: readmeUrl
  type: string
- container: ''
  name: spdxLicenseId
  type: string
- container: ''
  name: version
  type: string
- container: ''
  name: semanticVersion
  type: string
- container: ''
  name: sourceCodeUrl
  type: string
- container: ''
  name: statementId
  type: string
- container: set
  name: principals
  type: string
- container: set
  name: actions
  type: string
property_count: 13
provider_name: Amazon Serverless Application Repository
provider_slug: amazon-serverless-application-repository
slug: amazon-serverless-application-repository-context
tags:
- Application Repository
- AWS
- Lambda
- SAM
- Serverless
- JSON-LD
- Linked Data
- Semantic Web
---
