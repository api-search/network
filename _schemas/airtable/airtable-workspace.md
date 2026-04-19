---
description: An Airtable workspace is an organizational container that groups related bases together. Workspaces provide a shared collaboration boundary with configurable permissions for team members.
layout: schema
name: Airtable Workspace
properties_list:
- description: The unique identifier for the workspace (starts with 'wsp').
  name: id
  type: string
- description: The display name of the workspace.
  name: name
  type: string
- description: The individual user collaborators on this workspace.
  name: collaborators
  type: array
- description: The user group collaborators on this workspace.
  name: groupCollaborators
  type: array
provider_name: Airtable
provider_slug: airtable
schema_file: json-schema/airtable-workspace-schema.json
slug: airtable-workspace
tags:
- Applications
- Collaboration
- Data
- Databases
- Low-Code
- Productivity
- Spreadsheets
title: Airtable Workspace
---
