---
description: Represents a blog author profile with biographical and social information
layout: schema
name: BlogAuthor
properties_list:
- description: Unique identifier for the blog author
  name: id
  type: string
- description: Full display name of the author
  name: name
  type: string
- description: URL-friendly identifier for the author
  name: slug
  type: string
- description: Author's email address
  name: email
  type: string
- description: Author biography or description
  name: bio
  type: string
- description: Author's personal website URL
  name: website
  type: string
- description: Author's Twitter/X handle
  name: twitter
  type: string
- description: Author's Facebook profile URL
  name: facebook
  type: string
- description: Author's LinkedIn profile URL
  name: linkedin
  type: string
- description: URL to the author's avatar image
  name: avatar
  type: string
- description: Language code for the author profile (e.g., en, es, fr)
  name: language
  type: string
- description: ID of the original author this was translated from
  name: translatedFromId
  type: string
- description: ISO 8601 timestamp when the author was created
  name: created
  type: string
- description: ISO 8601 timestamp when the author was last updated
  name: updated
  type: string
- description: ISO 8601 timestamp when the author was archived
  name: deletedAt
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/authors-api-blog-author-schema.json
slug: authors-api-blog-author
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Operations
- Sales
title: BlogAuthor
---
