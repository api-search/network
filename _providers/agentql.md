---
api_count: 3
apis:
- description: Extract structured JSON data from web pages using AgentQL query language or natural language prompts. Supports URL-based and raw HTML input, configurable browser behavior, proxy settings, and screensh
  name: AgentQL Query Data API
  slug: query-data-api
- description: Create and manage remote Chrome browser sessions with Chrome DevTools Protocol (CDP) access for authenticated web automation, stealth browsing, and complex multi-step interactions.
  name: AgentQL Remote Browser Sessions API
  slug: remote-browser-api
- description: Extract structured data from PDF documents and images (JPEG, PNG) using AgentQL query language or natural language prompts. Useful for processing invoices, reports, and other document formats.
  name: AgentQL Query Document API
  slug: query-document-api
common:
- title: ''
  type: Portal
  url: https://www.agentql.com/
- title: ''
  type: Documentation
  url: https://docs.agentql.com/home
- title: ''
  type: GettingStarted
  url: https://docs.agentql.com/quick-start
- title: ''
  type: Pricing
  url: https://www.agentql.com/pricing
- title: ''
  type: Blog
  url: https://www.agentql.com/blog
- title: ''
  type: Support
  url: https://docs.agentql.com/support
- title: ''
  type: Console
  url: https://dev.agentql.com/playground
- title: Python SDK
  type: SDK
  url: https://pypi.org/project/agentql/
- title: JavaScript SDK
  type: SDK
  url: https://www.npmjs.com/package/agentql
- title: ''
  type: CLI
  url: https://docs.agentql.com/cli
- title: ''
  type: GitHubOrganization
  url: https://github.com/tinyfish-io
created: '2025-08-19'
description: AgentQL connects LLMs and AI agents to the entire web through a specialized query language, REST API, and Python/JavaScript SDKs. It enables web scraping, data extraction, and browser automation using natural language queries that are self-healing — adapting automatically to page layout changes. AgentQL supports structured data extraction from web pages, PDF documents, and images, and integrates with LangChain, LlamaIndex, MCP, Zapier, and Google ADK.
features:
- description: A specialized query language that uses natural language to locate and extract web elements without requiring XPath, CSS selectors, or regex.
  name: Natural Language Query Language
- description: AI-powered queries automatically adapt to page layout changes, eliminating brittle scrapers that break on site updates.
  name: Self-Healing Queries
- description: Browserless data extraction from public URLs via a REST API requiring only an API key and query parameters.
  name: REST API
- description: Extract structured data from PDF documents, JPEG, and PNG images using the same query language as web extraction.
  name: PDF and Image Parsing
- description: Managed Chrome browser sessions with CDP access for authenticated browsing, stealth mode, and complex multi-step web automation.
  name: Remote Browser Sessions
- description: Python and JavaScript SDKs extend Playwright with AgentQL query capabilities for AI-powered browser automation.
  name: Playwright Integration
- description: Chrome extension for real-time query testing and optimization during development.
  name: Browser Debugger Extension
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Integrate AgentQL web extraction into LangChain agent and chain workflows.
  name: LangChain
- description: Use AgentQL as a data ingestion source for LlamaIndex-powered RAG and agent applications.
  name: LlamaIndex
- description: Expose AgentQL capabilities as MCP tools accessible to any MCP-compatible AI agent.
  name: MCP (Model Context Protocol)
- description: Connect AgentQL web extraction to thousands of apps via Zapier automation workflows.
  name: Zapier
- description: Integrate AgentQL with Google Agent Development Kit for Gemini-based agent web access.
  name: Google ADK
- description: Use AgentQL in Langflow visual AI workflow pipelines for web data extraction.
  name: Langflow
- description: Extend Playwright browser automation with AgentQL AI-powered element querying and data extraction.
  name: Playwright
jsonld:
- class_count: 5
  name: Agentql Context
  property_count: 16
  slug: agentql-context
layout: provider
modified: '2026-04-19'
name: AgentQL
skills: []
slug: agentql
solutions: []
tags:
- Agents
- Artificial Intelligence
- Web Scraping
- Data Extraction
- Browser Automation
- REST API
url: https://raw.githubusercontent.com/api-evangelist/agentql/refs/heads/main/apis.yml
use_cases:
- description: Extract product names, prices, and availability from e-commerce sites for competitive intelligence and price tracking.
  name: E-Commerce Price Monitoring
- description: Collect job listings, requirements, and company information from multiple job boards into a unified dataset.
  name: Job Board Aggregation
- description: Extract posts, metrics, and profile data from social media platforms for analysis and reporting.
  name: Social Media Content Harvesting
- description: Parse invoices, contracts, and reports in PDF format to extract structured data for downstream processing.
  name: Document Data Extraction
- description: Enable AI agents to access and extract data from any website as part of automated research and task completion workflows.
  name: AI Agent Web Access
- description: Automate the collection of contact information, company data, and other business intelligence from public web sources.
  name: Lead Generation
---
