---
aid: amazon-web-services:redshift-data
name: Amazon Redshift
tags:
  - Tables
  - Data
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/redshift/
overlays:
  - url: overlays/redshift-data-openapi-search.yml
    type: APIs.io Search
  - url: overlays/redshift-data-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/redshift/
    type: Documentation
  - url: properties/redshift-data-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/redshift/features/
    type: Features
  - url: https://aws.amazon.com/redshift/pricing/
    type: Pricing
  - url: https://aws.amazon.com/redshift/customer-success/
    type: Customer Success
  - url: https://aws.amazon.com/redshift/solutions/
    type: Solutions
description: >-
  Utilize the Amazon Redshift Data API to execute queries on Amazon Redshift
  tables by running SQL statements. Successful statements will be committed.
  Refer to the Amazon Redshift Management Guide for further details on the
  Amazon Redshift Data API and CLI usage examples.

---