---
aid: amazon-web-services:amazon-sagemaker-feature-store
name: Amazon SageMaker Feature Store
tags:
  - Batches
  - Record
  - Feature
  - Groups
  - Names
  - Machine Learning
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/sagemaker/feature-store/
overlays:
  - url: overlays/sagemaker-featurestore-runtime-openapi-search.yml
    type: APIs.io Search
  - url: |-

      overlays/sagemaker-featurestore-runtime-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/sagemaker/feature-store/
    type: Documentation
  - url: openapi/sagemaker-featurestore-runtime-openapi-original.yml
    type: OpenAPI
description: |-

  The Amazon SageMaker Feature Store is a fully managed repository
  specifically designed for storing, sharing, and managing features for
  machine learning (ML) models. Features are the inputs necessary for ML
  models during both training and inference. 

---