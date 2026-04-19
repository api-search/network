---
description: A unified customer profile representing an individual across Adobe Experience Cloud products, combining identity data, demographic attributes, behavioral signals, and segment memberships.
layout: schema
name: Adobe Experience Cloud Profile
properties_list:
- description: The unique identifier for the unified profile.
  name: profileId
  type: string
- description: A map of identity namespaces to identity values associated with this profile.
  name: identityMap
  type: object
- description: Demographic information about the individual.
  name: person
  type: object
- description: The personal email address.
  name: personalEmail
  type: object
- description: The mobile phone number.
  name: mobilePhone
  type: object
- description: The home postal address.
  name: homeAddress
  type: object
- description: A map of segment namespace to segment membership details.
  name: segmentMembership
  type: object
- description: Privacy and marketing consent preferences.
  name: consents
  type: object
- description: When the profile was first created.
  name: created
  type: string
- description: When the profile was last updated.
  name: lastModified
  type: string
provider_name: Adobe Experience Cloud
provider_slug: adobe-experience-cloud
schema_file: json-schema/adobe-experience-cloud-profile.json
slug: adobe-experience-cloud-profile
tags:
- Analytics
- Customer Experience
- Digital Marketing
- Personalization
- Campaign Management
- Journey Orchestration
title: Adobe Experience Cloud Profile
---
