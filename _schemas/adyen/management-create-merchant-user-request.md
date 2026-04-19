---
description: CreateMerchantUserRequest schema from Adyen API
layout: schema
name: CreateMerchantUserRequest
properties_list:
- description: The list of [account groups](https://docs.adyen.com/account/account-structure#account-groups) associated with this user.
  name: accountGroups
  type: array
- description: The email address of the user.
  name: email
  type: string
- description: 'The user''s full name. Allowed length: 1—80 characters.'
  name: name
  type: object
- description: The list of [roles](https://docs.adyen.com/account/user-roles) for this user.
  name: roles
  type: array
- description: The [tz database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the time zone of the user. For example, **Europe/Amsterdam**.
  name: timeZoneCode
  type: string
- description: The user's email address that will be their username. Must be the same as the one in the `email` field.
  name: username
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-create-merchant-user-request-schema.json
slug: management-create-merchant-user-request
tags:
- Payments
- Financial Services
- Fintech
title: CreateMerchantUserRequest
---
