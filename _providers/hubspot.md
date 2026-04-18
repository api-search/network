---
api_count: 63
apis:
- description: These endpoints allow you to return information about the domains connected to a particular HubSpot CMS site. You can return data for a list of domains or specify a domain by ID.
  name: HubSpot Domains API
  slug: hubspot-domains-api
- description: Endpoints for interacting with files in the CMS Developer File System. These files include HTML templates, CSS, JS, modules, and other assets which are used to create CMS content.
  name: HubSpot Source Code API
  slug: hubspot-source-code-api
- description: Use these endpoints for interacting with Blog Posts, Blog Authors, and Blog Tags.
  name: HubSpot Posts API
  slug: hubspot-posts-api
- description: Use the blog authors API to manage author information for your blog posts.
  name: HubSpot Authors API
  slug: hubspot-authors-api
- description: 'URL redirects allow you to redirect traffic from a HubSpot-hosted page or blog post to any URL. You can also update URL redirects in bulk and use a flexible pattern redirect to dynamically update the '
  name: HubSpot URL Redirects API
  slug: hubspot-url-redirects-api
- description: The HubDB API allows you to create, update, and delete HubDB data tables and their rows. HubDB tables can be used as data sources for dynamic CMS pages and are available in both draft and published ve
  name: HubSpot CMS HubDB API
  slug: hubspot-cms-hubdb-api
- description: The CMS Pages API provides endpoints for creating and managing site pages and landing pages hosted on HubSpot. You can create, retrieve, update, publish, and delete both site pages and landing pages p
  name: HubSpot CMS Pages API
  slug: hubspot-cms-pages-api
- description: Contact records store information about individuals. The contacts endpoints allow you to manage contact data and sync it between HubSpot and other systems. You can create, retrieve, update, and delete
  name: HubSpot Contacts API
  slug: hubspot-contacts-api
- description: Company records store data about businesses and organizations. The companies endpoints allow you to manage this data and sync it between HubSpot and other systems, including creating, retrieving, upda
  name: HubSpot Companies API
  slug: hubspot-companies-api
- description: A deal stores data about an ongoing transaction or sales opportunity. The deals endpoints allow you to manage deal records and sync data between HubSpot and other systems, supporting the full lifecycl
  name: HubSpot Deals API
  slug: hubspot-deals-api
- description: Tickets represent customer requests for help and are tracked through support pipelines until resolved. The tickets endpoints allow you to create, manage, and retrieve customer support ticket records a
  name: HubSpot Tickets API
  slug: hubspot-tickets-api
- description: Pipelines allow you to track records through defined stages in a process, such as sales deals or support tickets. The pipelines endpoints allow you to create, retrieve, update, and delete pipelines an
  name: HubSpot Pipelines API
  slug: hubspot-pipelines-api
- description: Products represent the goods or services you sell in HubSpot. The products endpoints allow you to manage a product library which can be used to quickly add products to deals, generate quotes, and repo
  name: HubSpot Products API
  slug: hubspot-products-api
- description: Line items are individual instances of products that are attached to a deal or quote. The line items endpoints allow you to create, retrieve, update, and delete line item records, enabling detailed pr
  name: HubSpot Line Items API
  slug: hubspot-line-items-api
- description: Quotes allow you to share pricing information with prospects and customers. The quotes endpoints allow you to create and manage quotes with associated line items, deals, and contacts, and support feat
  name: HubSpot Quotes API
  slug: hubspot-quotes-api
- description: The CRM properties endpoints allow you to manage custom properties and view default property details for any CRM object type. You can create, retrieve, update, and delete properties for contacts, comp
  name: HubSpot CRM Properties API
  slug: hubspot-crm-properties-api
- description: The associations endpoints allow you to manage relationships between CRM object records such as contacts, companies, deals, and tickets. You can create, retrieve, and delete associations with or witho
  name: HubSpot CRM Associations API
  slug: hubspot-crm-associations-api
- description: The owners endpoints are used to retrieve the list of available owners for a HubSpot account. HubSpot uses owners to assign CRM object records to specific users, and owner IDs are used when setting re
  name: HubSpot Owners API
  slug: hubspot-owners-api
- description: 'The imports endpoints allow you to import contact, company, deal, and other CRM object data into a HubSpot account in bulk using CSV or Excel files. You can map file columns to HubSpot properties and '
  name: HubSpot CRM Imports API
  slug: hubspot-crm-imports-api
- description: The Lists API allows you to create and manage lists of CRM records based on static membership or dynamic filter criteria. Lists can be used to segment contacts, companies, and other CRM objects for ma
  name: HubSpot CRM Lists API
  slug: hubspot-crm-lists-api
- description: 'The CRM Search API allows you to query and filter CRM objects using a flexible search interface. You can search across contacts, companies, deals, tickets, and other object types using filter groups, '
  name: HubSpot CRM Search API
  slug: hubspot-crm-search-api
- description: 'Custom objects allow you to define and create CRM object types that represent data unique to your business. The custom objects API allows you to define schemas, create records, manage properties, and '
  name: HubSpot Custom Objects API
  slug: hubspot-custom-objects-api
- description: 'The payments endpoints allow you to retrieve data about payment transactions processed through HubSpot Commerce. You can retrieve payment details, manage subscriptions, and access transaction history '
  name: HubSpot Commerce Payments API
  slug: hubspot-commerce-payments-api
- description: The subscriptions API allows you to retrieve data about recurring subscription records in HubSpot Commerce. Subscriptions are created when a customer purchases a recurring product through HubSpot paym
  name: HubSpot Commerce Subscriptions API
  slug: hubspot-commerce-subscriptions-api
- description: The OAuth API allows you to manage OAuth access tokens for public applications. You can generate, refresh, retrieve metadata for, and delete OAuth tokens to provide secure, scoped API access for HubSp
  name: HubSpot OAuth API
  slug: hubspot-oauth-api
- description: Custom events allow you to track advanced user activity via a JavaScript or HTTP API. The events API enables you to send custom event occurrences, define event schemas, and retrieve historical event d
  name: HubSpot Analytics Events API
  slug: hubspot-analytics-events-api
- description: The marketing emails API allows you to programmatically create, update, and retrieve details about marketing emails in HubSpot. You can manage email campaigns, retrieve email performance statistics, a
  name: HubSpot Marketing Email API
  slug: hubspot-marketing-email-api
- description: Marketing events are CRM objects that enable you to track marketing activities such as webinars along with the contacts who registered and attended. The marketing events API supports creating and mana
  name: HubSpot Marketing Events API
  slug: hubspot-marketing-events-api
- description: The forms endpoints allow you to create and manage HubSpot forms used for capturing lead information. Supported form types include HubSpot native forms, captured external forms, flow forms, and blog c
  name: HubSpot Forms API
  slug: hubspot-forms-api
- description: The conversations API enables management of inboxes, channels, threads, and messages within HubSpot's conversations system. You can retrieve conversation data, update thread statuses, send messages, a
  name: HubSpot Conversations API
  slug: hubspot-conversations-api
- description: The calls endpoints allow you to log and manage call engagement records within HubSpot CRM. You can create call records, associate them with contacts and deals, retrieve call data, and manage call rec
  name: HubSpot Engagement Calls API
  slug: hubspot-engagement-calls-api
- description: The notes endpoints allow you to create and manage note engagement records in HubSpot CRM. Notes can be associated with contacts, companies, deals, and tickets to capture important information and act
  name: HubSpot Engagement Notes API
  slug: hubspot-engagement-notes-api
- description: The meetings endpoints allow you to log and manage meeting engagement records in HubSpot CRM. You can create meeting records, associate them with contacts and companies, and retrieve meeting details a
  name: HubSpot Engagement Meetings API
  slug: hubspot-engagement-meetings-api
- description: 'The tasks endpoints allow you to create and manage task engagement records in HubSpot CRM. Tasks represent to-do items that can be assigned to users and associated with contacts, companies, and deals '
  name: HubSpot Engagement Tasks API
  slug: hubspot-engagement-tasks-api
- description: 'The emails engagement API allows you to log and manage email activity records on CRM records in HubSpot. You can create email engagement records to track sent emails, associate them with contacts and '
  name: HubSpot Engagement Emails API
  slug: hubspot-engagement-emails-api
- description: Custom workflow actions allow you to extend HubSpot workflows by creating reusable actions that can be installed by HubSpot users. The custom workflow actions API allows you to define, manage, and ret
  name: HubSpot Custom Workflow Actions API
  slug: hubspot-custom-workflow-actions-api
- description: The workflows API allows you to programmatically create, retrieve, update, and delete HubSpot automation workflows. You can manage workflow definitions and automate business processes across CRM objec
  name: HubSpot Workflows API
  slug: hubspot-workflows-api
- description: The webhooks API allows you to subscribe to events occurring in a HubSpot account, receiving real-time notifications when CRM objects or conversations are created, updated, or deleted. You can configu
  name: HubSpot Webhooks API
  slug: hubspot-webhooks-api
- description: The feature flags API allows public app developers to manage feature flags for their HubSpot app installations. Feature flags can be used to control the rollout of new functionality to specific accoun
  name: HubSpot CRM Feature Flags API
  slug: hubspot-crm-feature-flags-api
- description: The user provisioning API allows you to create and manage users in a HubSpot account along with their roles, permissions, and team assignments. You can add, retrieve, update, and remove users programm
  name: HubSpot Settings User Provisioning API
  slug: hubspot-settings-user-provisioning-api
- description: The blog tags API allows you to create, manage, and organize blog post tags in HubSpot CMS. Tags help organize blog content and improve discoverability. You can create, retrieve, update, and delete ta
  name: HubSpot Blog Tags API
  slug: hubspot-blog-tags-api
- description: 'The site search API allows you to search the content of HubSpot-hosted sites, including site pages, blog posts, landing pages, and knowledge articles. You can build custom site search experiences and '
  name: HubSpot CMS Site Search API
  slug: hubspot-cms-site-search-api
- description: The CMS content audit API allows you to query audit logs of CMS changes that occurred within your HubSpot account. You can filter and sort on content object changes by type, time period, or HubSpot us
  name: HubSpot CMS Content Audit API
  slug: hubspot-cms-content-audit-api
- description: The files API allows you to upload, manage, and organize files in HubSpot's file manager. You can upload files, organize them into folders, control file accessibility and privacy settings, retrieve fi
  name: HubSpot Files API
  slug: hubspot-files-api
- description: The feedback submissions API allows you to retrieve survey response data from HubSpot surveys including NPS, CSAT, CES, and custom surveys. This is a read-only API that provides access to existing sur
  name: HubSpot Feedback Submissions API
  slug: hubspot-feedback-submissions-api
- description: The leads API enables you to manage lead records in HubSpot. Leads are contacts or companies that are potential customers who have shown interest in your products or services. You can create, retrieve
  name: HubSpot Leads API
  slug: hubspot-leads-api
- description: The goals API enables you to sync user-specific sales and service team quotas between HubSpot and external systems. Goals are used to create user-specific quotas based on templates provided by HubSpot
  name: HubSpot Goals API
  slug: hubspot-goals-api
- description: The orders API enables you to create and manage ecommerce order data in HubSpot. You can create orders, manage associations to contacts, line items, payments, and invoices, and track fulfillment progr
  name: HubSpot Orders API
  slug: hubspot-orders-api
- description: The carts API enables you to create and manage ecommerce cart data in HubSpot. You can sync cart information between HubSpot and external ecommerce platforms, manage cart properties like pricing and c
  name: HubSpot Carts API
  slug: hubspot-carts-api
- description: The invoices API allows you to create, manage, retrieve, and delete invoices used for billing customers. Invoices progress through draft, open, paid, and voided statuses, and can be configured with di
  name: HubSpot Invoices API
  slug: hubspot-invoices-api
- description: The taxes API enables you to create and associate tax objects as part of the pricing details for quotes and invoices. Taxes are used in conjunction with discounts and fees when determining pricing tot
  name: HubSpot Taxes API
  slug: hubspot-taxes-api
- description: 'The fees API allows you to create and manage fees that can be included in invoices and legacy quotes. Fees support fixed dollar amounts or percentage-based values and are used alongside discounts and '
  name: HubSpot Fees API
  slug: hubspot-fees-api
- description: The discounts API enables you to create and associate discounts as part of the pricing details for quotes. Discounts work alongside fees and taxes in the quote pricing workflow, being applied first in
  name: HubSpot Discounts API
  slug: hubspot-discounts-api
- description: The communications API allows you to log WhatsApp, LinkedIn, or SMS messages to CRM record timelines. You can create, retrieve, update, and manage message engagement records and associate them with co
  name: HubSpot Engagement Communications API
  slug: hubspot-engagement-communications-api
- description: The postal mail engagement API allows you to log postal mail sent to or received from contacts or companies on their CRM records. You can create, retrieve, update, and delete postal mail engagement re
  name: HubSpot Engagement Postal Mail API
  slug: hubspot-engagement-postal-mail-api
- description: The transactional email API enables sending template-based transactional emails through HubSpot using the Single Send API and managing SMTP tokens. You can send emails for commerce receipts, account u
  name: HubSpot Transactional Email API
  slug: hubspot-transactional-email-api
- description: 'The subscription preferences API allows you to manage email subscription details for contacts in your account. You can retrieve subscription types, check contact preferences, subscribe or unsubscribe '
  name: HubSpot Subscription Preferences API
  slug: hubspot-subscription-preferences-api
- description: The timeline events API enables technology partners to send custom event data from external systems into HubSpot for display on CRM record activity timelines. You can create event templates, define cu
  name: HubSpot Timeline Events API
  slug: hubspot-timeline-events-api
- description: 'The calling extensions SDK enables apps to provide a custom calling option to HubSpot users directly from CRM records. The SDK facilitates bidirectional communication between calling applications and '
  name: HubSpot Calling Extensions API
  slug: hubspot-calling-extensions-api
- description: The video conferencing API enables you to integrate custom video conferencing solutions into HubSpot's meeting creation workflow. You can configure webhook notifications for meeting creation, updates,
  name: HubSpot Video Conferencing API
  slug: hubspot-video-conferencing-api
- description: The account information API provides account configuration and usage data for HubSpot accounts. You can retrieve account details including portal ID, time zone, currency settings, and data center loca
  name: HubSpot Account Information API
  slug: hubspot-account-information-api
- description: 'The business units (brands) API provides information about brands tied to a HubSpot user. You can retrieve brand data including brand name, ID, and logo metadata for brands associated with a specific '
  name: HubSpot Business Units API
  slug: hubspot-business-units-api
- description: The currencies API allows you to manage the currencies used in your HubSpot account. You can set your account's company currency, create additional currencies, update exchange rates, and configure aut
  name: HubSpot Currencies API
  slug: hubspot-currencies-api
asyncapis:
- description: 'The HubSpot Webhooks API enables real-time event notifications for changes to CRM objects and conversations in a HubSpot portal. When subscribed events occur, HubSpot delivers HTTP POST requests to a '
  name: HubSpot Webhooks API
  slug: hubspot-webhooks-asyncapi
capabilities:
- description: Workflow automation and integration management combining custom workflow actions, OAuth, feature flags, and conversations.
  name: HubSpot Automation and Integration
  slug: automation-and-integration
- description: Unified workflow for admins to manage commerce payments, subscriptions, HubDB data tables, CMS pages, and domains. Combines commerce operations with CMS data management for platform administration.
  name: HubSpot Commerce Admin
  slug: commerce-admin
- description: Commerce workflow for managing payments and subscriptions.
  name: HubSpot Commerce Operations
  slug: commerce-operations
- description: Unified workflow for marketing managers to manage blog content, authors, landing pages, site pages, domains, analytics events, and transactional email. Combines CMS and marketing APIs into a single co
  name: HubSpot Content And Marketing
  slug: content-and-marketing
- description: Content creation and management workflow for blog posts, authors, pages, domains, and source code.
  name: HubSpot Content Management
  slug: content-management
- description: Unified CRM workflow for managing contacts, companies, deals, tickets, and their associations.
  name: HubSpot CRM Management
  slug: crm-management
- description: Unified workflow for service agents to manage support tickets, conversations, threads, messages, and CRM associations. Combines ticket management with conversation channels for complete customer servi
  name: HubSpot Customer Service
  slug: customer-service
- description: Unified workflow for developers to manage custom workflow actions, feature flags, CMS source code, and OAuth authentication. Combines automation, deployment, and auth APIs for HubSpot platform develop
  name: HubSpot Developer Platform
  slug: developer-platform
- description: Marketing automation workflow combining email campaigns and analytics events.
  name: HubSpot Marketing Automation
  slug: marketing-automation
- description: Sales activity tracking workflow for calls, emails, meetings, tasks, and notes.
  name: HubSpot Sales Engagement
  slug: sales-engagement
- description: Unified workflow for sales reps to manage contacts, companies, deals, engagement activities (calls, emails, meetings, notes, tasks), lists, and CRM search. Combines core CRM and engagement APIs for en
  name: HubSpot Sales Pipeline
  slug: sales-pipeline
common:
- title: ''
  type: APIReference
  url: https://api.hubspot.com/api-catalog-public/v1/apis
- title: ''
  type: Portal
  url: https://developers.hubspot.com/
- title: ''
  type: Documentation
  url: https://developers.hubspot.com/docs/api/overview
- title: ''
  type: ChangeLog
  url: https://developers.hubspot.com/changelog
- title: ''
  type: Support
  url: https://community.hubspot.com/t5/HubSpot-Developers/ct-p/developers
- title: ''
  type: Support
  url: https://developers.hubspot.com/slack
- title: ''
  type: Blog
  url: https://developers.hubspot.com/blog
- title: ''
  type: Newsletter
  url: https://offers.hubspot.com/developer-newsletter-signup
- title: ''
  type: Events
  url: https://www.hubspot.com/developer-community-events
- title: ''
  type: PrivacyPolicy
  url: https://legal.hubspot.com/privacy-policy
- title: ''
  type: TermsOfService
  url: https://legal.hubspot.com/terms-of-service
- title: ''
  type: GettingStarted
  url: https://developers.hubspot.com/docs/getting-started/overview
- title: ''
  type: Documentation
  url: https://developers.hubspot.com/docs/guides/api
- title: ''
  type: Documentation
  url: https://developers.hubspot.com/docs/reference/api/overview
- title: ''
  type: Login
  url: https://app.hubspot.com/login
- title: ''
  type: Contact
  url: https://offers.hubspot.com/crm-platform-demo
- title: ''
  type: Documentation
  url: https://www.hubspot.com/our-story
- title: ''
  type: Blog
  url: https://blog.hubspot.com/
- title: ''
  type: Security
  url: https://legal.hubspot.com/security
- title: ''
  type: Partners
  url: https://www.hubspot.com/partners/affiliates
- title: ''
  type: Partners
  url: https://www.hubspot.com/partners
- title: ''
  type: Pricing
  url: https://www.hubspot.com/pricing/marketing/enterprise
- title: ''
  type: Showcase
  url: https://www.hubspot.com/case-studies
- title: ''
  type: SignUp
  url: https://app.hubspot.com/signup/developers
- title: ''
  type: Authentication
  url: https://developers.hubspot.com/docs/api/intro-to-auth
- title: ''
  type: RateLimits
  url: https://developers.hubspot.com/docs/guides/apps/api-usage/usage-details
- title: ''
  type: StatusPage
  url: https://status.hubspot.com
- title: ''
  type: Support
  url: https://community.hubspot.com/t5/APIs-Integrations/bd-p/integrations
- title: ''
  type: GitHubOrganization
  url: https://github.com/HubSpot
- title: ''
  type: GitHubRepository
  url: https://github.com/HubSpot/HubSpot-public-api-spec-collection
- title: ''
  type: SDK
  url: https://developers.hubspot.com/docs/api/client-libraries
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/hubspot
- title: ''
  type: Resources
  url: https://www.postman.com/hubspot/hubspot-public-api-workspace/overview
- title: ''
  type: Resources
  url: https://developers.hubspot.com/developer-tools
- title: ''
  type: APIReference
  url: https://developers.hubspot.com/apisbytier
- title: ''
  type: JSONSchema
  url: json-schema/hubspot-crm-object-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/hubspot-crm-search-request-schema.json
- title: ''
  type: JSONLD
  url: json-ld/hubspot-context.jsonld
- title: Python SDK
  type: SDK
  url: https://pypi.org/project/hubspot-api-client/
- title: Node.js SDK
  type: SDK
  url: https://www.npmjs.com/package/@hubspot/api-client
- title: Ruby SDK
  type: SDK
  url: https://rubygems.org/gems/hubspot-api-client
- title: PHP SDK
  type: SDK
  url: https://packagist.org/packages/hubspot/api-client
- title: HubSpot CLI
  type: CLI
  url: https://www.npmjs.com/package/@hubspot/cli
- title: HubSpot MCP Server
  type: GitHubRepository
  url: https://github.com/HubSpot/mcp-server
- title: Calling Extensions SDK
  type: SDK
  url: https://github.com/HubSpot/calling-extensions-sdk
- title: ''
  type: JSONLD
  url: json-ld/hubspot-analytics-events-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-authors-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-blog-posts-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-cms-hubdb-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-cms-pages-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-commerce-payments-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-commerce-subscriptions-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-conversations-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-associations-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-companies-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-contacts-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-deals-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-feature-flags-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-lists-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-search-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-tickets-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-custom-workflow-actions-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-domains-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-calls-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-emails-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-meetings-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-association-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-batch-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-filter-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-gdpr-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-next-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-note-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-paging-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-property-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-sort-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-tasks-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-marketing-emal-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-oauth-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/hubspot-source-code-api-context.jsonld
- title: Spectral Rules
  type: Documentation
  url: rules/hubspot-spectral-rules.yml
- title: Vocabulary
  type: Documentation
  url: vocabulary/hubspot-vocabulary.yaml
- title: Naftiko Capability
  type: Documentation
  url: capabilities/automation-and-integration.yaml
- title: Naftiko Capability
  type: Documentation
  url: capabilities/commerce-operations.yaml
- title: Naftiko Capability
  type: Documentation
  url: capabilities/content-management.yaml
- title: Naftiko Capability
  type: Documentation
  url: capabilities/crm-management.yaml
- title: Naftiko Capability
  type: Documentation
  url: capabilities/marketing-automation.yaml
- title: Naftiko Capability
  type: Documentation
  url: capabilities/sales-engagement.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/analytics-events-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/authors-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/blog-posts-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/cms-hubdb-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/cms-pages-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/commerce-payments-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/commerce-subscriptions-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/conversations-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/crm-associations-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/crm-companies-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/crm-contacts-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/crm-deals-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/crm-feature-flags-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/crm-lists-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/crm-search-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/crm-tickets-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/custom-workflow-actions-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/domains-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/engagement-calls-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/engagement-emails-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/engagement-meetings-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/engagement-notes.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/engagement-tasks-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/marketing-emal-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/oauth-api.yaml
- title: Naftiko Shared Capability
  type: Documentation
  url: capabilities/shared/source-code-api.yaml
created: 2023/11/14
description: HubSpot provides a full platform of marketing, sales, customer service, and CRM software plus the methodology, resources, and support to help businesses grow better.
features:
- description: AI-powered tool that generates blog posts, landing pages, and marketing copy.
  name: AI Content Writer
- description: AI assistant that creates personalized email content for marketing and sales outreach.
  name: AI Email Writer
- description: AI tool that generates complete website pages from prompts and brand guidelines.
  name: AI Website Generator
- description: Create, personalize, and optimize marketing emails with drag-and-drop editor and A/B testing.
  name: Email Marketing Software
- description: Track email opens, clicks, and replies in real-time with desktop notifications.
  name: Email Tracking Software
- description: Build conversational chatbots to qualify leads and provide customer support 24/7.
  name: Free Chatbot Builder
- description: Drag-and-drop builder for creating high-converting landing pages without code.
  name: Free Landing Page Builder
- description: Real-time live chat widget for engaging website visitors and routing to sales or support.
  name: Free Live Chat Software
- description: Shareable scheduling links that sync with Google Calendar and Outlook.
  name: Free Meeting Scheduler App
- description: Create forms that automatically capture and sync leads into the CRM.
  name: Free Online Form Builder
- description: Fully managed web hosting for HubSpot CMS-built websites with SSL and CDN.
  name: Free Web Hosting
- description: Drag-and-drop website builder with responsive themes and SEO optimization.
  name: Free Website Builder
- description: Track, score, and nurture leads through the sales funnel with automated workflows.
  name: Lead Management Software
- description: Unified analytics dashboard for measuring campaign performance across channels.
  name: Marketing Analytics
- description: Reusable email templates with personalization tokens for consistent sales outreach.
  name: Sales Email Templates
image: https://www.hubspot.com/hubfs/HubSpot_Logos/HubSpot-Inversed-Favicon.png
integrations:
- description: Bi-directional CRM sync between HubSpot and Salesforce for unified sales and marketing data.
  name: Salesforce
- description: Send HubSpot notifications, create tasks, and share CRM data directly in Slack channels.
  name: Slack
- description: Sync contacts, calendar events, and emails between HubSpot and Google Workspace apps.
  name: Google Workspace
- description: Connect Outlook email, calendar, and contacts with HubSpot CRM for seamless productivity.
  name: Microsoft 365
- description: Automatically log Zoom meeting details and recordings on CRM contact timelines.
  name: Zoom
- description: Sync ecommerce order data, products, and customers between Shopify and HubSpot.
  name: Shopify
- description: Embed HubSpot forms, live chat, and analytics on WordPress sites with the official plugin.
  name: WordPress
- description: Process payments and sync transaction data between Stripe and HubSpot Commerce.
  name: Stripe
- description: Connect HubSpot with thousands of apps through automated Zapier workflows.
  name: Zapier
- description: Sync support tickets and development issues between HubSpot and Jira.
  name: Jira
- description: Sync invoices, payments, and customer data between HubSpot and QuickBooks.
  name: QuickBooks
- description: Share HubSpot CRM and marketing data with Snowflake for advanced analytics.
  name: Snowflake
- description: Track ad performance and sync audiences between HubSpot and Google Ads.
  name: Google Ads
- description: Create and manage Facebook ad campaigns with HubSpot audience targeting.
  name: Facebook Ads
- description: Sync LinkedIn lead gen forms and ads data with HubSpot for B2B marketing.
  name: LinkedIn
jsonld:
- class_count: 6
  name: Hubspot Analytics Events Api Context
  property_count: 14
  slug: hubspot-analytics-events-api-context
- class_count: 0
  name: Hubspot Analytics Events Context
  property_count: 8
  slug: hubspot-analytics-events-context
- class_count: 15
  name: Hubspot Authors Api Context
  property_count: 30
  slug: hubspot-authors-api-context
- class_count: 0
  name: Hubspot Authors Context
  property_count: 18
  slug: hubspot-authors-context
- class_count: 19
  name: Hubspot Blog Posts Api Context
  property_count: 52
  slug: hubspot-blog-posts-api-context
- class_count: 0
  name: Hubspot Blog Posts Context
  property_count: 22
  slug: hubspot-blog-posts-context
- class_count: 8
  name: Hubspot Cms Hubdb Api Context
  property_count: 15
  slug: hubspot-cms-hubdb-api-context
- class_count: 0
  name: Hubspot Cms Hubdb Context
  property_count: 9
  slug: hubspot-cms-hubdb-context
- class_count: 5
  name: Hubspot Cms Pages Api Context
  property_count: 20
  slug: hubspot-cms-pages-api-context
- class_count: 0
  name: Hubspot Cms Pages Context
  property_count: 6
  slug: hubspot-cms-pages-context
- class_count: 24
  name: Hubspot Commerce Payments Api Context
  property_count: 47
  slug: hubspot-commerce-payments-api-context
- class_count: 0
  name: Hubspot Commerce Payments Context
  property_count: 26
  slug: hubspot-commerce-payments-context
- class_count: 13
  name: Hubspot Commerce Subscriptions Api Context
  property_count: 22
  slug: hubspot-commerce-subscriptions-api-context
- class_count: 0
  name: Hubspot Commerce Subscriptions Context
  property_count: 14
  slug: hubspot-commerce-subscriptions-context
- class_count: 1
  name: Hubspot Context
  property_count: 49
  slug: hubspot-context
- class_count: 17
  name: Hubspot Conversations Api Context
  property_count: 40
  slug: hubspot-conversations-api-context
- class_count: 0
  name: Hubspot Conversations Context
  property_count: 19
  slug: hubspot-conversations-context
- class_count: 19
  name: Hubspot Crm Associations Api Context
  property_count: 28
  slug: hubspot-crm-associations-api-context
- class_count: 0
  name: Hubspot Crm Associations Context
  property_count: 22
  slug: hubspot-crm-associations-context
- class_count: 14
  name: Hubspot Crm Companies Api Context
  property_count: 22
  slug: hubspot-crm-companies-api-context
- class_count: 0
  name: Hubspot Crm Companies Context
  property_count: 15
  slug: hubspot-crm-companies-context
- class_count: 14
  name: Hubspot Crm Contacts Api Context
  property_count: 22
  slug: hubspot-crm-contacts-api-context
- class_count: 0
  name: Hubspot Crm Contacts Context
  property_count: 15
  slug: hubspot-crm-contacts-context
- class_count: 14
  name: Hubspot Crm Deals Api Context
  property_count: 22
  slug: hubspot-crm-deals-api-context
- class_count: 0
  name: Hubspot Crm Deals Context
  property_count: 15
  slug: hubspot-crm-deals-context
- class_count: 14
  name: Hubspot Crm Feature Flags Api Context
  property_count: 20
  slug: hubspot-crm-feature-flags-api-context
- class_count: 0
  name: Hubspot Crm Feature Flags Context
  property_count: 16
  slug: hubspot-crm-feature-flags-context
- class_count: 8
  name: Hubspot Crm Lists Api Context
  property_count: 21
  slug: hubspot-crm-lists-api-context
- class_count: 0
  name: Hubspot Crm Lists Context
  property_count: 9
  slug: hubspot-crm-lists-context
- class_count: 7
  name: Hubspot Crm Search Api Context
  property_count: 21
  slug: hubspot-crm-search-api-context
- class_count: 0
  name: Hubspot Crm Search Context
  property_count: 8
  slug: hubspot-crm-search-context
- class_count: 14
  name: Hubspot Crm Tickets Api Context
  property_count: 22
  slug: hubspot-crm-tickets-api-context
- class_count: 0
  name: Hubspot Crm Tickets Context
  property_count: 15
  slug: hubspot-crm-tickets-context
- class_count: 22
  name: Hubspot Custom Workflow Actions Api Context
  property_count: 39
  slug: hubspot-custom-workflow-actions-api-context
- class_count: 0
  name: Hubspot Custom Workflow Actions Context
  property_count: 24
  slug: hubspot-custom-workflow-actions-context
- class_count: 4
  name: Hubspot Domains Api Context
  property_count: 27
  slug: hubspot-domains-api-context
- class_count: 0
  name: Hubspot Domains Context
  property_count: 6
  slug: hubspot-domains-context
- class_count: 23
  name: Hubspot Engagement Calls Api Context
  property_count: 46
  slug: hubspot-engagement-calls-api-context
- class_count: 0
  name: Hubspot Engagement Calls Context
  property_count: 25
  slug: hubspot-engagement-calls-context
- class_count: 13
  name: Hubspot Engagement Emails Api Context
  property_count: 22
  slug: hubspot-engagement-emails-api-context
- class_count: 0
  name: Hubspot Engagement Emails Context
  property_count: 14
  slug: hubspot-engagement-emails-context
- class_count: 13
  name: Hubspot Engagement Meetings Api Context
  property_count: 22
  slug: hubspot-engagement-meetings-api-context
- class_count: 0
  name: Hubspot Engagement Meetings Context
  property_count: 14
  slug: hubspot-engagement-meetings-context
- class_count: 2
  name: Hubspot Engagement Notes Association Context
  property_count: 4
  slug: hubspot-engagement-notes-association-context
- class_count: 8
  name: Hubspot Engagement Notes Batch Context
  property_count: 15
  slug: hubspot-engagement-notes-batch-context
- class_count: 0
  name: Hubspot Engagement Notes Context
  property_count: 25
  slug: hubspot-engagement-notes-context
- class_count: 2
  name: Hubspot Engagement Notes Filter Context
  property_count: 6
  slug: hubspot-engagement-notes-filter-context
- class_count: 1
  name: Hubspot Engagement Notes Gdpr Context
  property_count: 2
  slug: hubspot-engagement-notes-gdpr-context
- class_count: 1
  name: Hubspot Engagement Notes Next Context
  property_count: 2
  slug: hubspot-engagement-notes-next-context
- class_count: 6
  name: Hubspot Engagement Notes Note Context
  property_count: 16
  slug: hubspot-engagement-notes-note-context
- class_count: 1
  name: Hubspot Engagement Notes Paging Context
  property_count: 1
  slug: hubspot-engagement-notes-paging-context
- class_count: 1
  name: Hubspot Engagement Notes Property Context
  property_count: 6
  slug: hubspot-engagement-notes-property-context
- class_count: 1
  name: Hubspot Engagement Notes Sort Context
  property_count: 2
  slug: hubspot-engagement-notes-sort-context
- class_count: 13
  name: Hubspot Engagement Tasks Api Context
  property_count: 22
  slug: hubspot-engagement-tasks-api-context
- class_count: 0
  name: Hubspot Engagement Tasks Context
  property_count: 14
  slug: hubspot-engagement-tasks-context
- class_count: 9
  name: Hubspot Marketing Emal Api Context
  property_count: 28
  slug: hubspot-marketing-emal-api-context
- class_count: 0
  name: Hubspot Marketing Emal Context
  property_count: 11
  slug: hubspot-marketing-emal-context
- class_count: 4
  name: Hubspot Oauth Api Context
  property_count: 17
  slug: hubspot-oauth-api-context
- class_count: 0
  name: Hubspot Oauth Context
  property_count: 6
  slug: hubspot-oauth-context
- class_count: 8
  name: Hubspot Source Code Api Context
  property_count: 23
  slug: hubspot-source-code-api-context
- class_count: 0
  name: Hubspot Source Code Context
  property_count: 10
  slug: hubspot-source-code-context
layout: provider
modified: '2026-04-18'
name: HubSpot
rules:
- name: HubSpot API Rules
  rule_count: 21
  severity_counts:
    error: 19
    hint: 0
    info: 1
    warn: 1
  slug: hubspot-spectral-rules
skills: []
slug: hubspot
solutions: []
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
url: https://raw.githubusercontent.com/apis-json/artisanal/main/apis/hubspot.yml
use_cases:
- description: Use AI to generate blog posts, social media content, and marketing copy at scale.
  name: AI-Powered Content Creation
- description: Leverage AI for lead scoring, deal forecasting, and automated sales email generation.
  name: AI-Powered Sales
- description: Track and analyze marketing, sales, and service performance with unified reporting dashboards.
  name: Analytics
- description: Create, manage, and publish website content, blog posts, and landing pages.
  name: Content Creation and Management
- description: Centralized content management for creating and distributing content across channels.
  name: Content Hub
- description: Manage customer support tickets, knowledge base, and feedback surveys.
  name: Customer Service
- description: Automate ticket routing, responses, and escalation with workflow-based support.
  name: Customer Support Automation
- description: Clean, deduplicate, and enrich CRM data with automated data quality tools.
  name: Data Management and Insights
- description: Track deals through customizable pipeline stages with forecasting and reporting.
  name: Deal Management
- description: Design, send, and analyze marketing email campaigns with segmentation and A/B testing.
  name: Email Marketing
- description: Connect with 1,500+ integrations in the HubSpot App Marketplace.
  name: HubSpot Ecosystem
- description: Attract visitors with SEO, blogs, and social media, then convert them with forms and CTAs.
  name: Inbound Marketing
- description: Connect apps and automate business processes with programmable workflows.
  name: Integration and Automation
- description: Build landing pages with embedded forms to capture and qualify leads.
  name: Landing Pages & Forms
- description: Capture leads through forms, chatbots, and CTAs, then nurture with automated sequences.
  name: Lead Generation and Conversion
- description: Engage website visitors in real-time with live chat and route conversations to the right team.
  name: Live Chat
- description: Sync, clean, and automate business data across systems with programmable automation.
  name: Operations Hub
- description: Manage sales teams with activity tracking, quotas, forecasting, and coaching tools.
  name: Sales Management
- description: Deliver customer service with ticketing, knowledge base, feedback, and customer portal.
  name: Service Hub
- description: Automate repetitive tasks across marketing, sales, and service with visual workflow builder.
  name: Workflows
---
