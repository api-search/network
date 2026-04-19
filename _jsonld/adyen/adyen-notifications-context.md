---
class_count: 86
classes:
- AccountCloseNotification
- AccountCreateNotification
- AccountEvent
- AccountFundsBelowThresholdNotificationContent
- AccountFundsBelowThresholdNotification
- AccountHolderCreateNotification
- AccountHolderDetails
- AccountHolderPayoutNotificationContent
- AccountHolderPayoutNotification
- AccountHolderStatusChangeNotificationContent
- AccountHolderStatusChangeNotification
- AccountHolderStatus
- AccountHolderStoreStatusChangeNotificationContent
- AccountHolderStoreStatusChangeNotification
- AccountHolderUpcomingDeadlineNotificationContent
- AccountHolderUpcomingDeadlineNotification
- AccountHolderUpdateNotification
- AccountHolderVerificationNotificationContent
- AccountHolderVerificationNotification
- AccountPayoutState
- AccountProcessingState
- AccountUpdateNotification
- Amount
- BankAccountDetail
- BeneficiarySetupNotificationContent
- BeneficiarySetupNotification
- BusinessDetails
- CloseAccountResponse
- CompensateNegativeBalanceNotificationContent
- CompensateNegativeBalanceNotificationRecord
- CompensateNegativeBalanceNotification
- CreateAccountHolderResponse
- CreateAccountResponse
- DirectDebitInitiatedNotificationContent
- DirectDebitInitiatedNotification
- ErrorFieldType
- FieldType
- IndividualDetails
- KYCCheckResult
- KYCCheckStatusData
- KYCCheckSummary
- KYCLegalArrangementCheckResult
- KYCLegalArrangementEntityCheckResult
- KYCPayoutMethodCheckResult
- KYCShareholderCheckResult
- KYCSignatoryCheckResult
- KYCUltimateParentCompanyCheckResult
- KYCVerificationResult
- LegalArrangementDetail
- LegalArrangementEntityDetail
- LocalDate
- Message
- NotificationErrorContainer
- NotificationResponse
- OperationStatus
- PaymentFailureNotificationContent
- PaymentFailureNotification
- PayoutMethod
- PayoutScheduleResponse
- PersonalDocumentData
- RefundFundsTransferNotificationContent
- RefundFundsTransferNotification
- RefundResult
- ReportAvailableNotificationContent
- ReportAvailableNotification
- ScheduledRefundsNotificationContent
- ScheduledRefundsNotification
- ShareholderContact
- SignatoryContact
- SplitAmount
- Split
- StoreDetail
- Transaction
- TransferFundsNotificationContent
- TransferFundsNotification
- UltimateParentCompanyBusinessDetails
- UltimateParentCompany
- UpdateAccountHolderResponse
- UpdateAccountResponse
- ViasAddress
- ViasName
- ViasPersonalData
- ViasPhoneNumber
- email
- description
- name
context_file: json-ld/adyen-notifications-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-notifications-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Notifications from Adyen.
layout: jsonld
name: Adyen Notifications Context
namespaces:
- prefix: adyen
  uri: https://docs.adyen.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: content
  type: string
- container: ''
  name: error
  type: string
- container: ''
  name: eventDate
  type: dateTime
- container: ''
  name: eventType
  type: string
- container: ''
  name: executingUserKey
  type: string
- container: ''
  name: live
  type: boolean
- container: ''
  name: pspReference
  type: string
- container: ''
  name: event
  type: string
- container: ''
  name: executionDate
  type: dateTime
- container: ''
  name: reason
  type: string
- container: ''
  name: accountCode
  type: string
- container: ''
  name: balanceDate
  type: string
- container: ''
  name: currentFunds
  type: string
- container: ''
  name: fundThreshold
  type: string
- container: ''
  name: merchantAccountCode
  type: string
- container: ''
  name: address
  type: string
- container: set
  name: bankAccountDetails
  type: string
- container: ''
  name: bankAggregatorDataReference
  type: string
- container: ''
  name: businessDetails
  type: string
- container: ''
  name: fullPhoneNumber
  type: string
- container: ''
  name: individualDetails
  type: string
- container: ''
  name: lastReviewDate
  type: string
- container: set
  name: legalArrangements
  type: string
- container: ''
  name: merchantCategoryCode
  type: string
- container: ''
  name: metadata
  type: reference
- container: set
  name: payoutMethods
  type: string
- container: ''
  name: principalBusinessAddress
  type: string
- container: set
  name: storeDetails
  type: string
- container: ''
  name: webAddress
  type: string
- container: ''
  name: accountHolderCode
  type: string
- container: set
  name: amounts
  type: string
- container: ''
  name: bankAccountDetail
  type: string
- container: ''
  name: estimatedArrivalDate
  type: string
- container: set
  name: invalidFields
  type: string
- container: ''
  name: merchantReference
  type: string
- container: ''
  name: originalPspReference
  type: string
- container: ''
  name: payoutAccountCountry
  type: string
- container: ''
  name: payoutAccountNumber
  type: string
- container: ''
  name: payoutBalanceAccountId
  type: string
- container: ''
  name: payoutBankName
  type: string
- container: ''
  name: payoutBranchCode
  type: string
- container: ''
  name: payoutReference
  type: integer
- container: ''
  name: payoutSpeed
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: newStatus
  type: string
- container: ''
  name: oldStatus
  type: string
- container: set
  name: events
  type: string
- container: ''
  name: payoutState
  type: string
- container: ''
  name: processingState
  type: string
- container: ''
  name: statusReason
  type: string
- container: ''
  name: store
  type: string
- container: ''
  name: storeReference
  type: string
- container: ''
  name: kycCheckStatusData
  type: string
- container: ''
  name: legalArrangementCode
  type: string
- container: ''
  name: legalArrangementEntityCode
  type: string
- container: ''
  name: payoutMethodCode
  type: string
- container: ''
  name: shareholderCode
  type: string
- container: ''
  name: signatoryCode
  type: string
- container: ''
  name: allowPayout
  type: boolean
- container: ''
  name: disableReason
  type: string
- container: ''
  name: disabled
  type: boolean
- container: ''
  name: notAllowedReason
  type: string
- container: ''
  name: payoutLimit
  type: string
- container: ''
  name: tierNumber
  type: integer
- container: ''
  name: processedFrom
  type: string
- container: ''
  name: processedTo
  type: string
- container: ''
  name: currency
  type: string
- container: ''
  name: value
  type: integer
- container: ''
  name: accountNumber
  type: string
- container: ''
  name: accountType
  type: string
- container: ''
  name: bankAccountName
  type: string
- container: ''
  name: bankAccountReference
  type: string
- container: ''
  name: bankAccountUUID
  type: string
- container: ''
  name: bankBicSwift
  type: string
- container: ''
  name: bankCity
  type: string
- container: ''
  name: bankCode
  type: string
- container: ''
  name: bankName
  type: string
- container: ''
  name: branchCode
  type: string
- container: ''
  name: checkCode
  type: string
- container: ''
  name: countryCode
  type: string
- container: ''
  name: currencyCode
  type: string
- container: ''
  name: iban
  type: string
- container: ''
  name: ownerCity
  type: string
- container: ''
  name: ownerCountryCode
  type: string
- container: ''
  name: ownerDateOfBirth
  type: string
- container: ''
  name: ownerHouseNumberOrName
  type: string
- container: ''
  name: ownerName
  type: string
- container: ''
  name: ownerNationality
  type: string
- container: ''
  name: ownerPostalCode
  type: string
- container: ''
  name: ownerState
  type: string
- container: ''
  name: ownerStreet
  type: string
- container: ''
  name: primaryAccount
  type: boolean
- container: ''
  name: taxId
  type: string
- container: ''
  name: urlForVerification
  type: string
- container: ''
  name: destinationAccountCode
  type: string
- container: ''
  name: destinationAccountHolderCode
  type: string
- container: ''
  name: sourceAccountCode
  type: string
- container: ''
  name: sourceAccountHolderCode
  type: string
- container: ''
  name: transferDate
  type: dateTime
- container: ''
  name: doingBusinessAs
  type: string
- container: ''
  name: legalBusinessName
  type: string
- container: set
  name: listedUltimateParentCompany
  type: string
- container: ''
  name: registrationNumber
  type: string
- container: set
  name: shareholders
  type: string
- container: set
  name: signatories
  type: string
- container: ''
  name: stockExchange
  type: string
- container: ''
  name: stockNumber
  type: string
- container: ''
  name: stockTicker
  type: string
- container: ''
  name: resultCode
  type: string
- container: set
  name: records
  type: string
- container: ''
  name: amount
  type: string
- container: ''
  name: accountHolderDetails
  type: string
- container: ''
  name: accountHolderStatus
  type: string
- container: ''
  name: legalEntity
  type: string
- container: ''
  name: primaryCurrency
  type: string
- container: ''
  name: verification
  type: string
- container: ''
  name: verificationProfile
  type: string
- container: ''
  name: payoutSchedule
  type: string
- container: ''
  name: debitInitiationDate
  type: string
- container: set
  name: splits
  type: string
- container: ''
  name: errorCode
  type: integer
- container: ''
  name: errorDescription
  type: string
- container: ''
  name: fieldType
  type: string
- container: ''
  name: field
  type: string
- container: ''
  name: fieldName
  type: string
- container: ''
  name: personalData
  type: string
- container: set
  name: checks
  type: string
- container: set
  name: requiredFields
  type: string
- container: ''
  name: summary
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: kycCheckCode
  type: integer
- container: ''
  name: kycCheckDescription
  type: string
- container: ''
  name: ultimateParentCompanyCode
  type: string
- container: ''
  name: accountHolder
  type: string
- container: set
  name: legalArrangementsEntities
  type: string
- container: set
  name: ultimateParentCompany
  type: string
- container: set
  name: legalArrangementEntities
  type: string
- container: ''
  name: legalArrangementReference
  type: string
- container: ''
  name: legalForm
  type: string
- container: ''
  name: taxNumber
  type: string
- container: ''
  name: legalArrangementEntityReference
  type: string
- container: set
  name: legalArrangementMembers
  type: string
- container: ''
  name: legalEntityType
  type: string
- container: ''
  name: phoneNumber
  type: string
- container: ''
  name: month
  type: integer
- container: ''
  name: year
  type: integer
- container: ''
  name: code
  type: string
- container: ''
  name: text
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: notificationResponse
  type: string
- container: ''
  name: statusCode
  type: string
- container: set
  name: errorFields
  type: string
- container: ''
  name: errorMessage
  type: string
- container: ''
  name: modificationMerchantReference
  type: string
- container: ''
  name: modificationPspReference
  type: string
- container: ''
  name: paymentMerchantReference
  type: string
- container: ''
  name: paymentPspReference
  type: string
- container: ''
  name: merchantAccount
  type: string
- container: ''
  name: payoutMethodReference
  type: string
- container: ''
  name: recurringDetailReference
  type: string
- container: ''
  name: shopperReference
  type: string
- container: ''
  name: nextScheduledPayout
  type: dateTime
- container: ''
  name: schedule
  type: string
- container: ''
  name: expirationDate
  type: string
- container: ''
  name: issuerCountry
  type: string
- container: ''
  name: issuerState
  type: string
- container: ''
  name: number
  type: string
- container: ''
  name: originalReference
  type: string
- container: ''
  name: originalTransaction
  type: string
- container: ''
  name: response
  type: string
- container: ''
  name: remoteAccessUrl
  type: string
- container: ''
  name: success
  type: boolean
- container: ''
  name: lastPayout
  type: string
- container: set
  name: refundResults
  type: string
- container: ''
  name: jobTitle
  type: string
- container: ''
  name: shareholderReference
  type: string
- container: ''
  name: shareholderType
  type: string
- container: ''
  name: signatoryReference
  type: string
- container: ''
  name: account
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: logo
  type: string
- container: ''
  name: merchantHouseNumber
  type: string
- container: ''
  name: shopperInteraction
  type: string
- container: ''
  name: splitConfigurationUUID
  type: string
- container: ''
  name: storeName
  type: string
- container: ''
  name: virtualAccount
  type: string
- container: ''
  name: captureMerchantReference
  type: string
- container: ''
  name: capturePspReference
  type: string
- container: ''
  name: creationDate
  type: dateTime
- container: ''
  name: disputePspReference
  type: string
- container: ''
  name: disputeReasonCode
  type: string
- container: ''
  name: payoutPspReference
  type: string
- container: ''
  name: transactionStatus
  type: string
- container: ''
  name: transferCode
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: houseNumberOrName
  type: string
- container: ''
  name: postalCode
  type: string
- container: ''
  name: stateOrProvince
  type: string
- container: ''
  name: street
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: gender
  type: string
- container: ''
  name: infix
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: dateOfBirth
  type: string
- container: set
  name: documentData
  type: string
- container: ''
  name: nationality
  type: string
- container: ''
  name: phoneCountryCode
  type: string
- container: ''
  name: phoneType
  type: string
property_count: 209
provider_name: Adyen
provider_slug: adyen
slug: adyen-notifications-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
