---
aid: amazon-web-services:ec2-instance-connect
name: Amazon EC2 Instance Connect
tags:
  - Console
  - Keys
  - SSHPublic
  - Send
  - Serial
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: >-
  https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-eic.html
overlays:
  - url: overlays/ec2-instance-connect-openapi-search.yml
    type: APIs.io Search
  - url: overlays/ec2-instance-connect-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: >-
      https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-eic.html
    type: Documentation
  - url: properties/ec2-instance-connect-openapi-original.yml
    type: OpenAPI
description: >-
  Amazon EC2 Instance Connect allows system administrators to generate and share
  one-time use SSH public keys on EC2, offering users a convenient and reliable
  method to access their instances securely.

---