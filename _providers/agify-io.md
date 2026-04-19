---
api_count: 1
apis:
- description: Predict the age of a person based on their first name. Returns an estimated age, data count used for the prediction, and optionally a country-localized estimate. Supports single name and batch request
  name: Agify.io Predict Age API
  slug: predict-age-api
common:
- title: ''
  type: Portal
  url: https://agify.io/
- title: ''
  type: Documentation
  url: https://agify.io/documentation
- title: ''
  type: Pricing
  url: https://agify.io/#pricing
- title: ''
  type: RateLimits
  url: ''
created: '2025-01-07'
description: Agify.io is a simple REST API that predicts the age of a person based on their first name. Using a large dataset of name-age associations, it returns an estimated age along with a count of how many data points were used and the name's country-localized variant when a country code is provided. Supports batch requests for up to 10 names per call. Used for demographics research, content personalization, and marketing segmentation.
features:
- description: Estimates a person's age from their first name using a large statistical dataset of name-age associations.
  name: Name-Based Age Prediction
- description: Accepts an optional ISO 3166-1 country code to return country-specific age predictions for the given name.
  name: Country Localization
- description: Supports up to 10 names per API request using array parameter syntax for efficient bulk predictions.
  name: Batch Processing
- description: Returns X-Rate-Limit-Limit, X-Rate-Limit-Remaining, and X-Rate-Limit-Reset headers to track API usage and quota.
  name: Rate Limit Headers
- description: Free access for up to 100 requests per day without an API key, making it easy to evaluate the service.
  name: Free Tier
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Sibling API that predicts gender based on first name — commonly used alongside Agify for demographic profiling.
  name: Genderize.io
- description: Sibling API that predicts nationality from first name, completing a demographic analysis trifecta with Agify and Genderize.
  name: Nationalize.io
jsonld:
- class_count: 2
  name: Agify Io Context
  property_count: 3
  slug: agify-io-context
layout: provider
modified: '2026-04-19'
name: Agify.io
skills: []
slug: agify-io
solutions: []
tags:
- Age Prediction
- Name Analysis
- Demographics
- REST API
url: https://raw.githubusercontent.com/api-evangelist/agify-io/refs/heads/main/apis.yml
use_cases:
- description: Analyze name datasets to estimate age distributions across a user base for research and analytics purposes.
  name: Demographics Research
- description: Tailor content or product recommendations based on estimated age derived from a user's provided first name.
  name: Content Personalization
- description: Segment leads and customers by estimated age group for targeted marketing campaigns without requiring date-of-birth collection.
  name: Marketing Segmentation
- description: Provide age-range hints during user registration to improve form completion rates and data accuracy.
  name: Form Pre-Fill Assistance
---
