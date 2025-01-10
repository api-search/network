---
aid: amazon-web-services:aws-resource-explorer
name: AWS Resource Explorer
tags:
  - ARN
  - Accounts
  - Associate
  - Batches
  - Configurations
  - Default
  - Disassociate
  - Index
  - Indexes
  - Levels
  - Members
  - Resources
  - Search
  - Services
  - Supported
  - Tags
  - Types
  - Untag
  - View
  - Views
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/resourceexplorer/
overlays:
  - url: overlays/resource-explorer-2-openapi-search.yml
    type: APIs.io Search
  - url: overlays/resource-explorer-2-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/resourceexplorer/
    type: Documentation
  - url: openapi/resource-explorer-2-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/resourceexplorer/features/
    type: Features
  - url: https://aws.amazon.com/resourceexplorer/pricing/
    type: Pricing
  - url: https://aws.amazon.com/resourceexplorer/faqs/
    type: FAQ
description: |-

  Amazon Web Services Resource Explorer is a search and discovery service
  that allows users to explore their resources using an internet search
  engine-like experience. Examples of resources that can be searched for
  include Amazon RDS instances, Amazon S3 buckets, and Amazon DynamoDB
  tables. Users can search for resources using metadata such as names, tags,
  and IDs. Resource Explorer can search across all AWS Regions in the user's
  account to simplify cross-Region workloads. By turning on Resource
  Explorer, users can scan and index resources in each Region, with the
  option to designate one Region as the aggregator index for the account.
  This aggregator index contains a copy of all resource information from all
  Regions where Resource Explorer is enabled. Users can access a
  comprehensive view of their resources across all indexed Regions in their
  account. For more information on enabling and configuring Resource
  Explorer, refer to the user guide provided by Amazon Web Services.

---