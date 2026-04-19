---
class_count: 6
classes:
- Secret
- RotationRules
- SecretValue
- Tag
- ListSecretsResponse
- GetRandomPasswordResponse
context_file: json-ld/amazon-secrets-manager-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-secrets-manager/refs/heads/main/json-ld/amazon-secrets-manager-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Secrets Manager from Amazon Secrets Manager.
layout: jsonld
name: Amazon Secrets Manager Context
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
  name: ARN
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: Description
  type: string
- container: ''
  name: KmsKeyId
  type: string
- container: ''
  name: RotationEnabled
  type: boolean
- container: ''
  name: RotationLambdaARN
  type: string
- container: ''
  name: LastRotatedDate
  type: dateTime
- container: ''
  name: LastChangedDate
  type: dateTime
- container: ''
  name: LastAccessedDate
  type: dateTime
- container: ''
  name: DeletedDate
  type: dateTime
- container: set
  name: Tags
  type: string
- container: ''
  name: SecretVersionsToStages
  type: string
- container: ''
  name: OwningService
  type: string
- container: ''
  name: CreatedDate
  type: dateTime
- container: ''
  name: PrimaryRegion
  type: string
- container: ''
  name: VersionId
  type: string
- container: ''
  name: SecretBinary
  type: string
- container: ''
  name: SecretString
  type: string
- container: set
  name: VersionStages
  type: string
- container: ''
  name: AutomaticallyAfterDays
  type: integer
- container: ''
  name: Duration
  type: string
- container: ''
  name: ScheduleExpression
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: Value
  type: string
- container: set
  name: SecretList
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: RandomPassword
  type: string
property_count: 27
provider_name: Amazon Secrets Manager
provider_slug: amazon-secrets-manager
slug: amazon-secrets-manager-context
tags:
- AWS
- Configuration
- Credentials
- Rotation
- Secrets
- Security
- JSON-LD
- Linked Data
- Semantic Web
---
