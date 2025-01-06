---
aid: amazon-web-services:amazon-dynamodb-accelerator-dax
name: Amazon DynamoDB Accelerator (DAX)
tags:
  - Subnets
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/dynamodbaccelerator/
overlays:
  - url: overlays/dax-openapi-search.yml
    type: APIs.io Search
  - url: overlays/dax-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/dynamodbaccelerator/
    type: Documentation
  - url: openapi/dax-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/dynamodbaccelerator/customers/
    type: Customers
description: |-

  DAX is a managed caching service designed specifically for Amazon
  DynamoDB. It significantly boosts database read speeds by storing
  frequently accessed data from DynamoDB, allowing applications to retrieve
  that data with extremely low latency. Setting up a DAX cluster is a
  straightforward process through the AWS Management Console. 

---