---
api_count: 1
apis:
- description: 'Command-line tool that generates .aiignore configuration files to protect secrets from AI coding tools including JetBrains AI, Cursor, GitHub Copilot, Claude Code, Codeium, and Windsurf with a single '
  name: AIIgnore CLI
  slug: aiignore-cli
common:
- title: ''
  type: GitHubRepository
  url: https://github.com/yjcho9317/aiignore-cli
- title: ''
  type: Portal
  url: https://www.jetbrains.com/ai/
- title: ''
  type: GitHubRepository
  url: https://github.com/topics/aiignore
- title: ''
  type: Documentation
  url: https://docs.cursor.com/context/rules
- title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/claude-code/
created: '2025-01-01'
description: The .aiignore file is a configuration specification that tells AI coding agents and LLM-powered developer tools which files, directories, and content should not be read, processed, or modified. Modeled after .gitignore syntax, .aiignore files protect sensitive data, proprietary code, and personal information from being exposed to AI models during development workflows. Supported by JetBrains AI Assistant, Cursor, GitHub Copilot, Claude Code, Gemini Code Assist, and other AI coding tools.
features:
- description: Uses familiar glob pattern syntax from .gitignore so developers can immediately define exclusion rules.
  name: .gitignore-Compatible Syntax
- description: Prevents AI models from reading .env files, credential files, API keys, private keys, and other sensitive data.
  name: Secrets Protection
- description: Single .aiignore file works across JetBrains AI, Cursor, GitHub Copilot, Claude Code, Codeium, and Windsurf.
  name: Multi-Tool Support
- description: Exclude entire directories from AI context with simple pattern rules (e.g., vendor/, node_modules/).
  name: Directory-Level Exclusion
- description: Match files by extension, name, or path pattern to control AI model access granularly.
  name: File Pattern Matching
- description: Single file in project root applies rules across the entire project tree.
  name: Project-Root Placement
- description: Prevent proprietary algorithms, business logic, or licensed code from being sent to external AI APIs.
  name: Proprietary Code Protection
- description: aiignore-cli generates boilerplate .aiignore files with one command, covering common secrets patterns automatically.
  name: CLI Generation Tool
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: JetBrains IDEs (IntelliJ, PyCharm, WebStorm, etc.) AI Assistant respects .aiignore in project root.
  name: JetBrains AI Assistant
- description: Cursor IDE supports .cursorignore (similar concept) for controlling AI context access.
  name: Cursor AI Editor
- description: GitHub Copilot supports content exclusion via repository settings and .copilotignore patterns.
  name: GitHub Copilot
- description: Anthropic Claude Code CLI supports .claudeignore file for excluding files from AI context.
  name: Claude Code
- description: Codeium AI coding assistant with configurable file exclusion patterns.
  name: Codeium
- description: Codeium Windsurf AI editor with .windsurfignore support for context control.
  name: Windsurf
- description: Google Gemini Code Assist with project-level context exclusion configuration.
  name: Gemini Code Assist
jsonld:
- class_count: 4
  name: Aiignore Context
  property_count: 12
  slug: aiignore-context
layout: provider
modified: '2026-04-19'
name: .AIIgnore
skills: []
slug: aiignore
solutions: []
tags:
- AI Agents
- Configuration
- Developer Workflow
- Security
- Privacy
- Developer Tools
- LLM
- Secrets Management
url: https://raw.githubusercontent.com/api-evangelist/aiignore/refs/heads/main/apis.yml
use_cases:
- description: Exclude .env and config files containing API keys, tokens, and credentials from AI coding tool context.
  name: API Key Protection
- description: Protect trade secrets and proprietary algorithms from being processed by AI models hosted on third-party infrastructure.
  name: Proprietary Algorithm Protection
- description: Ensure regulated data (PII, healthcare records, financial data) is not sent to external AI APIs.
  name: Compliance and Data Privacy
- description: Exclude large binary files, build artifacts, and generated files that would waste AI context window.
  name: Large File Exclusion
- description: Prevent licensed third-party code and vendor directories from being included in AI context.
  name: Third-Party Code Exclusion
---
