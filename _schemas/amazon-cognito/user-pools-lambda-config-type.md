---
description: Specifies the configuration for Lambda triggers.
layout: schema
name: LambdaConfigType
properties_list:
- description: ''
  name: PreSignUp
  type: object
- description: ''
  name: CustomMessage
  type: object
- description: ''
  name: PostConfirmation
  type: object
- description: ''
  name: PreAuthentication
  type: object
- description: ''
  name: PostAuthentication
  type: object
- description: ''
  name: DefineAuthChallenge
  type: object
- description: ''
  name: CreateAuthChallenge
  type: object
- description: ''
  name: VerifyAuthChallengeResponse
  type: object
- description: ''
  name: PreTokenGeneration
  type: object
- description: ''
  name: UserMigration
  type: object
- description: ''
  name: CustomSMSSender
  type: object
- description: ''
  name: CustomEmailSender
  type: object
- description: ''
  name: KMSKeyID
  type: object
provider_name: Amazon Cognito
provider_slug: amazon-cognito
schema_file: json-schema/user-pools-lambda-config-type-schema.json
slug: user-pools-lambda-config-type
tags:
- Authentication
- AWS
- Identity
- OAuth
- User Management
title: LambdaConfigType
---
