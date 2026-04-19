---
consumed_apis:
- figma-rest
description: Unified workflow for managing design files, components, styles, projects, comments, and asset export. Combines the Figma REST API endpoints into a cohesive design system management experience. Used by design system engineers, developers, and design ops teams.
layout: capability
name: Figma Design System Management
operations:
- description: Get a Figma file.
  method: GET
  name: get-file
  path: /v1/files/{file_key}
- description: Get specific nodes from a file.
  method: GET
  name: get-file-nodes
  path: /v1/files/{file_key}/nodes
- description: Render images from a file.
  method: GET
  name: get-images
  path: /v1/images/{file_key}
- description: Get a component by key.
  method: GET
  name: get-component
  path: /v1/components/{key}
- description: List team components.
  method: GET
  name: get-team-components
  path: /v1/teams/{team_id}/components
- description: List team projects.
  method: GET
  name: get-team-projects
  path: /v1/teams/{team_id}/projects
- description: List files in a project.
  method: GET
  name: get-project-files
  path: /v1/projects/{project_id}/files
personas: []
provider_name: Figma
provider_slug: figma
search_terms:
- list team projects.
- get specific nodes from a file.
- list published components for a team.
- get download links for images used as fills in a file.
- files
- get project files
- get a component by key.
- list published component sets for a team.
- figma
- list published styles for a team.
- ui/ux
- get a specific component by key.
- interfaces
- get team styles
- team project access.
- prototyping
- list files in a project.
- list components in a figma file.
- get file nodes
- render and export images from a figma file.
- list team components.
- image rendering.
- get team components
- get file versions
- get specific nodes from a figma file by ids.
- list version history of a figma file.
- render images from a file.
- list comments on a figma file.
- get file components
- get file
- get team component sets
- design file access.
- component access.
- post comment
- get a figma file document tree.
- get component
- get image fills
- get comments
- get information about the authenticated user.
- asset export
- design systems
- components
- get team projects
- get a figma file.
- collaboration
- get images
- team component access.
- post a comment on a figma file.
- design
- prototypes
- list projects for a team.
- graphics
- get me
- project file access.
- file node access.
slug: design-system-management
tags:
- Figma
- Design Systems
- Components
- Files
- Asset Export
tools:
- description: Get a Figma file document tree.
  hints:
    openWorld: true
    readOnly: true
  name: get-file
- description: Get specific nodes from a Figma file by IDs.
  hints:
    readOnly: true
  name: get-file-nodes
- description: Render and export images from a Figma file.
  hints:
    readOnly: true
  name: get-images
- description: Get download links for images used as fills in a file.
  hints:
    readOnly: true
  name: get-image-fills
- description: List version history of a Figma file.
  hints:
    readOnly: true
  name: get-file-versions
- description: List comments on a Figma file.
  hints:
    readOnly: true
  name: get-comments
- description: Post a comment on a Figma file.
  hints:
    readOnly: false
  name: post-comment
- description: List published components for a team.
  hints:
    readOnly: true
  name: get-team-components
- description: List components in a Figma file.
  hints:
    readOnly: true
  name: get-file-components
- description: Get a specific component by key.
  hints:
    idempotent: true
    readOnly: true
  name: get-component
- description: List published component sets for a team.
  hints:
    readOnly: true
  name: get-team-component-sets
- description: List published styles for a team.
  hints:
    readOnly: true
  name: get-team-styles
- description: List projects for a team.
  hints:
    readOnly: true
  name: get-team-projects
- description: List files in a project.
  hints:
    readOnly: true
  name: get-project-files
- description: Get information about the authenticated user.
  hints:
    readOnly: true
  name: get-me
---
