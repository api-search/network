---
api_count: 1
apis:
- description: The Amazon Forecast API provides programmatic access to create and manage datasets, predictors, forecasts, and export jobs for time-series forecasting using machine learning models.
  name: Amazon Forecast API
  slug: amazon-forecast-api
capabilities:
- description: 'Manage end-to-end time-series forecasting pipelines: datasets, predictors, and forecast generation.'
  name: Amazon Forecast Time Series Prediction
  slug: amazon-forecast-time-series-prediction
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/forecast/
- title: ''
  type: Website
  url: https://aws.amazon.com/forecast/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/forecast/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/machine-learning/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/forecast/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-forecast
- title: ''
  type: SpectralRules
  url: rules/amazon-forecast-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/forecast.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-forecast-time-series-prediction.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-forecast-vocabulary.yaml
- title: ''
  type: JSON-LD
  url: json-ld/amazon-forecast-context.jsonld
created: '2026-03-16'
description: Amazon Forecast is a fully managed service that uses machine learning to deliver highly accurate forecasts. It analyzes your historical time-series data and automatically selects the right machine learning algorithms to generate accurate forecasts with no machine learning expertise required.
features:
- description: Automatically evaluates and selects from over 60 ML algorithms to find the best fit for your time-series data.
  name: AutoML
- description: Generates quantile forecasts (p10, p50, p90) to estimate demand uncertainty and plan inventory buffers.
  name: Probabilistic Forecasts
- description: Pre-built domain configurations for retail, workforce, traffic, and cloud capacity forecasting.
  name: Domain-Specific Models
- description: Incorporate external factors (price, promotions, holidays) as related time-series data to improve accuracy.
  name: Related Time Series
- description: Automatic tuning of model hyperparameters to maximize forecast accuracy.
  name: HPO (Hyperparameter Optimization)
- description: Forecast Explainability reports show which features most impact each individual forecast.
  name: Explainability
- description: Export forecast results to Amazon S3 in CSV format for downstream consumption.
  name: S3 Export
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Import training datasets and export forecast results to S3.
  name: Amazon S3
- description: Transform and prepare time-series data for Forecast using AWS Glue ETL jobs.
  name: AWS Glue
- description: Combine Amazon Forecast with SageMaker for custom ML pipelines.
  name: Amazon SageMaker
- description: Control access to Forecast datasets, predictors, and forecasts with IAM policies.
  name: AWS IAM
- description: Monitor Forecast job status, errors, and API usage metrics.
  name: Amazon CloudWatch
- description: Encrypt Forecast datasets and training data with customer-managed KMS keys.
  name: AWS KMS
- description: Visualize exported forecast data in QuickSight dashboards.
  name: Amazon QuickSight
jsonld:
- class_count: 5
  name: Amazon Forecast Context
  property_count: 15
  slug: amazon-forecast-context
layout: provider
modified: '2026-04-19'
name: Amazon Forecast
rules:
- name: Amazon Forecast API Rules
  rule_count: 25
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 15
  slug: amazon-forecast-spectral-rules
skills: []
slug: amazon-forecast
solutions: []
tags:
- AWS
- Forecasting
- Machine Learning
- Predictive Analytics
- Time Series
url: https://raw.githubusercontent.com/api-evangelist/amazon-forecast/refs/heads/main/apis.yml
use_cases:
- description: Predict item-level sales for inventory planning and replenishment across stores.
  name: Retail Demand Forecasting
- description: Forecast staffing needs for contact centers and seasonal workforce management.
  name: Workforce Capacity Planning
- description: Predict EC2 capacity requirements to optimize reserved instance purchases.
  name: Cloud Resource Forecasting
- description: Forecast component and raw material demand to reduce stockouts and carrying costs.
  name: Supply Chain Optimization
- description: Project revenue by product, region, and channel for financial planning.
  name: Financial Revenue Forecasting
- description: Predict electricity load and generation requirements for grid balancing.
  name: Energy Load Forecasting
---
