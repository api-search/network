---
description: Represents a contact in Marketing Cloud. A contact is an individual who interacts with marketing campaigns across channels.
layout: schema
name: Contact
properties_list:
- description: Unique identifier for the contact. This value is used across all Marketing Cloud channels and applications.
  name: contactKey
  type: string
- description: System-generated unique numeric identifier
  name: contactID
  type: integer
- description: Current status of the contact
  name: contactStatus
  type: string
- description: Date and time the contact was created
  name: createdDate
  type: string
- description: Date and time the contact was last modified
  name: modifiedDate
  type: string
- description: Collection of attribute sets associated with the contact
  name: attributeSets
  type: array
provider_name: Salesforce Marketing Cloud
provider_slug: salesforce-marketing-cloud
schema_file: json-schema/salesforce-marketing-cloud-contact-schema.json
slug: salesforce-marketing-cloud-contact
tags:
- Automation
- Customer Journey
- Digital Marketing
- Email
- Marketing
- Personalization
title: Contact
---
