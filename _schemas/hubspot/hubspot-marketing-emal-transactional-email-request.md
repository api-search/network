---
description: Request body for sending a transactional email
layout: schema
name: TransactionalEmailRequest
properties_list:
- description: The ID of the transactional email template to use
  name: emailId
  type: integer
- description: The email message configuration
  name: message
  type: object
- description: Properties to set on the contact (if createContact is enabled)
  name: contactProperties
  type: object
- description: Custom template variables for personalization
  name: customProperties
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-marketing-emal-transactional-email-request-schema.json
slug: hubspot-marketing-emal-transactional-email-request
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
title: TransactionalEmailRequest
---
