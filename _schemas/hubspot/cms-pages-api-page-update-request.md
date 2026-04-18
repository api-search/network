---
description: Request body for updating a CMS page.
layout: schema
name: PageUpdateRequest
properties_list:
- description: The internal name of the page.
  name: name
  type: string
- description: The HTML title tag content.
  name: htmlTitle
  type: string
- description: The URL slug for the page.
  name: slug
  type: string
- description: The meta description for SEO.
  name: metaDescription
  type: string
- description: The layout sections and widget data for the page content.
  name: layoutSections
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/cms-pages-api-page-update-request-schema.json
slug: cms-pages-api-page-update-request
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
title: PageUpdateRequest
---
