---
description: Request body for provisioning a new child application
layout: schema
name: ProvisionApplicationRequest
properties_list:
- description: Name of the customer application
  name: name
  type: string
- description: Description of the application
  name: description
  type: string
- description: Unique identifier for the customer in the partner's system
  name: uniqueForeignId
  type: string
- description: List of authorized OAuth 2.0 callback URLs
  name: oauth2AuthorizedCallbackUrls
  type: array
- description: List of valid JavaScript SDK domains
  name: validJsSdkDomains
  type: array
provider_name: LinkedIn
provider_slug: linkedin
schema_file: json-schema/linkedin-talent-learning-parent-application-provision-application-request-schema.json
slug: linkedin-talent-learning-parent-application-provision-application-request
tags:
- Business
- Careers
- Marketing
- Professional Networking
- Recruiting
- Social Media
title: ProvisionApplicationRequest
---
