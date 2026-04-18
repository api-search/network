---
description: Response containing provisioned application details
layout: schema
name: ProvisionApplicationResponse
properties_list:
- description: URN of the provisioned application
  name: applicationUrn
  type: string
- description: OAuth 2.0 client ID for the application
  name: clientId
  type: string
- description: OAuth 2.0 client secret for the application
  name: clientSecret
  type: string
- description: Name of the application
  name: name
  type: string
- description: Partner's unique identifier for the customer
  name: uniqueForeignId
  type: string
- description: ''
  name: oauth2AuthorizedCallbackUrls
  type: array
- description: ''
  name: validJsSdkDomains
  type: array
- description: Timestamp of application creation
  name: createdAt
  type: integer
provider_name: LinkedIn
provider_slug: linkedin
schema_file: json-schema/linkedin-talent-learning-parent-application-provision-application-response-schema.json
slug: linkedin-talent-learning-parent-application-provision-application-response
tags:
- Business
- Careers
- Marketing
- Professional Networking
- Recruiting
- Social Media
title: ProvisionApplicationResponse
---
