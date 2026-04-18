---
channels:
- description: Triggered when a new contact record is created in the portal. The event payload includes the ID of the newly created contact and metadata about the creation event.
  name: contact.creation
  operation: subscribe
  operation_id: onContactCreation
  summary: Contact created
- description: Triggered when a contact record is deleted (archived) from the portal. The event payload includes the ID of the deleted contact.
  name: contact.deletion
  operation: subscribe
  operation_id: onContactDeletion
  summary: Contact deleted
- description: Triggered when a property value changes on a contact record. The event payload includes the property name, new value, and the contact's ID.
  name: contact.propertyChange
  operation: subscribe
  operation_id: onContactPropertyChange
  summary: Contact property changed
- description: Triggered when a new company record is created in the portal.
  name: company.creation
  operation: subscribe
  operation_id: onCompanyCreation
  summary: Company created
- description: Triggered when a company record is deleted (archived) from the portal.
  name: company.deletion
  operation: subscribe
  operation_id: onCompanyDeletion
  summary: Company deleted
- description: Triggered when a property value changes on a company record.
  name: company.propertyChange
  operation: subscribe
  operation_id: onCompanyPropertyChange
  summary: Company property changed
- description: Triggered when a new deal record is created in the portal.
  name: deal.creation
  operation: subscribe
  operation_id: onDealCreation
  summary: Deal created
- description: Triggered when a deal record is deleted (archived) from the portal.
  name: deal.deletion
  operation: subscribe
  operation_id: onDealDeletion
  summary: Deal deleted
- description: Triggered when a property value changes on a deal record.
  name: deal.propertyChange
  operation: subscribe
  operation_id: onDealPropertyChange
  summary: Deal property changed
- description: Triggered when a new ticket record is created in the portal.
  name: ticket.creation
  operation: subscribe
  operation_id: onTicketCreation
  summary: Ticket created
- description: Triggered when a ticket record is deleted (archived) from the portal.
  name: ticket.deletion
  operation: subscribe
  operation_id: onTicketDeletion
  summary: Ticket deleted
- description: Triggered when a property value changes on a ticket record.
  name: ticket.propertyChange
  operation: subscribe
  operation_id: onTicketPropertyChange
  summary: Ticket property changed
- description: Triggered when a new conversation thread is created in the HubSpot conversations inbox.
  name: conversation.creation
  operation: subscribe
  operation_id: onConversationCreation
  summary: Conversation created
- description: Triggered when a conversation thread is deleted from the portal.
  name: conversation.deletion
  operation: subscribe
  operation_id: onConversationDeletion
  summary: Conversation deleted
- description: Triggered when a property changes on a conversation thread.
  name: conversation.propertyChange
  operation: subscribe
  operation_id: onConversationPropertyChange
  summary: Conversation property changed
- description: Triggered when a new message is added to an existing conversation thread.
  name: conversation.newMessage
  operation: subscribe
  operation_id: onConversationNewMessage
  summary: New conversation message
description: The HubSpot Webhooks API enables real-time event notifications for changes to CRM objects and conversations in a HubSpot portal. When subscribed events occur, HubSpot delivers HTTP POST requests to a registered target URL containing details about the event. Webhooks support subscription types for contacts, companies, deals, tickets, and conversations.
layout: asyncapi
messages:
- description: Payload delivered when a new contact record is created in the HubSpot portal. The objectId identifies the newly created contact.
  name: ContactCreationEvent
  summary: A contact record was created.
  title: Contact Creation Event
- description: ''
  name: ContactDeletionEvent
  summary: A contact record was deleted.
  title: Contact Deletion Event
- description: ''
  name: ContactPropertyChangeEvent
  summary: A contact property value was changed.
  title: Contact Property Change Event
- description: ''
  name: CompanyCreationEvent
  summary: A company record was created.
  title: Company Creation Event
- description: ''
  name: CompanyDeletionEvent
  summary: A company record was deleted.
  title: Company Deletion Event
- description: ''
  name: CompanyPropertyChangeEvent
  summary: A company property value was changed.
  title: Company Property Change Event
- description: ''
  name: DealCreationEvent
  summary: A deal record was created.
  title: Deal Creation Event
- description: ''
  name: DealDeletionEvent
  summary: A deal record was deleted.
  title: Deal Deletion Event
- description: ''
  name: DealPropertyChangeEvent
  summary: A deal property value was changed.
  title: Deal Property Change Event
- description: ''
  name: TicketCreationEvent
  summary: A ticket record was created.
  title: Ticket Creation Event
- description: ''
  name: TicketDeletionEvent
  summary: A ticket record was deleted.
  title: Ticket Deletion Event
- description: ''
  name: TicketPropertyChangeEvent
  summary: A ticket property value was changed.
  title: Ticket Property Change Event
- description: ''
  name: ConversationCreationEvent
  summary: A conversation was created.
  title: Conversation Creation Event
- description: ''
  name: ConversationDeletionEvent
  summary: A conversation was deleted.
  title: Conversation Deletion Event
- description: ''
  name: ConversationPropertyChangeEvent
  summary: A conversation property was changed.
  title: Conversation Property Change Event
- description: ''
  name: ConversationNewMessageEvent
  summary: A new message was added to a conversation.
  title: Conversation New Message Event
name: HubSpot Webhooks API
provider_name: HubSpot
provider_slug: hubspot
servers:
- description: HubSpot management API for configuring webhook settings and subscriptions. Webhook events are delivered to the target URL configured in your app settings.
  name: hubspot-api
  protocol: https
  url: https://api.hubapi.com
slug: hubspot-webhooks-asyncapi
spec_file: asyncapi/hubspot-webhooks-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/asyncapi/hubspot-webhooks-asyncapi.yml
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
- AsyncAPI
- Webhooks
- Events
version: v3
---
