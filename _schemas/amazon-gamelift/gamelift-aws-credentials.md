---
description: Temporary access credentials used for uploading game build files to Amazon GameLift. They are valid for a limited time. If they expire before you upload your game build, get a new set by calling <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_RequestUploadCredentials.html">RequestUploadCredentials</a>.
layout: schema
name: AwsCredentials
properties_list:
- description: ''
  name: AccessKeyId
  type: object
- description: ''
  name: SecretAccessKey
  type: object
- description: ''
  name: SessionToken
  type: object
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
schema_file: json-schema/gamelift-aws-credentials-schema.json
slug: gamelift-aws-credentials
tags:
- AWS
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
title: AwsCredentials
---
