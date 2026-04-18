---
consumed_apis:
- confluence-cloud-v2
description: Unified workflow for managing Confluence content including pages, blog posts, comments, attachments, spaces, and labels. Used by content authors, knowledge managers, and platform administrators.
layout: capability
name: Confluence Content Management
operations:
- description: List all pages with optional filtering
  method: GET
  name: list-pages
  path: /v1/pages
- description: Create a new page
  method: POST
  name: create-page
  path: /v1/pages
- description: Get a page by ID
  method: GET
  name: get-page
  path: /v1/pages/{id}
- description: Update a page
  method: PUT
  name: update-page
  path: /v1/pages/{id}
- description: Delete a page
  method: DELETE
  name: delete-page
  path: /v1/pages/{id}
- description: List child pages
  method: GET
  name: list-child-pages
  path: /v1/pages/{id}/children
- description: Get labels for a page
  method: GET
  name: get-page-labels
  path: /v1/pages/{id}/labels
- description: List attachments for a page
  method: GET
  name: list-page-attachments
  path: /v1/pages/{id}/attachments
- description: List footer comments for a page
  method: GET
  name: list-footer-comments
  path: /v1/pages/{id}/comments
- description: List all spaces
  method: GET
  name: list-spaces
  path: /v1/spaces
- description: Get a space by ID
  method: GET
  name: get-space
  path: /v1/spaces/{id}
- description: List pages in a space
  method: GET
  name: list-pages-in-space
  path: /v1/spaces/{id}/pages
- description: List all blog posts
  method: GET
  name: list-blog-posts
  path: /v1/blog-posts
- description: Create a new blog post
  method: POST
  name: create-blog-post
  path: /v1/blog-posts
- description: Get a blog post by ID
  method: GET
  name: get-blog-post
  path: /v1/blog-posts/{id}
- description: Update a blog post
  method: PUT
  name: update-blog-post
  path: /v1/blog-posts/{id}
- description: Delete a blog post
  method: DELETE
  name: delete-blog-post
  path: /v1/blog-posts/{id}
- description: Get a comment by ID
  method: GET
  name: get-comment
  path: /v1/comments/{id}
- description: Update a comment
  method: PUT
  name: update-comment
  path: /v1/comments/{id}
- description: Delete a comment
  method: DELETE
  name: delete-comment
  path: /v1/comments/{id}
- description: Get an attachment by ID
  method: GET
  name: get-attachment
  path: /v1/attachments/{id}
- description: Delete an attachment
  method: DELETE
  name: delete-attachment
  path: /v1/attachments/{id}
- description: Get a label by ID
  method: GET
  name: get-label
  path: /v1/labels/{id}
personas: []
provider_name: Confluence
provider_slug: confluence
search_terms:
- delete a blog post by id.
- list spaces
- get all labels applied to a specific page.
- list child pages of a specific page for navigating content hierarchies.
- update blog post
- list footer comments for a page
- delete a comment
- list pages
- get a specific attachment by its id.
- get page
- confluence
- create a new confluence blog post.
- get an attachment by id
- create a new blog post
- delete a blog post
- create page
- update a blog post
- delete a confluence page by id.
- create a new confluence page in a space.
- update an existing comment.
- list all confluence pages with optional filtering by space, status, and title.
- get labels for a page
- manage comments
- get a page by id
- get comment
- get a specific blog post by its id.
- update an existing blog post.
- wiki
- page label management
- get a comment by id
- get a specific confluence space by its id.
- individual blog post operations
- knowledge base
- get a blog post by id
- get a specific label by its id.
- get a space by id
- label information
- list footer comments on a specific page.
- individual space operations
- get page labels
- list footer comments
- manage attachments
- update page
- child page navigation
- get a label by id
- manage confluence spaces
- list all confluence spaces.
- delete an attachment by id.
- get attachment
- update an existing confluence page title and body.
- delete an attachment
- list all blog posts
- documentation
- manage blog posts
- update a page
- create inline comment
- list all spaces
- list pages in space
- delete comment
- update a comment
- list page attachments
- create footer comment
- list inline comments
- delete blog post
- list child pages
- get space
- list pages in a space
- create blog post
- list all file attachments on a specific page.
- delete page
- get label
- list all pages belonging to a specific space.
- create an inline comment on a specific text selection in a page.
- get a specific comment by its id.
- list all pages with optional filtering
- list attachments for a page
- list inline comments on a specific page.
- page attachment management
- list all blog posts with optional space filtering.
- delete a comment by id.
- page comment management
- delete a page
- get a specific confluence page by its id.
- delete attachment
- collaboration
- content management
- individual page operations
- pages within a space
- manage confluence pages
- list blog posts
- create a new page
- get blog post
- update comment
- create a footer comment on a page or blog post.
slug: content-management
tags:
- Confluence
- Content Management
- Collaboration
- Wiki
- Knowledge Base
tools:
- description: List all Confluence pages with optional filtering by space, status, and title.
  hints:
    openWorld: true
    readOnly: true
  name: list-pages
- description: Create a new Confluence page in a space.
  hints:
    readOnly: false
  name: create-page
- description: Get a specific Confluence page by its ID.
  hints:
    openWorld: true
    readOnly: true
  name: get-page
- description: Update an existing Confluence page title and body.
  hints:
    idempotent: true
    readOnly: false
  name: update-page
- description: Delete a Confluence page by ID.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-page
- description: List child pages of a specific page for navigating content hierarchies.
  hints:
    openWorld: true
    readOnly: true
  name: list-child-pages
- description: Get all labels applied to a specific page.
  hints:
    openWorld: true
    readOnly: true
  name: get-page-labels
- description: List all file attachments on a specific page.
  hints:
    openWorld: true
    readOnly: true
  name: list-page-attachments
- description: List all Confluence spaces.
  hints:
    openWorld: true
    readOnly: true
  name: list-spaces
- description: Get a specific Confluence space by its ID.
  hints:
    openWorld: true
    readOnly: true
  name: get-space
- description: List all pages belonging to a specific space.
  hints:
    openWorld: true
    readOnly: true
  name: list-pages-in-space
- description: List all blog posts with optional space filtering.
  hints:
    openWorld: true
    readOnly: true
  name: list-blog-posts
- description: Create a new Confluence blog post.
  hints:
    readOnly: false
  name: create-blog-post
- description: Get a specific blog post by its ID.
  hints:
    openWorld: true
    readOnly: true
  name: get-blog-post
- description: Update an existing blog post.
  hints:
    idempotent: true
    readOnly: false
  name: update-blog-post
- description: Delete a blog post by ID.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-blog-post
- description: Get a specific comment by its ID.
  hints:
    openWorld: true
    readOnly: true
  name: get-comment
- description: Create a footer comment on a page or blog post.
  hints:
    readOnly: false
  name: create-footer-comment
- description: Create an inline comment on a specific text selection in a page.
  hints:
    readOnly: false
  name: create-inline-comment
- description: Update an existing comment.
  hints:
    idempotent: true
    readOnly: false
  name: update-comment
- description: Delete a comment by ID.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-comment
- description: List footer comments on a specific page.
  hints:
    openWorld: true
    readOnly: true
  name: list-footer-comments
- description: List inline comments on a specific page.
  hints:
    openWorld: true
    readOnly: true
  name: list-inline-comments
- description: Get a specific attachment by its ID.
  hints:
    openWorld: true
    readOnly: true
  name: get-attachment
- description: Delete an attachment by ID.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-attachment
- description: Get a specific label by its ID.
  hints:
    openWorld: true
    readOnly: true
  name: get-label
---
