---
description: Request body for the URL Inspection API.
layout: schema
name: InspectUrlIndexRequest
properties_list:
- description: The fully qualified URL to inspect. Must be under the specified site property.
  name: inspectionUrl
  type: string
- description: The URL of the site property in Search Console. Can be a URL-prefix property (e.g., https://example.com/) or a domain property (e.g., sc-domain:example.com).
  name: siteUrl
  type: string
- description: Optional BCP-47 language code for the response. If not specified, the response will be in English.
  name: languageCode
  type: string
provider_name: Google Search Console
provider_slug: google-search-console
schema_file: json-schema/google-search-console-inspect-url-index-request-schema.json
slug: google-search-console-inspect-url-index-request
tags:
- Analytics
- Google
- Search
- SEO
- Webmaster Tools
title: InspectUrlIndexRequest
---
