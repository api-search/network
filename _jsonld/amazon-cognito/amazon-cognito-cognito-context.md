---
class_count: 1
classes:
- Amazon Cognito User Pool
context_file: json-ld/amazon-cognito-cognito-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-cognito/refs/heads/main/json-ld/amazon-cognito-cognito-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Cognito Cognito from Amazon Cognito.
layout: jsonld
name: Amazon Cognito Cognito Context
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
  name: Id
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: Arn
  type: string
- container: ''
  name: CreationDate
  type: dateTime
- container: ''
  name: LastModifiedDate
  type: dateTime
- container: ''
  name: EstimatedNumberOfUsers
  type: integer
- container: ''
  name: MfaConfiguration
  type: string
- container: ''
  name: Policies
  type: reference
- container: ''
  name: PasswordPolicy
  type: reference
- container: ''
  name: MinimumLength
  type: integer
- container: ''
  name: RequireUppercase
  type: boolean
- container: ''
  name: RequireLowercase
  type: boolean
- container: ''
  name: RequireNumbers
  type: boolean
- container: ''
  name: RequireSymbols
  type: boolean
- container: ''
  name: TemporaryPasswordValidityDays
  type: integer
- container: set
  name: AutoVerifiedAttributes
  type: string
- container: set
  name: UsernameAttributes
  type: string
- container: set
  name: SchemaAttributes
  type: reference
- container: ''
  name: EmailConfiguration
  type: reference
- container: ''
  name: SourceArn
  type: string
- container: ''
  name: ReplyToEmailAddress
  type: string
- container: ''
  name: EmailSendingAccount
  type: string
- container: ''
  name: SmsConfiguration
  type: reference
- container: ''
  name: SnsCallerArn
  type: string
- container: ''
  name: ExternalId
  type: string
- container: ''
  name: SnsRegion
  type: string
- container: ''
  name: UserPoolTags
  type: reference
- container: ''
  name: AdminCreateUserConfig
  type: reference
- container: ''
  name: AllowAdminCreateUserOnly
  type: boolean
- container: ''
  name: UnusedAccountValidityDays
  type: integer
- container: ''
  name: InviteMessageTemplate
  type: reference
- container: ''
  name: SMSMessage
  type: string
- container: ''
  name: EmailMessage
  type: string
- container: ''
  name: EmailSubject
  type: string
property_count: 35
provider_name: Amazon Cognito
provider_slug: amazon-cognito
slug: amazon-cognito-cognito-context
tags:
- Authentication
- AWS
- Identity
- OAuth
- User Management
- JSON-LD
- Linked Data
- Semantic Web
---
