---
aid: amazon-web-services:amazon-elastic-container-registry
name: Amazon Elastic Container Registry
tags:
  - Cache
  - Pull
  - Rules
  - Validate
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/ecr/
overlays:
  - url: overlays/ecr-openapi-search.yml
    type: APIs.io Search
  - url: overlays/ecr-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/ecr/
    type: Documentation
  - url: openapi/ecr-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/ecr/features/
    type: Features
  - url: https://aws.amazon.com/ecr/pricing/
    type: Pricing
  - url: https://aws.amazon.com/ecr/getting-started/
    type: Getting Started
  - url: https://aws.amazon.com/ecr/resources/
    type: Resources
  - url: https://aws.amazon.com/ecr/faqs/
    type: FAQ
  - url: https://aws.amazon.com/ecr/customers/
    type: Customers
description: |-

  The Amazon Elastic Container Registry (Amazon ECR) is a managed service
  that allows customers to store and manage container images securely. Users
  can easily push, pull, and manage images using the Docker CLI or their
  preferred client. Amazon ECR supports private repositories with
  resource-based permissions using IAM, allowing specific users or Amazon
  EC2 instances to access repositories and images. 

---