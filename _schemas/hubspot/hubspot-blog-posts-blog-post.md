---
description: Represents a blog post with all content and metadata
layout: schema
name: BlogPost
properties_list:
- description: Unique identifier for the blog post
  name: id
  type: string
- description: Internal name of the blog post
  name: name
  type: string
- description: URL slug for the blog post
  name: slug
  type: string
- description: HTML title tag content
  name: htmlTitle
  type: string
- description: HTML content of the blog post body
  name: postBody
  type: string
- description: Summary or excerpt of the blog post
  name: postSummary
  type: string
- description: ID of the associated blog author
  name: blogAuthorId
  type: string
- description: Display name of the author
  name: authorName
  type: string
- description: ID of the blog this post belongs to
  name: contentGroupId
  type: string
- description: Campaign GUID associated with the post
  name: campaign
  type: string
- description: Category ID for the post
  name: categoryId
  type: integer
- description: Current state of the blog post
  name: state
  type: string
- description: Current state description
  name: currentState
  type: string
- description: ISO 8601 timestamp when the post was/will be published
  name: publishDate
  type: string
- description: ISO 8601 timestamp when the post was created
  name: created
  type: string
- description: ISO 8601 timestamp when the post was last updated
  name: updated
  type: string
- description: ISO 8601 timestamp when the post was archived
  name: archivedAt
  type: string
- description: Whether the post is currently published
  name: currentlyPublished
  type: boolean
- description: Domain where the post is published
  name: domain
  type: string
- description: URL of the featured image
  name: featuredImage
  type: string
- description: Alt text for the featured image
  name: featuredImageAltText
  type: string
- description: Meta description for SEO
  name: metaDescription
  type: string
- description: Custom HTML for the head section
  name: headHtml
  type: string
- description: Custom HTML for the footer section
  name: footerHtml
  type: string
- description: Language code of the blog post
  name: language
  type: string
- description: ID of the original post this was translated from
  name: translatedFromId
  type: string
- description: Array of tag IDs associated with the post
  name: tagIds
  type: array
- description: Whether to display the featured image
  name: useFeaturedImage
  type: boolean
- description: Full URL of the published post
  name: url
  type: string
- description: A/B test status
  name: abStatus
  type: string
- description: A/B test ID if part of a test
  name: abTestId
  type: string
- description: ID of the folder containing the post
  name: folderId
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-blog-posts-blog-post-schema.json
slug: hubspot-blog-posts-blog-post
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
title: BlogPost
---
