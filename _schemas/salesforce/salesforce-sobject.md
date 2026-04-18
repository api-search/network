---
description: A Salesforce SObject record as returned by the REST API. Contains an attributes object with type and URL metadata, an Id field with the 18-character record identifier, and dynamic fields specific to the object type (e.g., Name, Email, Phone for Contact).
layout: schema
name: Salesforce SObject Record
properties_list:
- description: ''
  name: attributes
  type: object
- description: The globally unique 18-character Salesforce record identifier. The first three characters are the key prefix identifying the object type, followed by a unique alphanumeric string.
  name: Id
  type: string
- description: The primary display name field for the record. For most standard objects this is the Name field; for Person Accounts and Contacts it may be a combination of first and last name.
  name: Name
  type:
  - string
  - 'null'
- description: The date and time the record was created, in ISO 8601 format with UTC timezone (e.g., 2024-01-15T10:30:00.000+0000).
  name: CreatedDate
  type:
  - string
  - 'null'
- description: The 18-character ID of the Salesforce user who created this record.
  name: CreatedById
  type:
  - string
  - 'null'
- description: The date and time the record was last modified, in ISO 8601 format with UTC timezone.
  name: LastModifiedDate
  type:
  - string
  - 'null'
- description: The 18-character ID of the Salesforce user who last modified this record.
  name: LastModifiedById
  type:
  - string
  - 'null'
- description: The date and time of the last system-level modification to the record. This is updated by any change to the record including system changes, unlike LastModifiedDate which reflects user changes only.
  name: SystemModstamp
  type:
  - string
  - 'null'
- description: Whether the record has been moved to the Recycle Bin (soft deleted). Records where IsDeleted is true are not returned by standard SOQL queries but can be retrieved using queryAll.
  name: IsDeleted
  type:
  - boolean
  - 'null'
- description: The 18-character ID of the user or queue that owns this record. Ownership controls access and assignment rules.
  name: OwnerId
  type:
  - string
  - 'null'
- description: The 18-character ID of the Record Type applied to this record. Record types allow different picklist values, page layouts, and business processes for the same object.
  name: RecordTypeId
  type:
  - string
  - 'null'
- description: The billing address for account records. A structured address object with street, city, state, postal code, country, and optional geolocation fields.
  name: BillingAddress
  type: object
- description: The shipping address for account records. A structured address object with street, city, state, postal code, country, and optional geolocation fields.
  name: ShippingAddress
  type: object
- description: The mailing address for contact records. A structured address object with street, city, state, postal code, country, and optional geolocation fields.
  name: MailingAddress
  type: object
- description: An alternate address for contact records. A structured address object with street, city, state, postal code, country, and optional geolocation fields.
  name: OtherAddress
  type: object
- description: The primary phone number for the record. Stored as a string to preserve formatting; no specific format is enforced by Salesforce.
  name: Phone
  type: object
- description: The fax number for the record. Stored as a string to preserve formatting.
  name: Fax
  type: object
- description: The mobile phone number for contact and lead records. Stored as a string to preserve formatting.
  name: MobilePhone
  type: object
provider_name: Salesforce
provider_slug: salesforce
schema_file: json-schema/salesforce-sobject-schema.json
slug: salesforce-sobject
tags:
- AI
- Analytics
- Cloud
- Commerce
- CRM
- Customer Service
- Enterprise
- Marketing
- Platform
- Sales
title: Salesforce SObject Record
---
