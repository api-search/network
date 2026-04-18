---
description: A Salesforce SObject record. Contains an attributes object describing the record type and URL, plus any number of field name/value pairs depending on the object type.
layout: schema
name: SObjectRecord
properties_list:
- description: Metadata attributes for this SObject record, including its type and REST API URL.
  name: attributes
  type: object
- description: The 18-character globally unique Salesforce record ID.
  name: Id
  type: string
provider_name: Salesforce
provider_slug: salesforce
schema_file: json-schema/salesforce-rest-s-object-record-schema.json
slug: salesforce-rest-s-object-record
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
title: SObjectRecord
---
