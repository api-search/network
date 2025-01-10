---
aid: amazon-web-services:aws-rds
name: AWS RDS
tags:
  - Batches
  - Execute
  - Statements
  - Begins
  - Transactions
  - Commit
  - SQL
  - Rollback
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/rds/
overlays:
  - url: overlays/rds-data-openapi-search.yml
    type: APIs.io Search
  - url: overlays/rds-data-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/rds/
    type: Documentation
  - url: openapi/rds-data-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/rds/features/
    type: Features
  - url: https://aws.amazon.com/rds/pricing/
    type: Pricing
  - url: https://aws.amazon.com/rds/resources/
    type: Resources
  - url: https://aws.amazon.com/rds/faqs/
    type: FAQ
  - url: https://aws.amazon.com/rds/customers/
    type: Customers
  - url: https://aws.amazon.com/rds/partners/
    type: Partners
description: |-

  The RDS Data API from Amazon RDS allows users to execute SQL statements on
  an Amazon Aurora DB cluster via an HTTP endpoint. This API is compatible
  with various types of Aurora databases, including Aurora PostgreSQL
  (Serverless v2, Serverless v1, and provisioned) and Aurora MySQL
  (Serverless v1). Detailed instructions on utilizing the Data API can be
  found in the Amazon Aurora User Guide.

---