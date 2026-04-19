---
description: A Search Console site resource representing a verified property. Properties can be URL-prefix properties or domain properties.
layout: schema
name: WmxSite
properties_list:
- description: 'The URL of the site. For URL-prefix properties, this is the full URL including protocol. For domain properties, this uses the sc-domain: prefix (e.g., sc-domain:example.com).'
  name: siteUrl
  type: string
- description: The user's permission level for this site in Search Console.
  name: permissionLevel
  type: string
provider_name: Google Search Console
provider_slug: google-search-console
schema_file: json-schema/google-search-console-wmx-site-schema.json
slug: google-search-console-wmx-site
tags:
- Analytics
- Google
- Search
- SEO
- Webmaster Tools
title: WmxSite
---
