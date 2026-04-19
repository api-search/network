---
description: <p>The email configuration of your user pool. The email configuration type sets your preferred sending method, Amazon Web Services Region, and sender for messages from your user pool.</p> <note> <p>Amazon Cognito can send email messages with Amazon Simple Email Service resources in the Amazon Web Services Region where you created your user pool, and in alternate Regions in some cases. For more information on the supported Regions, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-email.html">Email settings for Amazon Cognito user pools</a>.</p> </note>
layout: schema
name: EmailConfigurationType
properties_list:
- description: ''
  name: SourceArn
  type: object
- description: ''
  name: ReplyToEmailAddress
  type: object
- description: ''
  name: EmailSendingAccount
  type: object
- description: ''
  name: From
  type: object
- description: ''
  name: ConfigurationSet
  type: object
provider_name: Amazon Cognito
provider_slug: amazon-cognito
schema_file: json-schema/user-pools-email-configuration-type-schema.json
slug: user-pools-email-configuration-type
tags:
- Authentication
- AWS
- Identity
- OAuth
- User Management
title: EmailConfigurationType
---
