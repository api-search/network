---
description: Information about an AWS Cloud9 development environment.
layout: schema
name: Environment
properties_list:
- description: The ID of the environment.
  name: id
  type: string
- description: The name of the environment.
  name: name
  type: string
- description: The description for the environment.
  name: description
  type: string
- description: The type of environment.
  name: type
  type: string
- description: The connection type for connecting to the environment.
  name: connectionType
  type: string
- description: The current status of the environment.
  name: status
  type: string
- description: The Amazon Resource Name (ARN) of the environment owner.
  name: ownerArn
  type: string
provider_name: Amazon Cloud9
provider_slug: amazon-cloud9
schema_file: json-schema/cloud9-environment-schema.json
slug: cloud9-environment
tags:
- AWS
- Cloud9
- IDE
- Development
- Browser-Based
title: Environment
---
