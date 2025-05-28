---
aid: amazon-web-services:amazon-redshift
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
  - url: openapi/redshift-data-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/redshift/features/
    type: Features
  - url: https://aws.amazon.com/redshift/pricing/
    type: Pricing
  - url: https://aws.amazon.com/redshift/customer-success/
    type: Customer Success
  - url: https://aws.amazon.com/redshift/solutions/
    type: Solutions
description: |-

  Utilize the Amazon Redshift Data API to execute queries on Amazon Redshift
  tables by running SQL statements. Successful statements will be committed.
  Refer to the Amazon Redshift Management Guide for further details on the
  Amazon Redshift Data API and CLI usage examples.

---s
  - url: https://aws.amazon.com/redshift/partners/
    type: Partners
description: |-

  Amazon Redshift is a comprehensive data warehouse solution offered by
  Amazon Web Services. This API reference provides documentation for the
  various programming and command line interfaces available for managing
  Amazon Redshift clusters. It is important to note that Amazon Redshift
  operates asynchronously, requiring techniques such as polling or
  asynchronous callback handlers to track the status of commands. The
  parameter descriptions in this reference specify whether a change takes
  effect immediately, upon the next instance reboot, or during the next
  maintenance window. Amazon Redshift handles tasks such as provisioning
  capacity, monitoring, backup, and applying patches and upgrades to the
  engine, allowing users to focus on leveraging their data for business
  insights.

---