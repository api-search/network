---
api_count: 1
apis:
- description: The AWS Glue DataBrew API provides programmatic access to create and manage datasets, recipes, projects, jobs, and rulesets for visual data preparation and transformation workflows.
  name: AWS Glue DataBrew API
  slug: aws-glue-databrew-api
capabilities:
- description: 'Workflow capability for data analysts and data scientists preparing data using Amazon Glue DataBrew. Covers dataset management, recipe creation, job execution, and profiling for analytics and machine '
  name: Amazon Glue DataBrew Data Preparation
  slug: amazon-glue-databrew-data-preparation
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/glue/features/databrew/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/databrew/
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
  url: https://aws.amazon.com/blogs/big-data/tag/aws-glue-databrew/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/databrew/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-glue-databrew-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-glue-databrew-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-glue-databrew-data-preparation.yaml
created: '2026-03-16'
description: AWS Glue DataBrew is a visual data preparation tool that makes it easy for data analysts and data scientists to clean and normalize data to prepare it for analytics and machine learning. It provides over 250 pre-built transformations to automate data preparation tasks.
features:
- description: Apply over 250 ready-to-use transformations without writing code, including filtering, normalizing, aggregating, and reformatting data.
  name: 250+ Pre-Built Transformations
- description: Interactive visual interface to explore and transform data without writing code.
  name: Visual Data Preparation Interface
- description: Save transformation steps as reusable recipes that can be versioned and shared across teams.
  name: Recipe-Based Transformations
- description: Automatically profile datasets to understand data quality, distribution, and statistics.
  name: Data Profiling
- description: Define and enforce data quality rules with rulesets to validate data before processing.
  name: Data Quality Rules
- description: Create shared projects for team-based data preparation with centralized management.
  name: Collaborative Projects
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Read input datasets from and write transformed output to S3 buckets.
  name: Amazon S3
- description: Connect to Glue Data Catalog tables as data sources.
  name: AWS Glue Data Catalog
- description: Connect to Redshift databases as data sources for preparation.
  name: Amazon Redshift
- description: Use RDS databases as input sources for DataBrew transformation.
  name: Amazon RDS
- description: Integrate with Lake Formation for secure data lake access.
  name: AWS Lake Formation
jsonld:
- class_count: 122
  name: Amazon Glue Databrew Context
  property_count: 152
  slug: amazon-glue-databrew-context
layout: provider
modified: '2026-04-19'
name: Amazon Glue DataBrew
rules:
- name: Amazon Glue DataBrew API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: amazon-glue-databrew-spectral-rules
skills: []
slug: amazon-glue-databrew
solutions: []
tags:
- AWS
- Data Analytics
- Data Preparation
- ETL
- Machine Learning
url: https://raw.githubusercontent.com/api-evangelist/amazon-glue-databrew/refs/heads/main/apis.yml
use_cases:
- description: Clean, normalize, and transform raw data for business analytics dashboards and reports.
  name: Analytics Data Preparation
- description: Prepare and transform features from raw data for training machine learning models.
  name: Machine Learning Feature Engineering
- description: Profile datasets and apply quality rules to ensure data meets standards before processing.
  name: Data Quality Validation
- description: Automate recurring data transformation jobs as part of data pipeline workflows.
  name: ETL Pipeline Automation
---
