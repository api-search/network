---
description: <p>The Amazon Pinpoint analytics configuration necessary to collect metrics for a user pool.</p> <note> <p>In Regions where Amazon Pinpoint isn't available, user pools only support sending events to Amazon Pinpoint projects in us-east-1. In Regions where Amazon Pinpoint is available, user pools support sending events to Amazon Pinpoint projects within that same Region.</p> </note>
layout: schema
name: AnalyticsConfigurationType
properties_list:
- description: ''
  name: ApplicationId
  type: object
- description: ''
  name: ApplicationArn
  type: object
- description: ''
  name: RoleArn
  type: object
- description: ''
  name: ExternalId
  type: object
- description: ''
  name: UserDataShared
  type: object
provider_name: Amazon Cognito
provider_slug: amazon-cognito
schema_file: json-schema/user-pools-analytics-configuration-type-schema.json
slug: user-pools-analytics-configuration-type
tags:
- Authentication
- AWS
- Identity
- OAuth
- User Management
title: AnalyticsConfigurationType
---
