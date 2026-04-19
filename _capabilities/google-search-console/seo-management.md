---
consumed_apis:
- search-console
description: Unified SEO management workflow combining search analytics, sitemap management, URL inspection, and site management for SEO specialists and webmasters.
layout: capability
name: Google Search Console SEO Management
operations:
- description: List all Search Console sites.
  method: GET
  name: list-sites
  path: /v1/sites
- description: Get details for a specific site.
  method: GET
  name: get-site
  path: /v1/sites
- description: Add a site to Search Console.
  method: PUT
  name: add-site
  path: /v1/sites
- description: Remove a site from Search Console.
  method: DELETE
  name: delete-site
  path: /v1/sites
- description: Query search analytics data with filters.
  method: POST
  name: query-search-analytics
  path: /v1/search-analytics
- description: List sitemaps for a site.
  method: GET
  name: list-sitemaps
  path: /v1/sitemaps
- description: Get sitemap details.
  method: GET
  name: get-sitemap
  path: /v1/sitemaps
- description: Submit a sitemap.
  method: PUT
  name: submit-sitemap
  path: /v1/sitemaps
- description: Delete a sitemap.
  method: DELETE
  name: delete-sitemap
  path: /v1/sitemaps
- description: Inspect a URL for index status and rich results.
  method: POST
  name: inspect-url
  path: /v1/url-inspection
personas: []
provider_name: Google Search Console
provider_slug: google-search-console
search_terms:
- get site
- search
- list sitemaps
- list all search console sites.
- delete site
- remove a site from search console.
- list sitemaps for a site.
- list sites
- list all search console sites for the authenticated user.
- query search traffic data with filters and dimensions.
- delete a previously submitted sitemap.
- submit a sitemap for crawling.
- get details for a specific search console site.
- inspect a url for index status, crawl info, mobile usability, and rich results.
- seo
- inspect a url for index status and rich results.
- webmaster tools
- delete a sitemap.
- get sitemap details.
- delete sitemap
- query search analytics data with filters.
- get sitemap
- get details for a specific sitemap.
- analytics
- list sitemaps submitted for a site.
- webmaster
- submit sitemap
- manage search console sites.
- inspect url
- query search traffic data.
- submit a sitemap.
- search console
- get details for a specific site.
- query search analytics
- manage sitemaps.
- add a site to search console.
- add site
- inspect urls for indexing status.
- google
slug: seo-management
tags:
- Google
- Search Console
- SEO
- Analytics
- Webmaster
tools:
- description: List all Search Console sites for the authenticated user.
  hints:
    openWorld: true
    readOnly: true
  name: list-sites
- description: Get details for a specific Search Console site.
  hints:
    openWorld: true
    readOnly: true
  name: get-site
- description: Add a site to Search Console.
  hints:
    openWorld: true
    readOnly: false
  name: add-site
- description: Remove a site from Search Console.
  hints:
    destructive: true
    readOnly: false
  name: delete-site
- description: Query search traffic data with filters and dimensions.
  hints:
    openWorld: true
    readOnly: true
  name: query-search-analytics
- description: List sitemaps submitted for a site.
  hints:
    openWorld: true
    readOnly: true
  name: list-sitemaps
- description: Get details for a specific sitemap.
  hints:
    openWorld: true
    readOnly: true
  name: get-sitemap
- description: Submit a sitemap for crawling.
  hints:
    openWorld: true
    readOnly: false
  name: submit-sitemap
- description: Delete a previously submitted sitemap.
  hints:
    destructive: true
    readOnly: false
  name: delete-sitemap
- description: Inspect a URL for index status, crawl info, mobile usability, and rich results.
  hints:
    openWorld: true
    readOnly: true
  name: inspect-url
---
