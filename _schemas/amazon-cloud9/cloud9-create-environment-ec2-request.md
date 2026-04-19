---
description: Request body for creating an EC2-based Cloud9 environment.
layout: schema
name: CreateEnvironmentEC2Request
properties_list:
- description: The name of the environment.
  name: name
  type: string
- description: The description of the environment.
  name: description
  type: string
- description: The type of instance to connect to the environment.
  name: instanceType
  type: string
- description: The connection type to use for connecting to the environment.
  name: connectionType
  type: string
- description: The number of minutes until the running instance is shut down after the environment has last been used.
  name: automaticStopTimeMinutes
  type: integer
provider_name: Amazon Cloud9
provider_slug: amazon-cloud9
schema_file: json-schema/cloud9-create-environment-ec2-request-schema.json
slug: cloud9-create-environment-ec2-request
tags:
- AWS
- Cloud9
- IDE
- Development
- Browser-Based
title: CreateEnvironmentEC2Request
---
