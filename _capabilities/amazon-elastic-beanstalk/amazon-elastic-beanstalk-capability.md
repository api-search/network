---
consumed_apis:
- elastic_beanstalk
description: Unified capability for managing Amazon Elastic Beanstalk resources. Combines Amazon Elastic Beanstalk APIs for Application Developer workflows in Application Deployment.
layout: capability
name: Amazon Elastic Beanstalk Management
operations:
- description: Amazon Elastic Beanstalk Describe Applications
  method: GET
  name: describeApplications
  path: /v1/describeApplications
- description: Amazon Elastic Beanstalk Create Application
  method: POST
  name: createApplication
  path: /v1/createApplication
- description: Amazon Elastic Beanstalk Create Environment
  method: POST
  name: createEnvironment
  path: /v1/createEnvironment
- description: Amazon Elastic Beanstalk Describe Environments
  method: GET
  name: describeEnvironments
  path: /v1/describeEnvironments
- description: Amazon Elastic Beanstalk Update Environment
  method: POST
  name: updateEnvironment
  path: /v1/updateEnvironment
personas: []
provider_name: Amazon Elastic Beanstalk
provider_slug: amazon-elastic-beanstalk
search_terms:
- amazon elastic beanstalk create environment
- platform as a service
- developers building applications using amazon elastic beanstalk
- operations teams managing amazon elastic beanstalk infrastructure
- createEnvironment
- web applications
- describeEnvironments
- describeApplications
- platform-as-a-service for deploying and managing web applications
- amazon elastic beanstalk describe environments
- amazon elastic beanstalk create application
- aws
- amazon elastic beanstalk update environment
- paas
- updateEnvironment
- auto scaling
- deployment
- amazon web services
- elastic beanstalk
- unified capability for managing amazon elastic beanstalk resources. combines amazon elastic beanstalk apis for application developer workflows in application deployment.
- createApplication
- amazon elastic beanstalk describe applications
slug: amazon-elastic-beanstalk-capability
tags:
- Amazon Web Services
- Platform As A Service
- Deployment
tools:
- description: Amazon Elastic Beanstalk Describe Applications
  hints:
    readOnly: true
  name: describeApplications
- description: Amazon Elastic Beanstalk Create Application
  hints:
    readOnly: false
  name: createApplication
- description: Amazon Elastic Beanstalk Create Environment
  hints:
    readOnly: false
  name: createEnvironment
- description: Amazon Elastic Beanstalk Describe Environments
  hints:
    readOnly: true
  name: describeEnvironments
- description: Amazon Elastic Beanstalk Update Environment
  hints:
    readOnly: false
  name: updateEnvironment
---
