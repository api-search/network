---
api_count: 3
apis:
- description: RESTful API for Amazon S3 storage operations including bucket management, object operations, and access control.
  name: Amazon S3 REST API
  slug: ''
- description: Amazon S3 Control provides API operations for managing S3 account-level settings, access points, Batch Operations jobs, S3 Access Grants, Multi-Region Access Points, and Storage Lens configurations.
  name: Amazon S3 Control API
  slug: ''
- description: Amazon S3 Tables API provides operations for managing table buckets and tables stored in Apache Iceberg format, enabling structured tabular data storage in Apache Parquet format within Amazon S3.
  name: Amazon S3 Tables API
  slug: ''
capabilities:
- description: Unified capability for Amazon S3 storage management combining object storage operations, account-level controls, and tabular data management. Used by cloud engineers, data engineers, and platform team
  name: Amazon S3 Storage Management
  slug: storage-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/s3/
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
  url: https://aws.amazon.com/blogs/storage/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/s3/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: Login
  url: https://aws.amazon.com/console/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-s3
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Security
  url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/security.html
- title: ''
  type: Compliance
  url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-compliance.html
- title: ''
  type: ChangeLog
  url: https://docs.aws.amazon.com/AmazonS3/latest/API/WhatsNew.html
created: '2024-01-15'
description: Amazon Simple Storage Service (S3) is an object storage service offering industry-leading scalability, data availability, security, and performance.
features:
- Industry-leading scalability and 99.999999999% durability
- Multiple storage classes for cost optimization
- Object versioning and lifecycle management
- Server-side encryption and access control
- S3 Object Lock for WORM compliance
- Cross-region and same-region replication
- S3 Tables for Apache Iceberg tabular data
- S3 Access Grants for identity-based access
- Storage Lens analytics and insights
- Batch Operations for large-scale object processing
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- AWS Lambda
- Amazon CloudFront
- Amazon Athena
- AWS Glue
- Amazon EMR
- Amazon Redshift
- AWS CloudTrail
- Amazon EventBridge
jsonld:
- class_count: 10
  name: Amazon S3 Context
  property_count: 11
  slug: amazon-s3-context
- class_count: 0
  name: Amazon S3 Control Context
  property_count: 0
  slug: amazon-s3-control-context
- class_count: 0
  name: Amazon S3 Rest Context
  property_count: 0
  slug: amazon-s3-rest-context
- class_count: 0
  name: Amazon S3 Tables Context
  property_count: 0
  slug: amazon-s3-tables-context
layout: provider
modified: '2026-04-18'
name: Amazon S3
rules:
- name: Amazon S3 API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: amazon-s3-spectral-rules
skills: []
slug: amazon-s3
solutions: []
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
url: https://aws.amazon.com/s3/
use_cases:
- Storing and serving static website content
- Data lake foundation for analytics workloads
- Backup and disaster recovery storage
- Archive storage with Glacier integration
- Hosting machine learning training datasets
- Storing application logs and audit trails
---
