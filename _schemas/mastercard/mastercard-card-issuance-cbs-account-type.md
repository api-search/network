---
description: Bank ISO Account Type in CBS. <br/> **Conditional Mandatory**<font color='red'>* </font> field - Required while linking new debit account. Possible values configured in CSR portal on "Card Management > Institution Parameter Setup > Account Type [ISSS12]" screen. CBS Host account type must be configured to match with ISO account types like 10, 20. <br/> **Possible values:** <br/> * `DEFAULT` - Default Account * `SAVINGS` - Savings Account * `CHECKING` - Checking or Current Account * `CREDIT_CARD` - Credit Card Account * `CREDIT_LINE` - Credit Line Account * `CORPORATE` - Corporate Account * `UNIVERSAL` - Universal Account * `MONEY_MARKET_INVESTMENT` - Money Market Investment Account * `IRA_INVESTMENT` - Ira Investment Account * `STORED_VALUE` - Stored Value Account * `REVOLVING_LOAN` - Revolving Loan Account * `INSTALLMENT_LOAN` - Installment Loan Account * `REAL_ESTATE_LOAN` - Real Estate Loan Account
layout: schema
name: CbsAccountType
properties_list: []
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-card-issuance-cbs-account-type-schema.json
slug: mastercard-card-issuance-cbs-account-type
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: CbsAccountType
---
