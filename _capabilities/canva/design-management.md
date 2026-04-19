---
consumed_apis:
- connect-api
description: Unified design management workflow combining design creation, asset management, brand templates, autofill, exports, and collaboration for marketing teams and content creators.
layout: capability
name: Canva Design Management
operations:
- description: List designs.
  method: GET
  name: list-designs
  path: /v1/designs
- description: Create a design.
  method: POST
  name: create-design
  path: /v1/designs
- description: Get an asset.
  method: GET
  name: get-asset
  path: /v1/assets
- description: Delete an asset.
  method: DELETE
  name: delete-asset
  path: /v1/assets
- description: Export a design.
  method: POST
  name: create-export-job
  path: /v1/exports
- description: List brand templates.
  method: GET
  name: list-brand-templates
  path: /v1/brand-templates
- description: Create autofill job.
  method: POST
  name: create-autofill-job
  path: /v1/autofills
personas: []
provider_name: Canva
provider_slug: canva
search_terms:
- visual content
- get brand template
- get autofill job status.
- list folder items
- delete an asset.
- export a design to pdf, png, jpg, gif, pptx, or mp4.
- get resize job status.
- create design
- design creation and management.
- create autofill job.
- get an asset by id.
- graphics
- design
- delete asset
- brand management
- brand template access.
- get the autofill dataset for a brand template.
- apps
- design autofill.
- collaboration
- get a brand template by id.
- list designs.
- create comment
- get autofill job
- content creation
- asset management.
- get export job
- list brand templates
- get folder
- get asset
- create a design.
- marketing
- get a folder by id.
- export a design.
- create a new canva design.
- create a comment on a design.
- create autofill job
- get the authenticated user profile.
- get resize job
- list brand templates.
- get users me
- automation
- get an asset.
- get brand template dataset
- get design
- get export job status and download url.
- create a design from a brand template using autofill data.
- design exports.
- create export job
- list canva designs accessible to the user.
- resize a design to different dimensions or preset types.
- get a specific design by id.
- list available brand templates.
- list designs
- create resize job
- print
- upload asset
- canva
- templates
- upload an asset to canva.
- list items in a folder.
slug: design-management
tags:
- Canva
- Design
- Marketing
- Brand Management
- Content Creation
tools:
- description: List Canva designs accessible to the user.
  hints:
    openWorld: true
    readOnly: true
  name: list-designs
- description: Create a new Canva design.
  hints:
    readOnly: false
  name: create-design
- description: Get a specific design by ID.
  hints:
    readOnly: true
  name: get-design
- description: Get an asset by ID.
  hints:
    readOnly: true
  name: get-asset
- description: Delete an asset.
  hints:
    destructive: true
    readOnly: false
  name: delete-asset
- description: Upload an asset to Canva.
  hints:
    readOnly: false
  name: upload-asset
- description: Get a folder by ID.
  hints:
    readOnly: true
  name: get-folder
- description: List items in a folder.
  hints:
    readOnly: true
  name: list-folder-items
- description: Export a design to PDF, PNG, JPG, GIF, PPTX, or MP4.
  hints:
    readOnly: false
  name: create-export-job
- description: Get export job status and download URL.
  hints:
    readOnly: true
  name: get-export-job
- description: Create a comment on a design.
  hints:
    readOnly: false
  name: create-comment
- description: Get the authenticated user profile.
  hints:
    readOnly: true
  name: get-users-me
- description: List available brand templates.
  hints:
    readOnly: true
  name: list-brand-templates
- description: Get a brand template by ID.
  hints:
    readOnly: true
  name: get-brand-template
- description: Get the autofill dataset for a brand template.
  hints:
    readOnly: true
  name: get-brand-template-dataset
- description: Create a design from a brand template using autofill data.
  hints:
    readOnly: false
  name: create-autofill-job
- description: Get autofill job status.
  hints:
    readOnly: true
  name: get-autofill-job
- description: Resize a design to different dimensions or preset types.
  hints:
    readOnly: false
  name: create-resize-job
- description: Get resize job status.
  hints:
    readOnly: true
  name: get-resize-job
---
