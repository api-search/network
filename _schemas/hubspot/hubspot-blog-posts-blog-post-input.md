---
description: Input data for creating or updating a blog post
layout: schema
name: BlogPostInput
properties_list:
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
- description: ID of the blog this post belongs to
  name: contentGroupId
  type: string
- description: Campaign GUID
  name: campaign
  type: string
- description: Scheduled publish date
  name: publishDate
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
- description: Tag IDs to associate
  name: tagIds
  type: array
- description: Whether to display the featured image
  name: useFeaturedImage
  type: boolean
- description: Language code
  name: language
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-blog-posts-blog-post-input-schema.json
slug: hubspot-blog-posts-blog-post-input
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
title: BlogPostInput
---
