---
aid: amazon-web-services:amazon-elastic-container-registry-public
name: Amazon Elastic Container Registry Public
tags:
  - Layers
  - Uploads
  - Containers
  - Registry
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://docs.aws.amazon.com/AmazonECR/latest/public/what-is-ecr.html
overlays:
  - url: overlays/ecr-public-openapi-search.yml
    type: APIs.io Search
  - url: overlays/ecr-public-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://docs.aws.amazon.com/AmazonECR/latest/public/what-is-ecr.html
    type: Documentation
  - url: openapi/ecr-public-openapi-original.yml
    type: OpenAPI
  - url: https://gallery.ecr.aws/
    type: Gallery
description: |-

  The Amazon Elastic Container Registry Public (Amazon ECR Public) is a
  managed service that allows you to host and manage container images in
  both public and private registries. You can utilize popular tools like the
  Docker CLI to push, pull, and manage images within a secure, scalable, and
  reliable registry for Docker or OCI images. This API specifically supports
  public repositories within Amazon ECR, while private repository
  functionality can be found in the Amazon Elastic Container Registry API
  Reference.

---