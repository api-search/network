---
consumed_apis:
- snowflake-cortex-analyst
- snowflake-cortex-inference
- snowflake-cortex-search
- snowflake-notebook
description: Unified workflow for AI and ML capabilities including LLM inference, natural language analytics, semantic search, and notebook-based development. Used by Data Scientists and ML Engineers for AI-powered data exploration and model deployment.
layout: capability
name: Snowflake Cortex AI
operations:
- description: Ask a question about your data
  method: POST
  name: send-analyst-message
  path: /v1/analyst/messages
- description: Run LLM completion
  method: POST
  name: complete
  path: /v1/inference/complete
- description: List available LLM models
  method: GET
  name: list-models
  path: /v1/inference/models
- description: Query a search service
  method: POST
  name: query-search
  path: /v1/search
- description: List notebooks
  method: GET
  name: list-notebooks
  path: /v1/notebooks
- description: Create a notebook
  method: POST
  name: create-notebook
  path: /v1/notebooks
personas: []
provider_name: Snowflake
provider_slug: snowflake
search_terms:
- run llm completion
- list models
- data sharing
- data lakes
- query a cortex search service
- create notebook
- send analyst feedback
- llm inference
- complete
- list available cortex llm models
- available models
- llm complete
- send analyst message
- data warehousing
- generate query suggestions
- list search services
- list llm models
- ask a question about your data using natural language
- sql
- snowflake
- cortex
- send feedback on an analyst response
- list available llm models
- create a notebook
- generate verified query suggestions
- list cortex search services
- notebook management
- ask analyst
- execute a notebook
- query search
- ai
- query a search service
- run llm inference completion
- database
- list notebooks
- execute notebook
- natural language data analytics
- ask a question about your data
- semantic search
- machine learning
slug: cortex-ai
tags:
- Snowflake
- Cortex
- AI
- Machine Learning
tools:
- description: Ask a question about your data using natural language
  hints:
    readOnly: true
  name: ask-analyst
- description: Send feedback on an Analyst response
  hints:
    readOnly: false
  name: send-analyst-feedback
- description: Generate verified query suggestions
  hints:
    readOnly: true
  name: generate-query-suggestions
- description: List available Cortex LLM models
  hints:
    readOnly: true
  name: list-llm-models
- description: Run LLM inference completion
  hints:
    readOnly: true
  name: llm-complete
- description: Query a Cortex Search service
  hints:
    readOnly: true
  name: semantic-search
- description: List Cortex Search services
  hints:
    readOnly: true
  name: list-search-services
- description: List notebooks
  hints:
    readOnly: true
  name: list-notebooks
- description: Create a notebook
  hints:
    readOnly: false
  name: create-notebook
- description: Execute a notebook
  hints:
    readOnly: false
  name: execute-notebook
---
