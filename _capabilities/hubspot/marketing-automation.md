---
consumed_apis:
- marketing-emal-api
- analytics-events-api
description: Marketing automation workflow combining email campaigns and analytics events.
layout: capability
name: HubSpot Marketing Automation
operations: []
personas: []
provider_name: HubSpot
provider_slug: hubspot
search_terms:
- createsmtptoken
- hubspot list all smtp tokens
- analytics
- resetsmtptokenpassword
- customer service
- hubspot delete an smtp token
- marketing automation
- geteventtypes
- hubspot
- sendtransactionalemail
- hubspot retrieve event instances
- hubspot create an smtp token
- content
- hubspot retrieve available event types
- deletesmtptoken
- hubspot get an smtp token by id
- crm
- sales
- hubspot send a transactional email
- getsmtptokenbyid
- hubspot reset smtp token password
- marketing
- listsmtptokens
- email marketing
- commerce
- operations
- geteventinstances
- email
slug: marketing-automation
tags:
- HubSpot
- Marketing
- Email
- Analytics
tools:
- description: HubSpot List All SMTP Tokens
  hints:
    readOnly: true
  name: listsmtptokens
- description: HubSpot Create an SMTP Token
  hints:
    readOnly: false
  name: createsmtptoken
- description: HubSpot Get an SMTP Token by ID
  hints:
    readOnly: true
  name: getsmtptokenbyid
- description: HubSpot Delete an SMTP Token
  hints:
    destructive: true
  name: deletesmtptoken
- description: HubSpot Reset SMTP Token Password
  hints:
    readOnly: false
  name: resetsmtptokenpassword
- description: HubSpot Send a Transactional Email
  hints:
    readOnly: false
  name: sendtransactionalemail
- description: HubSpot Retrieve Event Instances
  hints:
    readOnly: true
  name: geteventinstances
- description: HubSpot Retrieve Available Event Types
  hints:
    readOnly: true
  name: geteventtypes
---
