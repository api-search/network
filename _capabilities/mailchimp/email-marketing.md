---
consumed_apis:
- marketing
- transactional
description: Unified workflow combining Mailchimp Marketing API for campaigns, audiences, and analytics with the Transactional API for personalized email delivery. Used by marketing teams and developers to manage the full email lifecycle.
layout: capability
name: Mailchimp Email Marketing
operations:
- description: List campaigns.
  method: GET
  name: list-campaigns
  path: /v1/campaigns
- description: Create a campaign.
  method: POST
  name: create-campaign
  path: /v1/campaigns
- description: Get campaign details.
  method: GET
  name: get-campaign
  path: /v1/campaigns/{campaign_id}
- description: Delete a campaign.
  method: DELETE
  name: delete-campaign
  path: /v1/campaigns/{campaign_id}
- description: Send campaign.
  method: POST
  name: send-campaign
  path: /v1/campaigns/{campaign_id}/send
- description: List audiences.
  method: GET
  name: list-audiences
  path: /v1/audiences
- description: List members.
  method: GET
  name: list-members
  path: /v1/audiences/{list_id}/members
- description: Add a member.
  method: POST
  name: add-member
  path: /v1/audiences/{list_id}/members
- description: List reports.
  method: GET
  name: list-reports
  path: /v1/reports
- description: Get campaign report.
  method: GET
  name: get-report
  path: /v1/reports/{campaign_id}
- description: Send a transactional email.
  method: POST
  name: send-transactional
  path: /v1/transactional/send
- description: Search sent messages.
  method: POST
  name: search-transactional
  path: /v1/transactional/search
personas: []
provider_name: Mailchimp
provider_slug: mailchimp
search_terms:
- marketing send campaign
- marketing get audience
- list all audiences.
- list reports
- transactional get user info
- marketing automation
- send a transactional email.
- list audience members.
- marketing list members
- list campaigns
- search transactional messages.
- add a member to an audience.
- marketing list templates
- send campaign
- create a new marketing campaign.
- campaigns
- list email templates.
- campaign reports.
- get campaign details.
- send transactional
- send campaign.
- audience management.
- email marketing
- audience members.
- search transactional
- marketing list audiences
- send a campaign.
- newsletters
- get a specific campaign report.
- create a campaign.
- send a marketing campaign.
- mailchimp
- transactional list templates
- marketing list automations
- search sent messages.
- get report
- get campaign report.
- transactional send template
- get a specific marketing campaign.
- add member
- search sent transactional messages.
- list members.
- marketing list reports
- specific campaign report.
- transactional get message info
- marketing list campaigns
- marketing get report
- list transactional email templates.
- delete campaign
- get audience details.
- marketing add member
- transactional email
- delete a marketing campaign.
- marketing delete campaign
- send transactional email.
- marketing campaigns.
- get campaign
- list campaigns.
- list campaign reports.
- list all marketing campaigns.
- marketing create campaign
- marketing get campaign
- transactional search messages
- add a member.
- create campaign
- list audiences
- list audiences.
- list members
- list reports.
- transactional send message
- get details about a sent transactional message.
- get transactional account information.
- specific campaign.
- list marketing automations.
- send a transactional email with a template.
- delete a campaign.
slug: email-marketing
tags:
- Mailchimp
- Email Marketing
- Transactional Email
- Marketing Automation
tools:
- description: List all marketing campaigns.
  hints:
    openWorld: true
    readOnly: true
  name: marketing-list-campaigns
- description: Get a specific marketing campaign.
  hints:
    idempotent: true
    readOnly: true
  name: marketing-get-campaign
- description: Create a new marketing campaign.
  hints:
    readOnly: false
  name: marketing-create-campaign
- description: Send a marketing campaign.
  hints:
    readOnly: false
  name: marketing-send-campaign
- description: Delete a marketing campaign.
  hints:
    destructive: true
    readOnly: false
  name: marketing-delete-campaign
- description: List all audiences.
  hints:
    openWorld: true
    readOnly: true
  name: marketing-list-audiences
- description: Get audience details.
  hints:
    idempotent: true
    readOnly: true
  name: marketing-get-audience
- description: List audience members.
  hints:
    readOnly: true
  name: marketing-list-members
- description: Add a member to an audience.
  hints:
    readOnly: false
  name: marketing-add-member
- description: List marketing automations.
  hints:
    readOnly: true
  name: marketing-list-automations
- description: List email templates.
  hints:
    readOnly: true
  name: marketing-list-templates
- description: List campaign reports.
  hints:
    readOnly: true
  name: marketing-list-reports
- description: Get a specific campaign report.
  hints:
    idempotent: true
    readOnly: true
  name: marketing-get-report
- description: Send a transactional email.
  hints:
    readOnly: false
  name: transactional-send-message
- description: Send a transactional email with a template.
  hints:
    readOnly: false
  name: transactional-send-template
- description: Search sent transactional messages.
  hints:
    readOnly: true
  name: transactional-search-messages
- description: Get details about a sent transactional message.
  hints:
    idempotent: true
    readOnly: true
  name: transactional-get-message-info
- description: List transactional email templates.
  hints:
    readOnly: true
  name: transactional-list-templates
- description: Get transactional account information.
  hints:
    readOnly: true
  name: transactional-get-user-info
---
