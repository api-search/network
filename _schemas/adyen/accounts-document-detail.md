---
description: DocumentDetail schema from Adyen API
layout: schema
name: DocumentDetail
properties_list:
- description: The code of account holder, to which the document applies.
  name: accountHolderCode
  type: string
- description: The Adyen-generated [`bankAccountUUID`](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder__resParam_accountHolderDetails-bankAccountDetails-bankAccountUUID) to which the do
  name: bankAccountUUID
  type: string
- description: Description of the document.
  name: description
  type: string
- description: The type of the document. Refer to [Verification checks](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-checks) for details on when each document type should be submitted and f
  name: documentType
  type: string
- description: Filename of the document.
  name: filename
  type: string
- description: The Adyen-generated [`legalArrangementCode`](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder__resParam_accountHolderDetails-legalArrangements-legalArrangementCode) to whi
  name: legalArrangementCode
  type: string
- description: The Adyen-generated [`legalArrangementEntityCode`](https://docs.adyen.com/api-explorer/#/Account/v6/post/createAccountHolder__resParam_accountHolderDetails-legalArrangements-legalArrangementEntities-l
  name: legalArrangementEntityCode
  type: string
- description: The Adyen-generated [`shareholderCode`](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder__resParam_accountHolderDetails-businessDetails-shareholders-shareholderCode) to wh
  name: shareholderCode
  type: string
- description: The Adyen-generated [`signatoryCode`](https://docs.adyen.com/api-explorer/#/Account/v6/post/createAccountHolder__resParam_accountHolderDetails-businessDetails-signatories-signatoryCode) to which the d
  name: signatoryCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-document-detail-schema.json
slug: accounts-document-detail
tags:
- Payments
- Financial Services
- Fintech
title: DocumentDetail
---
