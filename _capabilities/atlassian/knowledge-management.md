---
consumed_apis:
- atlassian-admin
description: Knowledge management workflow combining Confluence Content, Space, Search, Template, Label, and User APIs for technical writers and team leads to create, organize, and share documentation.
layout: capability
name: Atlassian Knowledge Management
operations:
- description: List Confluence content
  method: GET
  name: list-content
  path: /v1/content
- description: List Confluence spaces
  method: GET
  name: list-spaces
  path: /v1/spaces
- description: Search Confluence content
  method: GET
  name: search-content
  path: /v1/search
personas: []
provider_name: Atlassian
provider_slug: atlassian
search_terms:
- productivity
- list spaces
- content management
- list confluence users
- code
- collaboration
- list users
- list confluence content
- platform
- list content
- list groups
- list templates
- content search
- search confluence content using cql
- list confluence groups
- list confluence templates
- list confluence spaces
- list confluence pages and blog posts
- software development
- search confluence content
- confluence
- knowledge management
- atlassian
- space management
- search content
slug: knowledge-management
tags:
- Atlassian
- Confluence
- Knowledge Management
tools:
- description: List Confluence pages and blog posts
  hints:
    openWorld: true
    readOnly: true
  name: list-content
- description: Search Confluence content using CQL
  hints:
    readOnly: true
  name: search-content
- description: List Confluence spaces
  hints:
    readOnly: true
  name: list-spaces
- description: List Confluence templates
  hints:
    readOnly: true
  name: list-templates
- description: List Confluence groups
  hints:
    readOnly: true
  name: list-groups
- description: List Confluence users
  hints:
    readOnly: true
  name: list-users
---
