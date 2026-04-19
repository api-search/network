---
description: AccountHolderInfo schema from Adyen API
layout: schema
name: AccountHolderInfo
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
- description: The unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id) associated with the account holder. Adyen performs a verificatio
  name: legalEntityId
  type: string
- description: A set of key and value pairs for general use. The keys do not have specific names and may be used for storing miscellaneous data as desired. > Note that during an update of metadata, the omission of e
  name: metadata
  type: object
- description: The unique identifier of the migrated account holder in the classic integration.
  name: migratedAccountHolderCode
  type: string
- description: Your reference for the account holder, maximum 150 characters.
  name: reference
  type: string
- description: The time zone of the account holder. For example, **Europe/Amsterdam**. Defaults to the time zone of the balance platform if no time zone is set. For possible values, see the [list of time zone codes]
  name: timeZone
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-account-holder-info-schema.json
slug: configuration-account-holder-info
tags:
- Payments
- Financial Services
- Fintech
title: AccountHolderInfo
---
