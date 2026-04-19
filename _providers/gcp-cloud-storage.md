---
api_count: 2
apis:
- description: RESTful API for interacting with Google Cloud Storage buckets and objects.
  name: Google Cloud Storage JSON API
  slug: ''
- description: Amazon S3-compatible XML API for Google Cloud Storage.
  name: Google Cloud Storage XML API
  slug: ''
capabilities:
- description: Unified workflow for managing cloud storage buckets, objects, access controls, and IAM policies. Used by cloud engineers and data platform teams.
  name: Google Cloud Storage Management
  slug: cloud-storage
common:
- title: ''
  type: GettingStarted
  url: https://cloud.google.com/storage/docs/quickstarts
- title: ''
  type: SDK
  url: https://cloud.google.com/storage/docs/reference/libraries
- title: ''
  type: Console
  url: https://console.cloud.google.com/storage
- title: ''
  type: Blog
  url: https://cloud.google.com/blog/products/storage-data-transfer
- title: ''
  type: ChangeLog
  url: https://cloud.google.com/storage/docs/release-notes
- title: ''
  type: BestPractices
  url: https://cloud.google.com/storage/docs/best-practices
- title: ''
  type: Security
  url: https://cloud.google.com/storage/docs/security
- title: ''
  type: Compliance
  url: https://cloud.google.com/security/compliance
- title: ''
  type: APIReference
  url: https://cloud.google.com/storage/docs/apis
- title: ''
  type: CLI
  url: https://cloud.google.com/storage/docs/discover-object-storage-gsutil
- title: ''
  type: SpectralRules
  url: rules/gcp-cloud-storage-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/gcp-cloud-storage-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/cloud-storage.yaml
created: '2024-01-01'
description: Object storage service offering high durability, availability, and scalability for storing and accessing data on Google Cloud Platform.
features:
- description: Store data across multiple regions for high availability and low-latency access worldwide.
  name: Multi-Regional Storage
- description: Automatically transition objects between storage classes or delete them based on configurable rules.
  name: Object Lifecycle Management
- description: Maintain multiple versions of objects for data protection and recovery.
  name: Versioning
- description: Control access using IAM policies, ACLs, and signed URLs for secure data sharing.
  name: Fine-Grained Access Control
- description: Compose multiple objects into a single object without downloading and re-uploading data.
  name: Object Composition
- description: Watch for changes to objects in a bucket and receive push notifications.
  name: Change Notifications
- description: Lock retention policies to prevent object deletion for regulatory compliance.
  name: Retention Policies
image: https://cloud.google.com/images/social-icon-google-cloud-1200-630.png
integrations:
- description: Load data directly from Cloud Storage into BigQuery for analytics and data warehousing.
  name: BigQuery
- description: Trigger serverless functions on object creation, deletion, or metadata changes.
  name: Cloud Functions
- description: Process data stored in Cloud Storage using Apache Beam pipelines.
  name: Dataflow
- description: Transfer data between on-premises storage, other clouds, and Cloud Storage.
  name: Transfer Service
- description: Cache and serve Cloud Storage content through Google's global edge network.
  name: Cloud CDN
jsonld:
- class_count: 0
  name: Gcp Cloud Storage Context
  property_count: 6
  slug: gcp-cloud-storage-context
- class_count: 0
  name: Gcp Cloud Storage Json Context
  property_count: 0
  slug: gcp-cloud-storage-json-context
layout: provider
modified: '2026-04-18'
name: Google Cloud Storage
rules:
- name: Google Cloud Storage API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: gcp-cloud-storage-spectral-rules
skills: []
slug: gcp-cloud-storage
solutions: []
tags:
- Archival
- Backup
- Blob Storage
- Cloud Storage
- Data
- File Storage
- Google Cloud
- Object Storage
- Storage
url: https://cloud.google.com/storage
use_cases:
- description: Store structured and unstructured data at scale for analytics and machine learning pipelines.
  name: Data Lake Storage
- description: Store backups with configurable retention and cross-region replication for business continuity.
  name: Backup and Disaster Recovery
- description: Serve static web content directly from Cloud Storage buckets with custom domains.
  name: Static Website Hosting
- description: Store and serve media assets with CDN integration for low-latency content delivery.
  name: Media Content Delivery
---
