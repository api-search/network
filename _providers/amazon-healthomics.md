---
api_count: 1
apis:
- description: The AWS HealthOmics API provides programmatic access to manage omics storage, workflows, run groups, annotation stores, and variant stores for genomics and other omics data analysis.
  name: AWS HealthOmics API
  slug: aws-healthomics-api
capabilities:
- description: ''
  name: Amazon Healthomics Genomics Operations
  slug: amazon-healthomics-genomics-operations
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/healthomics/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/omics/
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
  url: https://aws.amazon.com/blogs/industries/healthcare/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/omics/
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
  type: SDK
  url: https://aws.amazon.com/developer/tools/
- title: ''
  type: CLI
  url: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/index.html
- title: ''
  type: SpectralRules
  url: rules/amazon-healthomics-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-healthomics-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-healthomics-genomics-operations.yaml
created: '2026-03-16'
description: AWS HealthOmics is a purpose-built service for healthcare and life sciences organizations that helps store, query, and analyze genomic, transcriptomic, and other omics data to generate insights and accelerate scientific discoveries and improve healthcare.
features:
- description: Purpose-built storage for genomic, transcriptomic, and other omics data with automatic optimization.
  name: Omics Storage
- description: Run industry-standard bioinformatics tools and pipelines using WDL and Nextflow workflow definitions.
  name: Bioinformatics Workflows
- description: Store and query genomic annotation data from sources like ClinVar, Ensembl, and custom datasets.
  name: Annotation Stores
- description: Store and query genomic variant data in VCF and other standard bioinformatics formats.
  name: Variant Stores
- description: Efficiently store and retrieve genomic sequence read sets in FASTQ, BAM, and CRAM formats.
  name: Sequence Stores
- description: Store and access reference genome files for alignment and analysis workflows.
  name: Reference Genomes
- description: Fully managed compute infrastructure for running bioinformatics workflows at scale.
  name: Managed Compute
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Import and export omics data using S3 as the primary data source and destination.
  name: Amazon S3
- description: Control access to HealthOmics resources using IAM roles and policies.
  name: AWS IAM
- description: Monitor HealthOmics workflows and storage operations through CloudWatch metrics.
  name: Amazon CloudWatch
- description: Govern and secure genomic data lake access using Lake Formation permissions.
  name: AWS Lake Formation
- description: Query genomic annotation and variant data stored in HealthOmics using Athena.
  name: Amazon Athena
- description: Supplement HealthOmics workflows with custom compute jobs using AWS Batch.
  name: AWS Batch
jsonld:
- class_count: 459
  name: Amazon Healthomics Context
  property_count: 0
  slug: amazon-healthomics-context
layout: provider
modified: '2026-04-19'
name: Amazon HealthOmics
rules:
- name: Amazon HealthOmics API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 3
    warn: 2
  slug: amazon-healthomics-spectral-rules
skills: []
slug: amazon-healthomics
solutions: []
tags:
- AWS
- Bioinformatics
- Genomics
- Healthcare
- Life Sciences
- Cloud Computing
url: https://raw.githubusercontent.com/api-evangelist/amazon-healthomics/refs/heads/main/apis.yml
use_cases:
- description: Store, analyze, and interpret whole genome sequencing data for research and clinical applications.
  name: Whole Genome Sequencing
- description: Run standard variant calling workflows on genomic data to identify genetic variants.
  name: Variant Calling Pipelines
- description: Analyze genomic data to understand drug response and develop personalized medicine approaches.
  name: Pharmacogenomics Research
- description: Process and analyze large-scale genomic datasets across patient populations for research.
  name: Population Genomics
- description: Support clinical genomics workflows for diagnosis and treatment of genetic disorders.
  name: Clinical Genomics
---
