---
description: BankAccountDetail schema from Adyen API
layout: schema
name: BankAccountDetail
properties_list:
- description: The bank account number (without separators). >Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field
  name: accountNumber
  type: string
- description: 'The type of bank account. Only applicable to bank accounts held in the USA. The permitted values are: `checking`, `savings`. >Refer to [Required information](https://docs.adyen.com/marketplaces-and-pl'
  name: accountType
  type: string
- description: The name of the bank account.
  name: bankAccountName
  type: string
- description: Merchant reference to the bank account.
  name: bankAccountReference
  type: string
- description: 'The unique identifier (UUID) of the Bank Account. >If, during an account holder create or update request, this field is left blank (but other fields provided), a new Bank Account will be created with '
  name: bankAccountUUID
  type: string
- description: The bank identifier code. >Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.
  name: bankBicSwift
  type: string
- description: The city in which the bank branch is located. >Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field
  name: bankCity
  type: string
- description: The bank code of the banking institution with which the bank account is registered. >Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/requ
  name: bankCode
  type: string
- description: The name of the banking institution with which the bank account is held. >Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-inform
  name: bankName
  type: string
- description: 'The branch code of the branch under which the bank account is registered. The value to be specified in this parameter depends on the country of the bank account: * United States - Routing number * Uni'
  name: branchCode
  type: string
- description: The check code of the bank account. >Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requireme
  name: checkCode
  type: string
- description: The two-letter country code in which the bank account is registered. >The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL'). >Refer to [Required information](https://docs.adyen.com
  name: countryCode
  type: string
- description: The currency in which the bank account deals. >The permitted currency codes are defined in ISO-4217 (e.g. 'EUR').
  name: currencyCode
  type: string
- description: The international bank account number. >The IBAN standard is defined in ISO-13616. >Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/requi
  name: iban
  type: string
- description: The city of residence of the bank account owner. >Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on fi
  name: ownerCity
  type: string
- description: The country code of the country of residence of the bank account owner. >The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL'). >Refer to [Required information](https://docs.adyen.
  name: ownerCountryCode
  type: string
- description: The date of birth of the bank account owner. The date should be in ISO-8601 format yyyy-mm-dd (e.g. 2000-01-31).
  name: ownerDateOfBirth
  type: string
- description: The house name or number of the residence of the bank account owner. >Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-informatio
  name: ownerHouseNumberOrName
  type: string
- description: The name of the bank account owner. >Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requireme
  name: ownerName
  type: string
- description: The country code of the country of nationality of the bank account owner. >The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL'). >Refer to [Required information](https://docs.adye
  name: ownerNationality
  type: string
- description: The postal code of the residence of the bank account owner. >Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for de
  name: ownerPostalCode
  type: string
- description: The state of residence of the bank account owner. >Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on f
  name: ownerState
  type: string
- description: The street name of the residence of the bank account owner. >Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for de
  name: ownerStreet
  type: string
- description: If set to true, the bank account is a primary account.
  name: primaryAccount
  type: boolean
- description: The tax ID number. >Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.
  name: taxId
  type: string
- description: The URL to be used for bank account verification. This may be generated on bank account creation. >Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verificatio
  name: urlForVerification
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-bank-account-detail-schema.json
slug: funds-bank-account-detail
tags:
- Payments
- Financial Services
- Fintech
title: BankAccountDetail
---
