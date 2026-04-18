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
- analytics
- hubspot create an smtp token
- customer service
- createsmtptoken
- hubspot retrieve event instances
- hubspot list all smtp tokens
- hubspot
- hubspot delete an smtp token
- crm
- hubspot get an smtp token by id
- marketing
- hubspot send a transactional email
- geteventtypes
- content
- marketing automation
- hubspot reset smtp token password
- listsmtptokens
- sendtransactionalemail
- commerce
- operations
- geteventinstances
- resetsmtptokenpassword
- hubspot retrieve available event types
- email marketing
- email
- getsmtptokenbyid
- sales
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
