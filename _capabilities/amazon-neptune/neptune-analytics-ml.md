---
consumed_apis:
- analytics
- ml
description: Workflow capability for Neptune Analytics graph analysis, vector search, and Neptune ML graph neural network model training and inference. Used by data scientists and ML engineers.
layout: capability
name: Amazon Neptune Analytics and Machine Learning
operations:
- description: List Neptune Analytics graphs
  method: GET
  name: list-analytics-graphs
  path: /v1/graphs
- description: List Neptune ML training jobs
  method: GET
  name: list-ml-jobs
  path: /v1/ml/jobs
personas: []
provider_name: Amazon Neptune
provider_slug: amazon-neptune
search_terms:
- neptune analytics graph management
- list neptune analytics graphs for in-memory graph analysis
- graph analytics
- create a neptune ml inference endpoint for predictions
- manages neptune clusters, instances, and infrastructure
- list ml jobs
- graph analytics, vector search, and ml model training and inference
- list neptune ml graph neural network training jobs
- neptune ml training job management
- machine learning
- list neptune ml training jobs
- data streaming
- Graph Database Administrator
- neptune
- ML Engineer
- gremlin
- create analytics graph
- list ml training jobs
- graph database management, querying, and data streaming
- writes gremlin, sparql, and opencypher queries against neptune
- database
- property graph
- performs graph analytics and builds ml models on graph data
- list analytics graphs
- trains and deploys neptune ml graph neural network models
- aws
- graph database
- sparql
- rdf
- create a neptune analytics graph for graph analytics workloads
- bulk loading
- Data Scientist
- Graph Developer
- create ml inference endpoint
- list neptune analytics graphs
- amazon neptune
slug: neptune-analytics-ml
tags:
- Amazon Neptune
- AWS
- Graph Analytics
- Machine Learning
tools:
- description: List Neptune Analytics graphs for in-memory graph analysis
  hints:
    readOnly: true
  name: list-analytics-graphs
- description: Create a Neptune Analytics graph for graph analytics workloads
  hints:
    readOnly: false
  name: create-analytics-graph
- description: List Neptune ML graph neural network training jobs
  hints:
    readOnly: true
  name: list-ml-training-jobs
- description: Create a Neptune ML inference endpoint for predictions
  hints:
    readOnly: false
  name: create-ml-inference-endpoint
---
