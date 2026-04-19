---
api_count: 12
apis:
- description: REST API for managing GitHub Copilot seats, usage, and organization settings.
  name: GitHub Copilot API
  slug: ''
- description: Manage Copilot for Business subscriptions, seat assignments, and usage metrics.
  name: GitHub Copilot for Business API
  slug: ''
- description: API for GitHub Copilot Chat interactions and conversations.
  name: GitHub Copilot Chat API
  slug: ''
- description: REST API for managing GitHub Copilot seat assignments, billing information, and subscription details for organizations including adding and removing users and teams.
  name: GitHub Copilot User Management API
  slug: ''
- description: REST API for retrieving aggregated Copilot usage metrics at the organization and team level, including data on active users, engaged users, and breakdowns by language and editor.
  name: GitHub Copilot Metrics API
  slug: ''
- description: REST API for retrieving detailed Copilot usage metrics reports at the enterprise and organization level, including daily and 28-day aggregated reports for both entity-level and user-level data.
  name: GitHub Copilot Usage Metrics API
  slug: ''
- description: REST API for programmatically managing Copilot content exclusion path rules at both the organization and enterprise level, enabling automation and governance of which content Copilot can access.
  name: GitHub Copilot Content Exclusion API
  slug: ''
- description: Platform for building Copilot Extensions that integrate third-party tools, services, and custom agents into GitHub Copilot Chat, using GitHub Apps with agent or skillset configurations.
  name: GitHub Copilot Extensions API
  slug: ''
- description: Autonomous coding agent that works in the background to complete tasks, spinning up secure development environments powered by GitHub Actions to explore code, make changes, run tests, and open pull re
  name: GitHub Copilot Coding Agent
  slug: ''
- description: AI-powered code review agent that analyzes pull requests for issues, suggests fixes, and provides feedback across any programming language with agentic context gathering capabilities.
  name: GitHub Copilot Code Review
  slug: ''
- description: GitHub official Model Context Protocol server that enables AI tools to interact with GitHub repositories, issues, pull requests, and other resources through a standardized protocol.
  name: GitHub MCP Server
  slug: ''
- description: Configuration system for providing repository-level, path-specific, and organization-level custom instructions to guide Copilot behavior, code style, and response formatting.
  name: GitHub Copilot Custom Instructions
  slug: ''
common:
- title: ''
  type: Portal
  url: https://github.com/features/copilot
- title: ''
  type: StatusPage
  url: https://www.githubstatus.com/
- title: ''
  type: TermsOfService
  url: https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
- title: ''
  type: PrivacyPolicy
  url: https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement
- title: ''
  type: GettingStarted
  url: https://docs.github.com/en/copilot/quickstart
- title: ''
  type: Blog
  url: https://github.blog/tag/github-copilot/
- title: ''
  type: SignUp
  url: https://github.com/github-copilot/signup
- title: ''
  type: Pricing
  url: https://github.com/features/copilot/plans
- title: ''
  type: ChangeLog
  url: https://github.blog/changelog/label/copilot/
- title: ''
  type: Support
  url: https://support.github.com
- title: ''
  type: SDK
  url: https://github.com/github/copilot-sdk
- title: ''
  type: TrustCenter
  url: https://copilot.github.trust.page/
- title: ''
  type: RateLimits
  url: https://docs.github.com/en/rest/overview/rate-limits-for-the-rest-api
- title: ''
  type: Authentication
  url: https://docs.github.com/en/rest/authentication
- title: ''
  type: OpenAPI
  url: https://github.com/github/rest-api-description
- title: ''
  type: Documentation
  url: https://docs.github.com/en/copilot
- title: ''
  type: Marketplace
  url: https://github.com/marketplace?type=apps&copilot_app=true
created: '2024'
description: APIs and resources for GitHub Copilot, an AI pair programmer that helps you write code faster.
features:
- description: AI-powered inline code suggestions that complete lines, functions, and entire blocks as you type in your IDE.
  name: Code Completion
- description: Conversational AI assistant for asking questions about code, generating solutions, and debugging directly in your editor.
  name: Chat
- description: Autonomous agent that explores code, makes changes, runs tests, and opens pull requests from issue assignments.
  name: Coding Agent
- description: AI-powered pull request review that analyzes changes, identifies issues, and suggests fixes across any language.
  name: Code Review
- description: Third-party integrations that extend Copilot Chat with custom tools, services, and domain-specific agents.
  name: Extensions
- description: Repository-level and organization-level configuration to guide Copilot behavior, code style, and conventions.
  name: Custom Instructions
- description: Model Context Protocol server enabling AI tools to interact with GitHub repositories, issues, and pull requests.
  name: MCP Server
- description: Governance controls to specify which files and repositories Copilot can access at organization and enterprise level.
  name: Content Exclusion
- description: Detailed analytics on Copilot adoption, usage patterns, and productivity impact across organizations and enterprises.
  name: Usage Metrics
- description: Programmatic management of Copilot seat assignments, billing, and subscription details for organizations and teams.
  name: Seat Management
image: https://github.githubassets.com/images/modules/site/copilot/copilot-logo.png
integrations:
- description: Full Copilot integration in VS Code including code completion, chat, code review, and MCP support.
  name: Visual Studio Code
- description: Copilot code completion and chat support across IntelliJ, PyCharm, WebStorm, and other JetBrains IDEs.
  name: JetBrains IDEs
- description: Copilot Chat, code review, and coding agent capabilities directly in the GitHub web interface.
  name: GitHub.com
- description: Copilot coding agent uses GitHub Actions to spin up secure environments for autonomous coding tasks.
  name: GitHub Actions
- description: Standard protocol integration enabling AI tools to access GitHub data through the official MCP server.
  name: Model Context Protocol
jsonld:
- class_count: 0
  name: Github Copilot Context
  property_count: 0
  slug: github-copilot-context
layout: provider
modified: '2026-04-18'
name: GitHub Copilot
rules:
- name: GitHub Copilot API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: github-copilot-spectral-rules
skills: []
slug: github-copilot
solutions: []
tags:
- Agents
- AI
- Artificial Intelligence
- Code Generation
- Code Review
- Coding Agent
- Custom Instructions
- Developer Tools
- Extensions
- IDE
- Machine Learning
- MCP
- Metrics
- Model Context Protocol
- Productivity
url: https://api.github.com/apis.yaml
use_cases:
- description: Accelerate software development with AI-powered code completions, chat assistance, and automated code review.
  name: Developer Productivity
- description: Manage Copilot deployments at scale with seat management, content exclusion, usage metrics, and compliance controls.
  name: Enterprise Copilot Governance
- description: Build domain-specific Copilot Extensions and agents that integrate third-party tools and services into the developer workflow.
  name: Custom AI Tooling
- description: Automate code review, identify potential issues, and enforce coding standards using the Copilot Code Review agent.
  name: Code Quality Automation
---
