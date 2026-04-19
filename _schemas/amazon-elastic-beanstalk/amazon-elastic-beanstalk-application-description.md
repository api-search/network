---
description: ApplicationDescription schema from Amazon Elastic Beanstalk AWS Elastic Beanstalk API
layout: schema
name: ApplicationDescription
properties_list:
- description: The Amazon Resource Name (ARN) of the application.
  name: ApplicationArn
  type: string
- description: The name of the application.
  name: ApplicationName
  type: string
- description: User-defined description of the application.
  name: Description
  type: string
- description: The date when the application was created.
  name: DateCreated
  type: string
- description: The date when the application was last modified.
  name: DateUpdated
  type: string
- description: The names of the versions for this application.
  name: Versions
  type: array
- description: The names of the configuration templates associated with this application.
  name: ConfigurationTemplates
  type: array
- description: The lifecycle settings for the application.
  name: ResourceLifecycleConfig
  type: object
provider_name: Amazon Elastic Beanstalk
provider_slug: amazon-elastic-beanstalk
schema_file: json-schema/amazon-elastic-beanstalk-application-description-schema.json
slug: amazon-elastic-beanstalk-application-description
tags:
- Amazon Web Services
- AWS
- Auto Scaling
- Deployment
- Elastic Beanstalk
- PaaS
- Platform As A Service
- Web Applications
title: ApplicationDescription
---
