---
description: Request body for creating a CMS page.
layout: schema
name: PageCreateRequest
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
- description: The domain to host the page on.
  name: domain
  type: string
- description: The language code for the page content.
  name: language
  type: string
- description: The path to the template to use for the page.
  name: templatePath
  type: string
- description: The layout sections and widget data for the page content.
  name: layoutSections
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/cms-pages-api-page-create-request-schema.json
slug: cms-pages-api-page-create-request
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
title: PageCreateRequest
---
