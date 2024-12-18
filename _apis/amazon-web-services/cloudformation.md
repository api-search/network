---
aid: amazon-web-services:cloudformation
name: AWS CloudFormation
tags:
  - Templates
  - Validate
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/cloudformation/
overlays:
  - url: overlays/cloudformation-openapi-search.yml
    type: APIs.io Search
  - url: overlays/cloudformation-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/cloudformation/
    type: Documentation
  - url: properties/cloudformation-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/cloudformation/features/
    type: Features
  - url: https://aws.amazon.com/cloudformation/pricing/
    type: Pricing
  - url: https://aws.amazon.com/cloudformation/getting-started/
    type: Getting Started
  - url: https://aws.amazon.com/cloudformation/resources/
    type: Resources
  - url: https://aws.amazon.com/cloudformation/partners/
    type: Partners
  - url: https://aws.amazon.com/cloudformation/faqs/
    type: FAQ
description: >-
  CloudFormation is an Amazon Web Services tool that allows users to easily
  create and manage infrastructure deployments in a predictable and repeatable
  manner. With CloudFormation, you can utilize various AWS products like EC2,
  EBS, SNS, ELB, and Auto Scaling to build reliable and scalable applications
  without needing to manually configure the underlying infrastructure. By
  declaring resources and their dependencies in a template file, CloudFormation
  organizes them into a stack, enabling seamless creation and deletion of all
  resources within the stack while managing dependencies between them.

---