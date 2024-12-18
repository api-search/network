---
aid: amazon-web-services:es
name: Amazon Elasticsearch Configuration Service
tags:
  - Accept
  - Access
  - Associate
  - Authorize
  - Auto
  - Cancel
  - Change
  - Clusters
  - Compatible
  - Configurations
  - Connections
  - Describe
  - Dissociate
  - Domains
  - Elasticsearch
  - Endpoints
  - History
  - Inbound
  - Info
  - Instances
  - Limits
  - Names
  - Offerings
  - Outbound
  - Packages
  - Progress
  - Purchase
  - Reject
  - Removal
  - Removes
  - Reserved
  - Revoke
  - Roles
  - Search
  - Services
  - Software
  - Status
  - Tags
  - Tunes
  - Types
  - Upgrade
  - VPC
  - Versions
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://es.[region].amazonaws.com
humanURL: >-
  https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html
overlays:
  - url: overlays/es-openapi-search.yml
    type: APIs.io Search
  - url: overlays/es-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: >-
      https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html
    type: Documentation
  - url: properties/es-openapi-original.yml
    type: OpenAPI
description: >-
  Utilize the Amazon Elasticsearch Configuration Service API for creating,
  customizing, and overseeing Elasticsearch domains. Developers can refer to the
  Amazon Elasticsearch Service Developer Guide for sample code showcasing the
  Configuration API in action, as well as instructions for sending signed HTTP
  requests to Elasticsearch APIs.

---