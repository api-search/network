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
- create a footer comment on a page or blog post.
- list all pages belonging to a specific space.
- get a comment by id
- delete a comment
- get all labels applied to a specific page.
- manage comments
- delete comment
- list all blog posts
- get a specific comment by its id.
- update an existing comment.
- create a new confluence blog post.
- create footer comment
- get a specific label by its id.
- create a new page
- label information
- delete page
- update a comment
- list footer comments on a specific page.
- documentation
- update page
- confluence
- content management
- manage blog posts
- manage confluence spaces
- update comment
- list all file attachments on a specific page.
- list inline comments
- list footer comments for a page
- list all pages with optional filtering
- list page attachments
- get page
- create inline comment
- page comment management
- get comment
- individual blog post operations
- list all confluence spaces.
- wiki
- knowledge base
- list all blog posts with optional space filtering.
- create a new confluence page in a space.
- delete an attachment by id.
- list child pages
- page label management
- delete a page
- delete a blog post
- get space
- get attachment
- get a label by id
- delete a blog post by id.
- get a space by id
- create blog post
- list child pages of a specific page for navigating content hierarchies.
- child page navigation
- get a specific attachment by its id.
- get a specific blog post by its id.
- list pages in space
- get a page by id
- create an inline comment on a specific text selection in a page.
- get labels for a page
- get label
- list footer comments
- get a specific confluence page by its id.
- update a blog post
- get a blog post by id
- get a specific confluence space by its id.
- list attachments for a page
- pages within a space
- delete blog post
- list blog posts
- update an existing confluence page title and body.
- individual page operations
- get page labels
- create page
- delete a comment by id.
- individual space operations
- manage attachments
- update a page
- update blog post
- list all confluence pages with optional filtering by space, status, and title.
- manage confluence pages
- list spaces
- get blog post
- list inline comments on a specific page.
- update an existing blog post.
- list all spaces
- create a new blog post
- page attachment management
- get an attachment by id
- list pages in a space
- delete a confluence page by id.
- collaboration
- list pages
- delete attachment
- delete an attachment
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
