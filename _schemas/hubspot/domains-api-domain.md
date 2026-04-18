---
description: Represents a domain connected to a HubSpot CMS site
layout: schema
name: Domain
properties_list:
- description: The unique identifier for the domain
  name: id
  type: string
- description: The actual domain or sub-domain (e.g., www.hubspot.com)
  name: domain
  type: string
- description: When the domain was created
  name: createdAt
  type: string
- description: When the domain was last updated
  name: updatedAt
  type: string
- description: Whether the DNS for this domain is optimally configured for use with HubSpot
  name: isResolving
  type: boolean
- description: Whether the domain has been manually marked as resolving
  name: isManuallyMarkedAsResolving
  type: boolean
- description: Whether SSL is enabled for this domain
  name: isSslEnabled
  type: boolean
- description: Whether the domain only accepts HTTPS connections
  name: isSslOnly
  type: boolean
- description: Whether this is the primary domain for blog posts
  name: isPrimaryBlogPost
  type: boolean
- description: Whether this is the primary domain for site pages
  name: isPrimarySitePage
  type: boolean
- description: Whether this is the primary domain for landing pages
  name: isPrimaryLandingPage
  type: boolean
- description: Whether this is the primary domain for email web pages
  name: isPrimaryEmail
  type: boolean
- description: Whether this is the primary domain for knowledge base
  name: isPrimaryKnowledge
  type: boolean
- description: Whether the domain is used for CMS blog posts
  name: isUsedForBlogPost
  type: boolean
- description: Whether the domain is used for CMS site pages
  name: isUsedForSitePage
  type: boolean
- description: Whether the domain is used for CMS landing pages
  name: isUsedForLandingPage
  type: boolean
- description: Whether the domain is used for CMS email web pages
  name: isUsedForEmail
  type: boolean
- description: Whether the domain is used for CMS knowledge pages
  name: isUsedForKnowledge
  type: boolean
- description: The expected CNAME record for this domain
  name: expectedCname
  type: string
- description: The domain to redirect to, if any
  name: redirectTo
  type: string
- description: The primary domain this domain is secondary to
  name: secondaryToDomain
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/domains-api-domain-schema.json
slug: domains-api-domain
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
title: Domain
---
