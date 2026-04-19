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
- marketing
- content
- operations
- hubspot retrieve event instances
- hubspot send a transactional email
- getsmtptokenbyid
- resetsmtptokenpassword
- sendtransactionalemail
- hubspot reset smtp token password
- hubspot get an smtp token by id
- email
- geteventtypes
- customer service
- analytics
- createsmtptoken
- geteventinstances
- crm
- marketing automation
- hubspot retrieve available event types
- hubspot delete an smtp token
- sales
- hubspot
- commerce
- hubspot create an smtp token
- listsmtptokens
- hubspot list all smtp tokens
- email marketing
- deletesmtptoken
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
