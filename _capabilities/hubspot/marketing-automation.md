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
- customer service
- hubspot send a transactional email
- getsmtptokenbyid
- crm
- sales
- resetsmtptokenpassword
- createsmtptoken
- hubspot
- hubspot retrieve event instances
- hubspot retrieve available event types
- listsmtptokens
- hubspot list all smtp tokens
- deletesmtptoken
- hubspot create an smtp token
- hubspot get an smtp token by id
- marketing
- hubspot reset smtp token password
- commerce
- geteventtypes
- analytics
- hubspot delete an smtp token
- email marketing
- sendtransactionalemail
- content
- email
- operations
- geteventinstances
- marketing automation
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
