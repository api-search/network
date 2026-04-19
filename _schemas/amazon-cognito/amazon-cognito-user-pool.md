---
description: Schema representing an Amazon Cognito user pool configuration and its properties.
layout: schema
name: Amazon Cognito User Pool
properties_list:
- description: The unique identifier for the user pool.
  name: Id
  type: string
- description: The name of the user pool.
  name: Name
  type: string
- description: The status of the user pool.
  name: Status
  type: string
- description: The Amazon Resource Name (ARN) for the user pool.
  name: Arn
  type: string
- description: The date and time when the user pool was created.
  name: CreationDate
  type: string
- description: The date and time when the user pool was last modified.
  name: LastModifiedDate
  type: string
- description: A number estimating the size of the user pool.
  name: EstimatedNumberOfUsers
  type: integer
- description: The multi-factor authentication (MFA) configuration.
  name: MfaConfiguration
  type: string
- description: The policies associated with the user pool.
  name: Policies
  type: object
- description: The attributes that are automatically verified.
  name: AutoVerifiedAttributes
  type: array
- description: Specifies whether email addresses or phone numbers can be used as user names when a user signs up.
  name: UsernameAttributes
  type: array
- description: The schema attributes for the user pool.
  name: SchemaAttributes
  type: array
- description: The email configuration for the user pool.
  name: EmailConfiguration
  type: object
- description: The SMS configuration for the user pool.
  name: SmsConfiguration
  type: object
- description: The tags that are assigned to the user pool.
  name: UserPoolTags
  type: object
- description: The configuration for AdminCreateUser requests.
  name: AdminCreateUserConfig
  type: object
provider_name: Amazon Cognito
provider_slug: amazon-cognito
schema_file: json-schema/amazon-cognito-user-pool-schema.json
slug: amazon-cognito-user-pool
tags:
- Authentication
- AWS
- Identity
- OAuth
- User Management
title: Amazon Cognito User Pool
---
