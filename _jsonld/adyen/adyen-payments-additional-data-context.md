---
class_count: 15
classes:
- AdditionalDataAirline
- AdditionalDataCarRental
- AdditionalDataCommon
- AdditionalDataLevel23
- AdditionalDataLodging
- AdditionalDataModifications
- AdditionalDataOpenInvoice
- AdditionalDataOpi
- AdditionalDataRatepay
- AdditionalDataRetry
- AdditionalDataRisk
- AdditionalDataRiskStandalone
- AdditionalDataSubMerchant
- AdditionalDataTemporaryServices
- AdditionalDataWallets
context_file: json-ld/adyen-payments-additional-data-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-payments-additional-data-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Payments Additional Data from Adyen.
layout: jsonld
name: Adyen Payments Additional Data Context
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
  name: airline.agencyInvoiceNumber
  type: string
- container: ''
  name: airline.agencyPlanName
  type: string
- container: ''
  name: airline.airlineCode
  type: string
- container: ''
  name: airline.airlineDesignatorCode
  type: string
- container: ''
  name: airline.boardingFee
  type: string
- container: ''
  name: airline.computerizedReservationSystem
  type: string
- container: ''
  name: airline.customerReferenceNumber
  type: string
- container: ''
  name: airline.documentType
  type: string
- container: ''
  name: airline.flightDate
  type: string
- container: ''
  name: airline.leg.carrierCode
  type: string
- container: ''
  name: airline.leg.classOfTravel
  type: string
- container: ''
  name: airline.leg.dateOfTravel
  type: string
- container: ''
  name: airline.leg.departAirport
  type: string
- container: ''
  name: airline.leg.departTax
  type: string
- container: ''
  name: airline.leg.destinationCode
  type: string
- container: ''
  name: airline.leg.fareBaseCode
  type: string
- container: ''
  name: airline.leg.flightNumber
  type: string
- container: ''
  name: airline.leg.stopOverCode
  type: string
- container: ''
  name: airline.passenger.dateOfBirth
  type: string
- container: ''
  name: airline.passenger.firstName
  type: string
- container: ''
  name: airline.passenger.lastName
  type: string
- container: ''
  name: airline.passenger.telephoneNumber
  type: string
- container: ''
  name: airline.passenger.travellerType
  type: string
- container: ''
  name: airline.passengerName
  type: string
- container: ''
  name: airline.ticketIssueAddress
  type: string
- container: ''
  name: airline.ticketNumber
  type: string
- container: ''
  name: airline.travelAgencyCode
  type: string
- container: ''
  name: airline.travelAgencyName
  type: string
- container: ''
  name: carRental.checkOutDate
  type: string
- container: ''
  name: carRental.customerServiceTollFreeNumber
  type: string
- container: ''
  name: carRental.daysRented
  type: string
- container: ''
  name: carRental.fuelCharges
  type: string
- container: ''
  name: carRental.insuranceCharges
  type: string
- container: ''
  name: carRental.locationCity
  type: string
- container: ''
  name: carRental.locationCountry
  type: string
- container: ''
  name: carRental.locationStateProvince
  type: string
- container: ''
  name: carRental.noShowIndicator
  type: string
- container: ''
  name: carRental.oneWayDropOffCharges
  type: string
- container: ''
  name: carRental.rate
  type: string
- container: ''
  name: carRental.rateIndicator
  type: string
- container: ''
  name: carRental.rentalAgreementNumber
  type: string
- container: ''
  name: carRental.rentalClassId
  type: string
- container: ''
  name: carRental.renterName
  type: string
- container: ''
  name: carRental.returnCity
  type: string
- container: ''
  name: carRental.returnCountry
  type: string
- container: ''
  name: carRental.returnDate
  type: string
- container: ''
  name: carRental.returnLocationId
  type: string
- container: ''
  name: carRental.returnStateProvince
  type: string
- container: ''
  name: carRental.taxExemptIndicator
  type: string
- container: ''
  name: travelEntertainmentAuthData.duration
  type: string
- container: ''
  name: travelEntertainmentAuthData.market
  type: string
- container: ''
  name: RequestedTestErrorResponseCode
  type: string
- container: ''
  name: allowPartialAuth
  type: string
- container: ''
  name: authorisationType
  type: string
- container: ''
  name: customRoutingFlag
  type: string
- container: ''
  name: industryUsage
  type: string
- container: ''
  name: manualCapture
  type: string
- container: ''
  name: networkTxReference
  type: string
- container: ''
  name: overwriteBrand
  type: string
- container: ''
  name: subMerchantCity
  type: string
- container: ''
  name: subMerchantCountry
  type: string
- container: ''
  name: subMerchantID
  type: string
- container: ''
  name: subMerchantName
  type: string
- container: ''
  name: subMerchantPostalCode
  type: string
- container: ''
  name: subMerchantState
  type: string
- container: ''
  name: subMerchantStreet
  type: string
- container: ''
  name: subMerchantTaxId
  type: string
- container: ''
  name: enhancedSchemeData.customerReference
  type: string
- container: ''
  name: enhancedSchemeData.destinationCountryCode
  type: string
- container: ''
  name: enhancedSchemeData.destinationPostalCode
  type: string
- container: ''
  name: enhancedSchemeData.destinationStateProvinceCode
  type: string
- container: ''
  name: enhancedSchemeData.dutyAmount
  type: string
- container: ''
  name: enhancedSchemeData.freightAmount
  type: string
- container: ''
  name: enhancedSchemeData.itemDetailLine[itemNr].commodityCode
  type: string
- container: ''
  name: enhancedSchemeData.itemDetailLine[itemNr].description
  type: string
- container: ''
  name: enhancedSchemeData.itemDetailLine[itemNr].discountAmount
  type: string
- container: ''
  name: enhancedSchemeData.itemDetailLine[itemNr].productCode
  type: string
- container: ''
  name: enhancedSchemeData.itemDetailLine[itemNr].quantity
  type: string
- container: ''
  name: enhancedSchemeData.itemDetailLine[itemNr].totalAmount
  type: string
- container: ''
  name: enhancedSchemeData.itemDetailLine[itemNr].unitOfMeasure
  type: string
- container: ''
  name: enhancedSchemeData.itemDetailLine[itemNr].unitPrice
  type: string
- container: ''
  name: enhancedSchemeData.orderDate
  type: string
- container: ''
  name: enhancedSchemeData.shipFromPostalCode
  type: string
- container: ''
  name: enhancedSchemeData.totalTaxAmount
  type: string
- container: ''
  name: lodging.checkInDate
  type: string
- container: ''
  name: lodging.checkOutDate
  type: string
- container: ''
  name: lodging.customerServiceTollFreeNumber
  type: string
- container: ''
  name: lodging.fireSafetyActIndicator
  type: string
- container: ''
  name: lodging.folioCashAdvances
  type: string
- container: ''
  name: lodging.folioNumber
  type: string
- container: ''
  name: lodging.foodBeverageCharges
  type: string
- container: ''
  name: lodging.noShowIndicator
  type: string
- container: ''
  name: lodging.prepaidExpenses
  type: string
- container: ''
  name: lodging.propertyPhoneNumber
  type: string
- container: ''
  name: lodging.room1.numberOfNights
  type: string
- container: ''
  name: lodging.room1.rate
  type: string
- container: ''
  name: lodging.totalRoomTax
  type: string
- container: ''
  name: lodging.totalTax
  type: string
- container: ''
  name: installmentPaymentData.selectedInstallmentOption
  type: string
- container: ''
  name: openinvoicedata.merchantData
  type: string
- container: ''
  name: openinvoicedata.numberOfLines
  type: string
- container: ''
  name: openinvoicedata.recipientFirstName
  type: string
- container: ''
  name: openinvoicedata.recipientLastName
  type: string
- container: ''
  name: openinvoicedataLine[itemNr].currencyCode
  type: string
- container: ''
  name: openinvoicedataLine[itemNr].description
  type: string
- container: ''
  name: openinvoicedataLine[itemNr].itemAmount
  type: string
- container: ''
  name: openinvoicedataLine[itemNr].itemId
  type: string
- container: ''
  name: openinvoicedataLine[itemNr].itemVatAmount
  type: string
- container: ''
  name: openinvoicedataLine[itemNr].itemVatPercentage
  type: string
- container: ''
  name: openinvoicedataLine[itemNr].numberOfItems
  type: string
- container: ''
  name: openinvoicedataLine[itemNr].returnShippingCompany
  type: string
- container: ''
  name: openinvoicedataLine[itemNr].returnTrackingNumber
  type: string
- container: ''
  name: openinvoicedataLine[itemNr].returnTrackingUri
  type: string
- container: ''
  name: openinvoicedataLine[itemNr].shippingCompany
  type: string
- container: ''
  name: openinvoicedataLine[itemNr].shippingMethod
  type: string
- container: ''
  name: openinvoicedataLine[itemNr].trackingNumber
  type: string
- container: ''
  name: openinvoicedataLine[itemNr].trackingUri
  type: string
- container: ''
  name: opi.includeTransToken
  type: string
- container: ''
  name: ratepay.installmentAmount
  type: string
- container: ''
  name: ratepay.interestRate
  type: string
- container: ''
  name: ratepay.lastInstallmentAmount
  type: string
- container: ''
  name: ratepay.paymentFirstday
  type: string
- container: ''
  name: ratepaydata.deliveryDate
  type: string
- container: ''
  name: ratepaydata.dueDate
  type: string
- container: ''
  name: ratepaydata.invoiceDate
  type: string
- container: ''
  name: ratepaydata.invoiceId
  type: string
- container: ''
  name: retry.chainAttemptNumber
  type: string
- container: ''
  name: retry.orderAttemptNumber
  type: string
- container: ''
  name: retry.skipRetry
  type: string
- container: ''
  name: riskdata.[customFieldName]
  type: string
- container: ''
  name: riskdata.basket.item[itemNr].amountPerItem
  type: string
- container: ''
  name: riskdata.basket.item[itemNr].brand
  type: string
- container: ''
  name: riskdata.basket.item[itemNr].category
  type: string
- container: ''
  name: riskdata.basket.item[itemNr].color
  type: string
- container: ''
  name: riskdata.basket.item[itemNr].currency
  type: string
- container: ''
  name: riskdata.basket.item[itemNr].itemID
  type: string
- container: ''
  name: riskdata.basket.item[itemNr].manufacturer
  type: string
- container: ''
  name: riskdata.basket.item[itemNr].productTitle
  type: string
- container: ''
  name: riskdata.basket.item[itemNr].quantity
  type: string
- container: ''
  name: riskdata.basket.item[itemNr].receiverEmail
  type: string
- container: ''
  name: riskdata.basket.item[itemNr].size
  type: string
- container: ''
  name: riskdata.basket.item[itemNr].sku
  type: string
- container: ''
  name: riskdata.basket.item[itemNr].upc
  type: string
- container: ''
  name: riskdata.promotions.promotion[itemNr].promotionCode
  type: string
- container: ''
  name: riskdata.promotions.promotion[itemNr].promotionDiscountAmount
  type: string
- container: ''
  name: riskdata.promotions.promotion[itemNr].promotionDiscountCurrency
  type: string
- container: ''
  name: riskdata.promotions.promotion[itemNr].promotionDiscountPercentage
  type: string
- container: ''
  name: riskdata.promotions.promotion[itemNr].promotionName
  type: string
- container: ''
  name: riskdata.riskProfileReference
  type: string
- container: ''
  name: riskdata.skipRisk
  type: string
- container: ''
  name: PayPal.CountryCode
  type: string
- container: ''
  name: PayPal.EmailId
  type: string
- container: ''
  name: PayPal.FirstName
  type: string
- container: ''
  name: PayPal.LastName
  type: string
- container: ''
  name: PayPal.PayerId
  type: string
- container: ''
  name: PayPal.Phone
  type: string
- container: ''
  name: PayPal.ProtectionEligibility
  type: string
- container: ''
  name: PayPal.TransactionId
  type: string
- container: ''
  name: avsResultRaw
  type: string
- container: ''
  name: bin
  type: string
- container: ''
  name: cvcResultRaw
  type: string
- container: ''
  name: riskToken
  type: string
- container: ''
  name: threeDAuthenticated
  type: string
- container: ''
  name: threeDOffered
  type: string
- container: ''
  name: tokenDataType
  type: string
- container: ''
  name: subMerchant.numberOfSubSellers
  type: string
- container: ''
  name: subMerchant.subSeller[subSellerNr].city
  type: string
- container: ''
  name: subMerchant.subSeller[subSellerNr].country
  type: string
- container: ''
  name: subMerchant.subSeller[subSellerNr].id
  type: string
- container: ''
  name: subMerchant.subSeller[subSellerNr].mcc
  type: string
- container: ''
  name: subMerchant.subSeller[subSellerNr].name
  type: string
- container: ''
  name: subMerchant.subSeller[subSellerNr].postalCode
  type: string
- container: ''
  name: subMerchant.subSeller[subSellerNr].state
  type: string
- container: ''
  name: subMerchant.subSeller[subSellerNr].street
  type: string
- container: ''
  name: subMerchant.subSeller[subSellerNr].taxId
  type: string
- container: ''
  name: enhancedSchemeData.employeeName
  type: string
- container: ''
  name: enhancedSchemeData.jobDescription
  type: string
- container: ''
  name: enhancedSchemeData.regularHoursRate
  type: string
- container: ''
  name: enhancedSchemeData.regularHoursWorked
  type: string
- container: ''
  name: enhancedSchemeData.requestName
  type: string
- container: ''
  name: enhancedSchemeData.tempStartDate
  type: string
- container: ''
  name: enhancedSchemeData.tempWeekEnding
  type: string
- container: ''
  name: androidpay.token
  type: string
- container: ''
  name: masterpass.transactionId
  type: string
- container: ''
  name: payment.token
  type: string
- container: ''
  name: paywithgoogle.token
  type: string
- container: ''
  name: samsungpay.token
  type: string
- container: ''
  name: visacheckout.callId
  type: string
property_count: 188
provider_name: Adyen
provider_slug: adyen
slug: adyen-payments-additional-data-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
