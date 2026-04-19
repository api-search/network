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
- list all search indexes
- search
- search index
- connect data source
- machine learning
- search index management
- index documents
- ai
- integrates kendra search into applications and rag pipelines
- knowledge management
- natural language
- amazon kendra
- search an index with natural language
- create a new amazon kendra enterprise search index
- IT Administrator
- enterprise knowledge organization and discovery
- create data source
- search an amazon kendra index using natural language query
- intelligent search and information retrieval
- Knowledge Manager
- create a new search index
- connect a data repository (s3, sharepoint, salesforce, etc.) to a kendra index
- add documents to an amazon kendra search index
- unified workflow for search index management, data connectivity, and query operations
- create index
- list data sources
- list all data source connectors for a kendra index
- aws
- list indexes
- data source connector management
- list all amazon kendra search indexes
- document management
- list data source connectors
- list search indexes
- Developer
- add documents to an index
- create search index
- manages enterprise knowledge bases and search indexes
- intelligent search
- configures and maintains data source connectors and index settings
- create a data source connector
- enterprise search
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
