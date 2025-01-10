---
aid: amazon-web-services:aws-launch-wizard
name: AWS Launch Wizard
tags:
  - Deployments
  - Events
  - Patterns
  - Workloads
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/launchwizard/
overlays:
  - url: overlays/launch-wizard-openapi-search.yml
    type: APIs.io Search
  - url: overlays/launch-wizard-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/launchwizard/
    type: Documentation
  - url: openapi/launch-wizard-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/launchwizard/faq/
    type: FAQ
description: |-

  Launch Wizard is a tool that simplifies the process of sizing,
  configuring, and deploying Amazon Web Services resources for third party
  applications, including Microsoft SQL Server Always On and HANA based SAP
  systems. This streamlined approach eliminates the need for manual
  identification and provisioning of individual AWS resources.

---