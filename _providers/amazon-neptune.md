---
api_count: 9
apis:
- description: Amazon Neptune Management API for creating, managing, and deleting Neptune DB clusters, instances, parameter groups, snapshots, and related infrastructure resources.
  name: Amazon Neptune Management API
  slug: ''
- description: Amazon Neptune Data API provides SDK support for more than 40 data operations including data loading, query execution, data inquiry, and machine learning. It supports Gremlin and openCypher query lang
  name: Amazon Neptune Data API
  slug: ''
- description: Apache TinkerPop Gremlin graph traversal language API for querying property graphs in Neptune. It supports both WebSocket and HTTP REST endpoints for submitting Gremlin traversals.
  name: Neptune Gremlin API
  slug: ''
- description: W3C SPARQL 1.1 query language API for querying RDF graphs in Neptune. It provides an HTTP REST endpoint compatible with the SPARQL 1.1 protocol specification.
  name: Neptune SPARQL API
  slug: ''
- description: openCypher graph query language API for querying property graphs with Cypher syntax in Neptune. It provides an HTTP endpoint for executing openCypher queries against property graph data.
  name: Neptune openCypher API
  slug: ''
- description: Neptune Streams generates a complete sequence of change-log entries that record every change made to graph data as it happens, enabling real-time capture of graph mutations via a REST API.
  name: Neptune Streams API
  slug: ''
- description: Neptune bulk loader API for ingesting large volumes of data from Amazon S3 into a Neptune DB instance. It supports CSV formats for property graphs and multiple RDF serialization formats.
  name: Neptune Loader API
  slug: ''
- description: Neptune ML enables machine learning on graph data using graph neural networks. It provides APIs for data processing, model training, and inference endpoint management powered by Amazon SageMaker.
  name: Neptune ML API
  slug: ''
- description: Neptune Analytics is a memory-optimized graph database engine for analytics, providing optimized graph analytic algorithms, low-latency queries, and vector search capabilities within graph traversals.
  name: Neptune Analytics API
  slug: ''
capabilities:
- description: Workflow capability for Neptune Analytics graph analysis, vector search, and Neptune ML graph neural network model training and inference. Used by data scientists and ML engineers.
  name: Amazon Neptune Analytics and Machine Learning
  slug: neptune-analytics-ml
- description: Workflow capability for managing Neptune graph databases, executing queries across Gremlin, SPARQL, and openCypher, and monitoring data streams. Used by graph database administrators and developers.
  name: Amazon Neptune Graph Data Management
  slug: neptune-graph-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/neptune/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/neptune/
- title: ''
  type: Getting Started
  url: https://aws.amazon.com/neptune/getting-started/
- title: ''
  type: Authentication
  url: https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth.html
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/database/category/database/amazon-neptune/
- title: ''
  type: Change Log
  url: https://docs.aws.amazon.com/neptune/latest/userguide/doc-history.html
- title: ''
  type: Release Notes
  url: https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases.html
- title: ''
  type: Status
  url: https://health.aws.amazon.com/
- title: ''
  type: Support
  url: https://repost.aws/tags/TAxVAEdWg1SrS0lClUSX-m_Q
- title: ''
  type: Terms of Service
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: Privacy Policy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: GitHub Organization
  url: https://github.com/aws
- title: ''
  type: Community
  url: https://repost.aws/
- title: ''
  type: Website
  url: https://aws.amazon.com/neptune/
- title: ''
  type: Login
  url: https://console.aws.amazon.com/neptune/
- title: ''
  type: Sign Up
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: FAQs
  url: https://aws.amazon.com/neptune/faqs/
- title: ''
  type: Security
  url: https://docs.aws.amazon.com/neptune/latest/userguide/security.html
- title: ''
  type: Service Level Agreement
  url: https://aws.amazon.com/neptune/sla/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/neptune/
- title: ''
  type: GitHub Samples
  url: https://github.com/aws-samples/amazon-neptune-samples
- title: ''
  type: SDKs
  url: https://docs.aws.amazon.com/neptune/latest/userguide/using-neptune-apis.html
- title: ''
  type: Tools
  url: https://github.com/awslabs/amazon-neptune-tools
- title: ''
  type: Pricing
  url: https://aws.amazon.com/neptune/pricing/
- title: ''
  type: JSON-LD
  url: json-ld/amazon-neptune-context.jsonld
- title: DB Cluster Schema
  type: JSONSchema
  url: json-schema/amazon-neptune-db-cluster-schema.json
- title: DB Instance Schema
  type: JSONSchema
  url: json-schema/amazon-neptune-db-instance-schema.json
- title: Graph Element Schema
  type: JSONSchema
  url: json-schema/amazon-neptune-graph-element-schema.json
- title: Loader Job Schema
  type: JSONSchema
  url: json-schema/amazon-neptune-loader-job-schema.json
- title: Stream Record Schema
  type: JSONSchema
  url: json-schema/amazon-neptune-stream-record-schema.json
- title: Analytics Graph Schema
  type: JSONSchema
  url: json-schema/amazon-neptune-analytics-graph-schema.json
- title: ML Job Schema
  type: JSONSchema
  url: json-schema/amazon-neptune-ml-job-schema.json
- title: ''
  type: SpectralRules
  url: rules/amazon-neptune-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-neptune-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/neptune-graph-management.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/neptune-analytics-ml.yaml
- title: Analytics Context
  type: JSON-LD
  url: json-ld/amazon-neptune-analytics-context.jsonld
- title: Data Context
  type: JSON-LD
  url: json-ld/amazon-neptune-data-context.jsonld
- title: Gremlin Context
  type: JSON-LD
  url: json-ld/amazon-neptune-gremlin-context.jsonld
- title: Loader Context
  type: JSON-LD
  url: json-ld/amazon-neptune-loader-context.jsonld
- title: Management Context
  type: JSON-LD
  url: json-ld/amazon-neptune-management-context.jsonld
- title: Ml Context
  type: JSON-LD
  url: json-ld/amazon-neptune-ml-context.jsonld
- title: Opencypher Context
  type: JSON-LD
  url: json-ld/amazon-neptune-opencypher-context.jsonld
- title: Sparql Context
  type: JSON-LD
  url: json-ld/amazon-neptune-sparql-context.jsonld
- title: Streams Context
  type: JSON-LD
  url: json-ld/amazon-neptune-streams-context.jsonld
created: '2024'
description: Amazon Neptune is a fast, reliable, fully managed graph database service that makes it easy to build and run applications that work with highly connected datasets. It supports property graph and RDF models, with multiple query languages including Gremlin, SPARQL, and openCypher.
features:
- description: Automatically scales compute and memory resources based on workload demands without requiring capacity planning.
  name: Serverless Graph Database
- description: Supports Apache TinkerPop Gremlin, openCypher, and SPARQL 1.1 query languages for property graph and RDF models.
  name: Multiple Query Language Support
- description: Multi-AZ deployment with up to 15 read replicas, automated failover, and continuous backups with point-in-time recovery up to 35 days.
  name: High Availability
- description: Multi-region replication with sub-second latency across up to five secondary clusters for global applications.
  name: Global Database
- description: Memory-optimized graph analytics engine for analyzing tens of billions of relationships within seconds with vector search capabilities.
  name: Neptune Analytics
- description: Fully managed GraphRAG with Amazon Bedrock Knowledge Bases for AI-enhanced graph retrieval augmented generation.
  name: GraphRAG Support
- description: Native graph neural network support via Neptune ML powered by Amazon SageMaker for link prediction and node classification.
  name: Machine Learning on Graphs
- description: Full ACID transaction support ensuring data consistency and integrity across graph operations.
  name: ACID Transactions
- description: VPC network isolation, IAM resource permissions, AWS KMS encryption, TLS in-transit encryption, and CloudWatch audit logging.
  name: AWS Security Integration
- description: Storage automatically grows up to 128 TiB with self-healing architecture spanning three availability zones.
  name: Auto-Expanding Storage
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Integration with Bedrock Knowledge Bases for fully managed GraphRAG and AI-enhanced knowledge graph applications.
  name: Amazon Bedrock
- description: Neptune ML uses SageMaker for training graph neural network models on Neptune graph data.
  name: Amazon SageMaker
- description: Bulk data loading from S3 using the Neptune Loader API with CSV and RDF serialization format support.
  name: Amazon S3
- description: Fine-grained resource-level access control and role-based permissions via AWS Identity and Access Management.
  name: AWS IAM
- description: Metrics, logs, and audit logging for monitoring Neptune cluster performance and compliance.
  name: Amazon CloudWatch
- description: Encryption at rest using AWS Key Management Service for customer-managed key support.
  name: AWS KMS
- description: Network isolation using Amazon Virtual Private Cloud with security group and firewall controls.
  name: Amazon VPC
- description: Gremlin graph traversal language and TinkerPop ecosystem integration for property graph querying.
  name: Apache TinkerPop
- description: Integration with Strands AI Agents SDK and popular agentic memory tools for AI agent applications.
  name: Strands AI Agents SDK
jsonld:
- class_count: 13
  name: Amazon Neptune Analytics Context
  property_count: 44
  slug: amazon-neptune-analytics-context
- class_count: 10
  name: Amazon Neptune Context
  property_count: 15
  slug: amazon-neptune-context
- class_count: 26
  name: Amazon Neptune Data Context
  property_count: 120
  slug: amazon-neptune-data-context
- class_count: 5
  name: Amazon Neptune Gremlin Context
  property_count: 20
  slug: amazon-neptune-gremlin-context
- class_count: 5
  name: Amazon Neptune Loader Context
  property_count: 21
  slug: amazon-neptune-loader-context
- class_count: 14
  name: Amazon Neptune Management Context
  property_count: 56
  slug: amazon-neptune-management-context
- class_count: 10
  name: Amazon Neptune Ml Context
  property_count: 50
  slug: amazon-neptune-ml-context
- class_count: 7
  name: Amazon Neptune Opencypher Context
  property_count: 21
  slug: amazon-neptune-opencypher-context
- class_count: 5
  name: Amazon Neptune Sparql Context
  property_count: 22
  slug: amazon-neptune-sparql-context
- class_count: 6
  name: Amazon Neptune Streams Context
  property_count: 20
  slug: amazon-neptune-streams-context
layout: provider
modified: '2026-04-19'
name: Amazon Neptune
rules:
- name: Amazon Neptune API Rules
  rule_count: 25
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 11
  slug: amazon-neptune-spectral-rules
skills: []
slug: amazon-neptune
solutions: []
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
url: ''
use_cases:
- description: Build knowledge graphs to enhance AI accuracy, comprehensiveness, and explainability using GraphRAG with Amazon Bedrock.
  name: Knowledge Graphs and GraphRAG
- description: Model transaction and account relationship networks to detect fraudulent patterns in near real-time using graph traversals.
  name: Fraud Detection
- description: Build unified customer profile graphs linking purchases, preferences, and interactions for personalization and marketing.
  name: Customer 360
- description: Model IT infrastructure as a connected graph to detect attack paths, anomalies, and proactive threats.
  name: Cybersecurity and Threat Detection
- description: Power product and content recommendation engines by traversing user-item relationship graphs.
  name: Recommendation Engines
- description: Model and query highly connected social graph data for applications requiring relationship traversal at scale.
  name: Social Networks
- description: Map network topology, dependencies, and configuration relationships for operations and impact analysis.
  name: Network and IT Operations
- description: Model complex supply chain relationships and dependencies for optimization and risk analysis.
  name: Supply Chain Management
---
