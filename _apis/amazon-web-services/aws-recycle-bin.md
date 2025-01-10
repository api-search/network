---
aid: amazon-web-services:aws-recycle-bin
name: AWS Recycle Bin
tags:
  - ARN
  - Locks
  - Resources
  - Rules
  - Tags
  - Unlock
  - Untag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://docs.aws.amazon.com/recyclebin/latest/APIReference/Welcome.html
overlays:
  - url: overlays/rbin-openapi-search.yml
    type: APIs.io Search
  - url: overlays/rbin-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: |-

      https://docs.aws.amazon.com/recyclebin/latest/APIReference/Welcome.html
    type: Documentation
  - url: openapi/rbin-openapi-original.yml
    type: OpenAPI
  - url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recycle-bin.html
    type: User Guide
  - url: https://docs.aws.amazon.com/cli/latest/reference/rbin/index.html
    type: Command Line Interface
description: |-

  This is the API Reference for Recycle Bin, a feature that allows you to
  recover accidentally deleted snapshots and EBS-backed AMIs. The
  documentation provides detailed descriptions and syntax for each action
  and data type within Recycle Bin. When you use Recycle Bin, any deleted
  resources are stored in the bin for a specified time period. 

---