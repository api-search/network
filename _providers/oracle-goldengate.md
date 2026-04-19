---
api_count: 6
apis:
- description: RESTful API for managing Oracle GoldenGate Microservices Architecture, including deployment configuration, process management, and monitoring.
  name: Oracle GoldenGate REST API
  slug: ''
- description: API for managing Oracle GoldenGate for Big Data deployments, allowing integration with Hadoop, Kafka, and other big data targets.
  name: Oracle GoldenGate for Big Data REST API
  slug: ''
- description: API for Oracle GoldenGate Veridata to verify and compare data between source and target systems.
  name: Oracle GoldenGate Veridata REST API
  slug: ''
- description: Oracle Cloud Infrastructure API for managing GoldenGate deployments in OCI.
  name: Oracle GoldenGate Cloud Service API
  slug: ''
- description: REST API for managing Oracle GoldenGate Stream Analytics pipelines, enabling real-time event stream processing, monitoring, and dashboard creation.
  name: Oracle GoldenGate Stream Analytics REST API
  slug: ''
- description: REST API for distributing and managing Oracle GoldenGate data streams, enabling real-time data distribution to downstream consumers.
  name: Oracle GoldenGate Data Streams REST API
  slug: ''
capabilities:
- description: Unified workflow for managing Oracle GoldenGate cloud deployments in OCI. Combines the OCI Cloud Service API with Stream Analytics for cloud platform administrators managing deployment lifecycle, conn
  name: Oracle GoldenGate Cloud Management
  slug: cloud-management
- description: Unified workflow for managing real-time data replication across on-premises and cloud environments. Combines the core GoldenGate REST API, Big Data API, and Data Streams API for data integration engin
  name: Oracle GoldenGate Data Replication
  slug: data-replication
- description: Unified workflow for verifying data consistency between source and target databases. Combines Veridata for data comparison and repair with core GoldenGate monitoring for data quality engineers and DBA
  name: Oracle GoldenGate Data Verification
  slug: data-verification
common:
- title: ''
  type: Portal
  url: https://www.oracle.com/integration/goldengate/
- title: ''
  type: Blog
  url: https://blogs.oracle.com/dataintegration/
- title: ''
  type: Pricing
  url: https://www.oracle.com/integration/goldengate/pricing/
- title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/middleware/goldengate/core/21.3/index.html
- title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- title: ''
  type: Documentation
  url: https://docs.oracle.com/en/cloud/paas/goldengate-service/docs.html
- title: ''
  type: SignUp
  url: https://www.oracle.com/cloud/free/
- title: ''
  type: Login
  url: https://cloud.oracle.com/
- title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- title: ''
  type: Support
  url: https://support.oracle.com
- title: ''
  type: KnowledgeCenter
  url: https://www.oracle.com/integration/goldengate/knowledge-hub/
- title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- title: ''
  type: GitHubRepository
  url: https://github.com/oracle/docker-images/tree/main/OracleGoldenGate
- title: ''
  type: Training
  url: https://education.oracle.com/data-integration/goldengate/product_148
- title: ''
  type: Tutorials
  url: https://docs.oracle.com/en/cloud/paas/goldengate-service/tutorials.html
- title: ''
  type: ReleaseNotes
  url: https://docs.oracle.com/en/database/goldengate/core/26/release-notes/
- title: ''
  type: JSONSchema
  url: json-schema/oracle-goldengate-deployment-schema.json
- title: ''
  type: JSONLD
  url: json-ld/oracle-goldengate-context.jsonld
created: '2024-01-15'
description: Oracle GoldenGate enables real-time data integration and replication in heterogeneous IT environments. These APIs provide programmatic access to manage and monitor GoldenGate deployments, processes, and configurations.
features:
- Real-time data replication across heterogeneous databases
- Change data capture (CDC) with minimal impact on source systems
- Zero-downtime migration and database upgrades
- Multi-cloud and hybrid cloud data integration
- Bidirectional replication for active-active architectures
- Stream analytics for real-time event processing
- Data verification and repair with Veridata
- Big data target support including Kafka, HDFS, and MongoDB
image: /assets/icons/oracle-goldengate.png
integrations:
- Oracle Database
- MySQL
- PostgreSQL
- SQL Server
- MongoDB
- Apache Kafka
- Apache Hadoop / HDFS
- Elasticsearch
- Google BigQuery
- Amazon Kinesis
- Snowflake
- Oracle Cloud Infrastructure
jsonld:
- class_count: 0
  name: Oracle Goldengate Big Data Rest Context
  property_count: 0
  slug: oracle-goldengate-big-data-rest-context
- class_count: 0
  name: Oracle Goldengate Cloud Service Context
  property_count: 0
  slug: oracle-goldengate-cloud-service-context
- class_count: 0
  name: Oracle Goldengate Context
  property_count: 16
  slug: oracle-goldengate-context
- class_count: 0
  name: Oracle Goldengate Data Streams Rest Context
  property_count: 0
  slug: oracle-goldengate-data-streams-rest-context
- class_count: 0
  name: Oracle Goldengate Rest Context
  property_count: 0
  slug: oracle-goldengate-rest-context
- class_count: 0
  name: Oracle Goldengate Stream Analytics Rest Context
  property_count: 0
  slug: oracle-goldengate-stream-analytics-rest-context
- class_count: 0
  name: Oracle Goldengate Veridata Rest Context
  property_count: 0
  slug: oracle-goldengate-veridata-rest-context
layout: provider
modified: '2026-04-18'
name: Oracle GoldenGate
rules:
- name: Oracle GoldenGate API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: oracle-goldengate-spectral-rules
skills: []
slug: oracle-goldengate
solutions: []
tags:
- CDC
- Data Integration
- Data Synchronization
- Database
- Enterprise
- Real-Time Replication
url: https://raw.githubusercontent.com/api-evangelist/oracle-goldengate/refs/heads/main/apis.yml
use_cases:
- Real-time data warehouse loading and synchronization
- Database migration with zero downtime
- Active-active database replication for high availability
- Streaming data to big data platforms (Kafka, Hadoop, Elasticsearch)
- Cloud migration from on-premises Oracle databases to OCI
- Data verification and compliance auditing
- Real-time analytics pipeline construction
---
