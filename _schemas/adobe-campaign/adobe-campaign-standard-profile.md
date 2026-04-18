---
description: Profile from Adobe Campaign API
layout: schema
name: Profile
properties_list:
- description: Unique identifier for the profile.
  name: PKey
  type: string
- description: Email address of the profile.
  name: email
  type: string
- description: First name of the profile.
  name: firstName
  type: string
- description: Last name of the profile.
  name: lastName
  type: string
- description: Phone number of the profile.
  name: phone
  type: string
- description: Mobile phone number.
  name: mobilePhone
  type: string
- description: Date of birth.
  name: birthDate
  type: string
- description: Gender of the profile.
  name: gender
  type: string
- description: Preferred language code.
  name: preferredLanguage
  type: string
- description: Whether the profile is on the deny list.
  name: blackList
  type: boolean
- description: Whether email is blocked for this profile.
  name: blackListEmail
  type: boolean
- description: Whether SMS is blocked for this profile.
  name: blackListMobile
  type: boolean
- description: Profile creation timestamp.
  name: created
  type: string
- description: Last modification timestamp.
  name: lastModified
  type: string
- description: Link to the profile subscriptions.
  name: subscriptions
  type: object
provider_name: Adobe Campaign
provider_slug: adobe-campaign
schema_file: json-schema/adobe-campaign-standard-profile-schema.json
slug: adobe-campaign-standard-profile
tags:
- Campaign Management
- Customer Experience
- Email Marketing
- Marketing Automation
- Multi-Channel Marketing
title: Profile
---
