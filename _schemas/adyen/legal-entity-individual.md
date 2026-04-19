---
description: Individual schema from Adyen API
layout: schema
name: Individual
properties_list:
- description: The individual's birth information.
  name: birthData
  type: object
- description: The email address of the legal entity.
  name: email
  type: string
- description: Information about the individual's identification document.
  name: identificationData
  type: object
- description: The individual's name.
  name: name
  type: object
- description: The individual's nationality.
  name: nationality
  type: string
- description: The phone number of the legal entity.
  name: phone
  type: object
- description: The residential address of the individual.
  name: residentialAddress
  type: object
- description: The tax information of the individual.
  name: taxInformation
  type: array
- description: The website and app URL of the legal entity.
  name: webData
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-individual-schema.json
slug: legal-entity-individual
tags:
- Payments
- Financial Services
- Fintech
title: Individual
---
