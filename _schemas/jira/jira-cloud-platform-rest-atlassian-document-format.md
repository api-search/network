---
description: Atlassian Document Format (ADF) representation of rich text content. ADF is a JSON-based format used in Jira Cloud REST API v3 for description, comment, and other rich text fields.
layout: schema
name: AtlassianDocumentFormat
properties_list:
- description: The root node type. Always doc.
  name: type
  type: string
- description: The ADF version. Currently 1.
  name: version
  type: integer
- description: The content nodes of the document.
  name: content
  type: array
provider_name: Jira
provider_slug: jira
schema_file: json-schema/jira-cloud-platform-rest-atlassian-document-format-schema.json
slug: jira-cloud-platform-rest-atlassian-document-format
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
title: AtlassianDocumentFormat
---
