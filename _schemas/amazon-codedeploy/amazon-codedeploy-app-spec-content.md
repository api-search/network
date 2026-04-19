---
description: A revision for an Lambda or Amazon ECS deployment that is a YAML-formatted or JSON-formatted string. For Lambda and Amazon ECS deployments, the revision is the same as the AppSpec file. This method replaces the deprecated <code>RawString</code> data type.
layout: schema
name: AppSpecContent
properties_list:
- description: ''
  name: content
  type: object
- description: ''
  name: sha256
  type: object
provider_name: Amazon CodeDeploy
provider_slug: amazon-codedeploy
schema_file: json-schema/amazon-codedeploy-app-spec-content-schema.json
slug: amazon-codedeploy-app-spec-content
tags:
- Amazon
- AWS
- Deployment
- DevOps
- CI/CD
- Release Management
- Blue/Green Deployment
title: AppSpecContent
---
