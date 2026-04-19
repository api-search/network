---
description: Schema representing an AWS Elastic Beanstalk environment, which is a collection of AWS resources running an application version deployed on a specific platform.
layout: schema
name: AWS Elastic Beanstalk Environment
properties_list:
- description: The ID of this environment.
  name: EnvironmentId
  type: string
- description: The name of this environment.
  name: EnvironmentName
  type: string
- description: The ARN of this environment.
  name: EnvironmentArn
  type: string
- description: The name of the application associated with this environment.
  name: ApplicationName
  type: string
- description: The application version deployed in this running environment.
  name: VersionLabel
  type:
  - string
  - 'null'
- description: The name of the SolutionStack deployed with this environment.
  name: SolutionStackName
  type:
  - string
  - 'null'
- description: The ARN of the platform version.
  name: PlatformArn
  type:
  - string
  - 'null'
- description: The name of the configuration template used to originally launch this environment.
  name: TemplateName
  type:
  - string
  - 'null'
- description: Describes this environment.
  name: Description
  type:
  - string
  - 'null'
- description: For load-balanced, autoscaling environments, the URL to the LoadBalancer.
  name: EndpointURL
  type:
  - string
  - 'null'
- description: The URL to the CNAME for this environment.
  name: CNAME
  type:
  - string
  - 'null'
- description: The creation date for this environment.
  name: DateCreated
  type: string
- description: The last modified date for this environment.
  name: DateUpdated
  type: string
- description: The current operational status of the environment.
  name: Status
  type: string
- description: Indicates if there is an in-progress environment configuration update or application version deployment that you can cancel.
  name: AbortableOperationInProgress
  type: boolean
- description: Describes the health status of the environment.
  name: Health
  type: string
- description: Returns the health status of the application running in your environment.
  name: HealthStatus
  type: string
- description: Describes the current tier of this environment.
  name: Tier
  type: object
- description: The description of the AWS resources used by this environment.
  name: Resources
  type: object
- description: A list of links to other environments in the same group.
  name: EnvironmentLinks
  type: array
- description: The Amazon Resource Name (ARN) of the environment's operations role.
  name: OperationsRole
  type:
  - string
  - 'null'
provider_name: Amazon Elastic Beanstalk
provider_slug: amazon-elastic-beanstalk
schema_file: json-schema/amazon-elastic-beanstalk-environment-schema.json
slug: amazon-elastic-beanstalk-environment
tags:
- Amazon Web Services
- AWS
- Auto Scaling
- Deployment
- Elastic Beanstalk
- PaaS
- Platform As A Service
- Web Applications
title: AWS Elastic Beanstalk Environment
---
