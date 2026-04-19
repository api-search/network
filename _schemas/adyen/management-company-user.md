---
description: CompanyUser schema from Adyen API
layout: schema
name: CompanyUser
properties_list:
- description: References to resources connected with this user.
  name: _links
  type: object
- description: The list of [account groups](https://docs.adyen.com/account/account-structure#account-groups) associated with this user.
  name: accountGroups
  type: array
- description: Indicates whether this user is active.
  name: active
  type: boolean
- description: Set of apps available to this user
  name: apps
  type: array
- description: The list of [merchant accounts](https://docs.adyen.com/account/account-structure#merchant-accounts) associated with this user.
  name: associatedMerchantAccounts
  type: array
- description: The email address of the user.
  name: email
  type: string
- description: The unique identifier of the user.
  name: id
  type: string
- description: The user's full name.
  name: name
  type: object
- description: The list of [roles](https://docs.adyen.com/account/user-roles) for this user.
  name: roles
  type: array
- description: The [tz database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the time zone of the user. For example, **Europe/Amsterdam**.
  name: timeZoneCode
  type: string
- description: The username for this user.
  name: username
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-company-user-schema.json
slug: management-company-user
tags:
- Payments
- Financial Services
- Fintech
title: CompanyUser
---
