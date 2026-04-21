---
consumed_apis:
- kendra
description: Unified workflow capability for Amazon Kendra enterprise search, combining index management, data source connectivity, document indexing, and intelligent query operations for knowledge management and RAG workflows.
layout: capability
name: Amazon Kendra Enterprise Search
operations:
- description: Create a new search index
  method: POST
  name: create-index
  path: /v1/indexes
- description: List all search indexes
  method: GET
  name: list-indexes
  path: /v1/indexes
- description: Search an index with natural language
  method: POST
  name: search
  path: /v1/indexes/{IndexId}/query
- description: Create a data source connector
  method: POST
  name: create-data-source
  path: /v1/indexes/{IndexId}/data-sources
- description: List data source connectors
  method: GET
  name: list-data-sources
  path: /v1/indexes/{IndexId}/data-sources
- description: Add documents to an index
  method: POST
  name: index-documents
  path: /v1/indexes/{IndexId}/documents
personas: []
provider_name: Amazon Kendra
provider_slug: amazon-kendra
search_terms:
- IT Administrator
- list all amazon kendra search indexes
- create search index
- knowledge management
- natural language
- create a new search index
- list all data source connectors for a kendra index
- search
- connect a data repository (s3, sharepoint, salesforce, etc.) to a kendra index
- list all search indexes
- intelligent search
- create a data source connector
- amazon kendra
- document management
- configures and maintains data source connectors and index settings
- machine learning
- create index
- ai
- search an amazon kendra index using natural language query
- add documents to an index
- create a new amazon kendra enterprise search index
- list data sources
- list data source connectors
- Knowledge Manager
- Developer
- search index management
- search an index with natural language
- search index
- data source connector management
- list search indexes
- add documents to an amazon kendra search index
- enterprise knowledge organization and discovery
- aws
- manages enterprise knowledge bases and search indexes
- integrates kendra search into applications and rag pipelines
- unified workflow for search index management, data connectivity, and query operations
- enterprise search
- create data source
- intelligent search and information retrieval
- list indexes
- index documents
- connect data source
slug: amazon-kendra-enterprise-search
tags:
- Amazon Kendra
- Enterprise Search
- Machine Learning
- AWS
- Knowledge Management
tools:
- description: Create a new Amazon Kendra enterprise search index
  hints:
    idempotent: false
    readOnly: false
  name: create-search-index
- description: List all Amazon Kendra search indexes
  hints:
    idempotent: true
    readOnly: true
  name: list-search-indexes
- description: Search an Amazon Kendra index using natural language query
  hints:
    openWorld: true
    readOnly: true
  name: search-index
- description: Connect a data repository (S3, SharePoint, Salesforce, etc.) to a Kendra index
  hints:
    idempotent: false
    readOnly: false
  name: connect-data-source
- description: List all data source connectors for a Kendra index
  hints:
    idempotent: true
    readOnly: true
  name: list-data-sources
- description: Add documents to an Amazon Kendra search index
  hints:
    idempotent: false
    readOnly: false
  name: index-documents
---
