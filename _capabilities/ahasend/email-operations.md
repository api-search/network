---
consumed_apis:
- ahasend
description: Unified workflow for sending transactional emails, managing domains, configuring webhooks, and monitoring delivery statistics. Used by developers integrating email notifications into applications.
layout: capability
name: AhaSend Email Operations
operations:
- description: List email messages
  method: GET
  name: list-messages
  path: /v1/messages
- description: Send a transactional email
  method: POST
  name: send-message
  path: /v1/messages
- description: List domains
  method: GET
  name: list-domains
  path: /v1/domains
- description: List webhooks
  method: GET
  name: list-webhooks
  path: /v1/webhooks
- description: List suppressed addresses
  method: GET
  name: list-suppressions
  path: /v1/suppressions
- description: Get deliverability statistics
  method: GET
  name: get-deliverability-stats
  path: /v1/statistics/deliverability
personas: []
provider_name: AhaSend
provider_slug: ahasend
search_terms:
- list webhooks
- send message
- manage sending domains
- send and retrieve transactional email messages
- list suppressions
- get deliverability statistics
- list suppressed addresses
- list suppressed email addresses (bounces, complaints, unsubscribes)
- email
- application developer integrating transactional email into their application
- list messages
- webhook and route configuration for email events
- transactional email
- email delivery statistics
- send a transactional email message via ahasend
- send email
- deliverability
- manage email suppressions
- manage event webhooks
- managing email suppression lists
- list sent email messages with delivery status
- send a transactional email
- list email messages
- list configured webhooks for email event notifications
- Developer
- DevOps Engineer
- smtp
- webhooks
- sending and tracking transactional emails
- get transactional email deliverability statistics and metrics
- list domains
- developer tools
- infrastructure engineer monitoring email delivery health and managing domains
- get deliverability stats
- configuring and validating sending domains
- list configured sending domains and their dns verification status
- send emails, manage domains, configure webhooks, and monitor delivery statistics
slug: email-operations
tags:
- Email
- Transactional Email
- Developer Tools
- Webhooks
- Deliverability
tools:
- description: Send a transactional email message via AhaSend
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: send-email
- description: List sent email messages with delivery status
  hints:
    openWorld: true
    readOnly: true
  name: list-messages
- description: List configured sending domains and their DNS verification status
  hints:
    openWorld: true
    readOnly: true
  name: list-domains
- description: List configured webhooks for email event notifications
  hints:
    openWorld: true
    readOnly: true
  name: list-webhooks
- description: List suppressed email addresses (bounces, complaints, unsubscribes)
  hints:
    openWorld: true
    readOnly: true
  name: list-suppressions
- description: Get transactional email deliverability statistics and metrics
  hints:
    openWorld: true
    readOnly: true
  name: get-deliverability-stats
---
