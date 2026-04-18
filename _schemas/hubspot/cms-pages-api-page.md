---
description: A HubSpot CMS page (site page or landing page).
layout: schema
name: Page
properties_list:
- description: The unique identifier for the page.
  name: id
  type: string
- description: The internal name of the page.
  name: name
  type: string
- description: The HTML title tag content for the page.
  name: htmlTitle
  type: string
- description: The URL slug for the page.
  name: slug
  type: string
- description: The current publish state of the page.
  name: state
  type: string
- description: The current display state of the page.
  name: currentState
  type: string
- description: The content type category code.
  name: contentTypeCategory
  type: integer
- description: The date and time the page was or will be published.
  name: publishDate
  type: string
- description: The meta description for SEO.
  name: metaDescription
  type: string
- description: The full URL of the published page.
  name: url
  type: string
- description: The domain the page is hosted on.
  name: domain
  type: string
- description: The language code for the page content.
  name: language
  type: string
- description: The path to the template used by the page.
  name: templatePath
  type: string
- description: The date and time the page was created.
  name: createdAt
  type: string
- description: The date and time the page was last updated.
  name: updatedAt
  type: string
- description: Whether the page has been archived.
  name: archived
  type: boolean
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/cms-pages-api-page-schema.json
slug: cms-pages-api-page
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
title: Page
---
