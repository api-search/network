---
description: AccountHolder schema from Adyen API
layout: schema
name: AccountHolder
properties_list:
- description: 'The unique identifier of the [balance platform](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id) to which the account holder belongs. Required in '
  name: balancePlatform
  type: string
- description: Contains key-value pairs that specify the actions that an account holder can do in your platform. The key is a capability required for your integration. For example, **issueCard** for Issuing. The val
  name: capabilities
  type: object
- description: Contact details of the account holder.
  name: contactDetails
  type: object
- description: Your description for the account holder, maximum 300 characters.
  name: description
  type: string
- description: The unique identifier of the account holder.
  name: id
  type: string
- description: 'The unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities__resParam_id) associated with the account holder. Adyen performs a verification '
  name: legalEntityId
  type: string
- description: The ID of the account holder's primary balance account. By default, this is set to the first balance account that you create for the account holder. To assign a different balance account, send a PATCH
  name: primaryBalanceAccount
  type: string
- description: Your reference for the account holder, maximum 150 characters.
  name: reference
  type: string
- description: 'The status of the account holder. Possible values: * **Active**: The account holder is active. This is the default status when creating an account holder. * **Inactive**: The account holder is tempora'
  name: status
  type: string
- description: The [time zone](https://www.iana.org/time-zones) of the account holder. For example, **Europe/Amsterdam**. If not set, the time zone of the balance account will be used. For possible values, see the [
  name: timeZone
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-account-holder-schema.json
slug: notification-webhooks-account-holder
tags:
- Payments
- Financial Services
- Fintech
title: AccountHolder
---
