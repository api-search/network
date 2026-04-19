---
class_count: 31
classes:
- id
- type
- Account
- CurrentAccount
- SavingsAccount
- CorporateAccount
- IslamicAccount
- DepositAccount
- LoanAccount
- Customer
- CorporateCustomer
- Beneficiary
- Transaction
- FundTransfer
- PaymentOrder
- StandingOrder
- DirectDebit
- Product
- DepositProduct
- LoanProduct
- CardProduct
- Card
- DebitCard
- CreditCard
- Currency
- Country
- Address
- counterparty
- description
- status
- audit
context_file: json-ld/temenos-transact-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/temenos-transact/refs/heads/main/json-ld/temenos-transact-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Temenos Transact from Temenos Transact.
layout: jsonld
name: Temenos Transact Context
namespaces:
- prefix: temenos
  uri: https://developer.temenos.com/ns/transact/
- prefix: fibo
  uri: https://spec.edmcouncil.org/fibo/ontology/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: schema
  uri: https://schema.org/
properties:
- container: ''
  name: accountId
  type: string
- container: ''
  name: accountName
  type: string
- container: ''
  name: accountType
  type: string
- container: ''
  name: customerId
  type: string
- container: ''
  name: customerName
  type: string
- container: ''
  name: customerMnemonic
  type: string
- container: ''
  name: shortName
  type: string
- container: list
  name: displayNames
  type: ''
- container: list
  name: customerNames
  type: ''
- container: ''
  name: title
  type: string
- container: ''
  name: gender
  type: string
- container: ''
  name: dateOfBirth
  type: date
- container: ''
  name: nationalityId
  type: string
- container: ''
  name: residenceId
  type: string
- container: list
  name: communicationDevices
  type: ''
- container: ''
  name: deviceType
  type: string
- container: ''
  name: deviceValue
  type: string
- container: list
  name: addresses
  type: ''
- container: ''
  name: addressType
  type: string
- container: ''
  name: addressLine1
  type: string
- container: ''
  name: addressLine2
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: postCode
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: transactionId
  type: string
- container: ''
  name: transactionType
  type: string
- container: ''
  name: debitOrCredit
  type: string
- container: ''
  name: amount
  type: decimal
- container: ''
  name: currency
  type: string
- container: ''
  name: bookingDate
  type: date
- container: ''
  name: valueDate
  type: date
- container: ''
  name: processingDate
  type: date
- container: ''
  name: reference
  type: string
- container: ''
  name: endToEndReference
  type: string
- container: ''
  name: narrative
  type: string
- container: ''
  name: counterpartyName
  type: string
- container: ''
  name: counterpartyAccountId
  type: string
- container: ''
  name: balance
  type: decimal
- container: ''
  name: workingBalance
  type: decimal
- container: ''
  name: availableBalance
  type: decimal
- container: ''
  name: clearedBalance
  type: decimal
- container: ''
  name: lockedAmount
  type: decimal
- container: ''
  name: overdraftLimit
  type: decimal
- container: ''
  name: accruedInterest
  type: decimal
- container: ''
  name: exchangeRate
  type: decimal
- container: ''
  name: chargesAmount
  type: decimal
- container: ''
  name: reversalIndicator
  type: boolean
- container: ''
  name: statementNumber
  type: string
- container: ''
  name: transactionStatus
  type: string
- container: ''
  name: channel
  type: string
- container: ''
  name: paymentMethod
  type: string
- container: ''
  name: debitAccountId
  type: string
- container: ''
  name: creditAccountId
  type: string
- container: ''
  name: debitAmount
  type: decimal
- container: ''
  name: creditAmount
  type: decimal
- container: ''
  name: debitCurrency
  type: string
- container: ''
  name: creditCurrency
  type: string
- container: ''
  name: transferType
  type: string
- container: ''
  name: paymentType
  type: string
- container: ''
  name: beneficiaryId
  type: string
- container: ''
  name: beneficiaryName
  type: string
- container: ''
  name: beneficiaryIban
  type: string
- container: ''
  name: beneficiaryBic
  type: string
- container: ''
  name: beneficiaryType
  type: string
- container: ''
  name: remittanceInformation
  type: string
- container: ''
  name: chargesType
  type: string
- container: ''
  name: iban
  type: string
- container: ''
  name: bic
  type: string
- container: ''
  name: bankName
  type: string
- container: ''
  name: frequency
  type: string
- container: ''
  name: startDate
  type: date
- container: ''
  name: endDate
  type: date
- container: ''
  name: nextPaymentDate
  type: date
- container: ''
  name: productId
  type: string
- container: ''
  name: productName
  type: string
- container: ''
  name: productGroup
  type: string
- container: ''
  name: principalAmount
  type: decimal
- container: ''
  name: outstandingBalance
  type: decimal
- container: ''
  name: interestRate
  type: decimal
- container: ''
  name: effectiveRate
  type: decimal
- container: ''
  name: maturityDate
  type: date
- container: ''
  name: disbursementDate
  type: date
- container: ''
  name: term
  type: string
- container: ''
  name: renewalType
  type: string
- container: ''
  name: repaymentFrequency
  type: string
- container: ''
  name: cardId
  type: string
- container: ''
  name: cardNumber
  type: string
- container: ''
  name: cardType
  type: string
- container: ''
  name: cardholderName
  type: string
- container: ''
  name: expiryDate
  type: string
- container: ''
  name: dailyLimit
  type: decimal
- container: ''
  name: availableLimit
  type: decimal
- container: ''
  name: currencyCode
  type: string
- container: ''
  name: currencyName
  type: string
- container: ''
  name: decimalPlaces
  type: integer
- container: ''
  name: buyRate
  type: decimal
- container: ''
  name: sellRate
  type: decimal
- container: ''
  name: midRate
  type: decimal
- container: ''
  name: countryCode
  type: string
- container: ''
  name: countryName
  type: string
- container: ''
  name: openingDate
  type: date
- container: ''
  name: branchId
  type: string
- container: ''
  name: accountOfficerId
  type: integer
- container: ''
  name: sectorId
  type: integer
- container: ''
  name: industryId
  type: integer
- container: ''
  name: language
  type: integer
- container: ''
  name: customerStatus
  type: integer
- container: ''
  name: customerCompany
  type: string
- container: ''
  name: amlCheck
  type: string
- container: ''
  name: amlResult
  type: string
- container: ''
  name: kycStatus
  type: string
- container: ''
  name: executionDate
  type: date
- container: ''
  name: totalCharges
  type: decimal
- container: ''
  name: rejectionReason
  type: string
- container: ''
  name: createdBy
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: modifiedBy
  type: string
- container: ''
  name: modifiedAt
  type: dateTime
- container: ''
  name: authorizedBy
  type: string
- container: ''
  name: authorizedAt
  type: dateTime
property_count: 121
provider_name: Temenos Transact
provider_slug: temenos-transact
slug: temenos-transact-context
tags:
- Banking
- Core Banking
- Digital Banking
- Enterprise
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
