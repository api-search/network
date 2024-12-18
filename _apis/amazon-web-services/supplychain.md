---
aid: amazon-web-services:supplychain
name: AWS Supply Chain
tags:
  - Bill
  - Configurations
  - Import
  - Instances
  - Jobs
  - Materials
  - Supply Chain
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/aws-supply-chain/
overlays:
  - url: overlays/supplychain-openapi-search.yml
    type: APIs.io Search
  - url: overlays/supplychain-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/aws-supply-chain/
    type: Documentation
  - url: properties/supplychain-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/aws-supply-chain/features/
    type: Features
  - url: https://aws.amazon.com/aws-supply-chain/pricing/
    type: Pricing
  - url: https://aws.amazon.com/aws-supply-chain/partners/
    type: Partners
  - url: https://aws.amazon.com/aws-supply-chain/resources/
    type: Resources
description: >-
  The AWS Supply Chain API is a cloud-based application designed to streamline
  supply chain management processes by connecting and extracting inventory,
  supply, and demand data from existing ERP and supply chain systems into a
  single data model. This API supports configuration data import for Supply
  Planning and all operations are authenticated and signed by Amazon
  certificates. The use of the AWS SDK is required, along with AWS Identity and
  Access Management users and roles to ensure secure access and permission
  policies.

---