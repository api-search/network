---
description: PrivacyRequest from Adobe Campaign API
layout: schema
name: PrivacyRequest
properties_list:
- description: Name identifying the privacy request.
  name: name
  type: string
- description: The namespace name used to identify the data subject (e.g., email, phone).
  name: namespaceName
  type: string
- description: The value used to look up the data subject in the specified namespace (e.g., the email address).
  name: reconciliationValue
  type: string
- description: The privacy regulation for the request.
  name: regulation
  type: string
- description: Whether to access or delete the data subject data.
  name: type
  type: string
provider_name: Adobe Campaign
provider_slug: adobe-campaign
schema_file: json-schema/adobe-campaign-standard-privacy-request-schema.json
slug: adobe-campaign-standard-privacy-request
tags:
- Campaign Management
- Customer Experience
- Email Marketing
- Marketing Automation
- Multi-Channel Marketing
title: PrivacyRequest
---
