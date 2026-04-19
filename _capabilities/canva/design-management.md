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
- list canva designs accessible to the user.
- templates
- get a specific design by id.
- get resize job
- marketing
- create design
- create comment
- collaboration
- design
- resize a design to different dimensions or preset types.
- get the authenticated user profile.
- get an asset.
- delete an asset.
- get export job status and download url.
- get export job
- create a comment on a design.
- get resize job status.
- get autofill job status.
- design creation and management.
- create a design from a brand template using autofill data.
- list folder items
- get brand template
- get a folder by id.
- delete asset
- get brand template dataset
- upload asset
- create export job
- get users me
- get asset
- list available brand templates.
- create a new canva design.
- brand template access.
- get folder
- content creation
- get design
- brand management
- create autofill job
- export a design to pdf, png, jpg, gif, pptx, or mp4.
- list designs
- get a brand template by id.
- design exports.
- visual content
- asset management.
- create a design.
- list items in a folder.
- list designs.
- list brand templates
- get the autofill dataset for a brand template.
- canva
- apps
- get an asset by id.
- automation
- design autofill.
- upload an asset to canva.
- list brand templates.
- create autofill job.
- create resize job
- get autofill job
- export a design.
- graphics
- print
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
