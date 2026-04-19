---
class_count: 53
classes:
- Order
- OrderList
- OrderItem
- OrderItemList
- CatalogItem
- CatalogItemList
- ListingsItem
- ListingsItemPutRequest
- ListingsItemPatchRequest
- ListingsItemSubmissionResponse
- InventorySummaries
- Report
- ReportList
- ReportDocument
- url
- CreateReportSpecification
- CreateReportResponse
- TransactionList
- Money
- Pagination
- ErrorList
- Profile
- Campaign
- name
- CreateCampaignRequest
- UpdateCampaignRequest
- CampaignResponse
- description
- AdGroup
- CreateAdGroupRequest
- AdGroupResponse
- Keyword
- CreateKeywordRequest
- KeywordResponse
- Target
- CreateTargetRequest
- TargetResponse
- ReportRequest
- ReportRequestResponse
- ReportStatus
- Price
- MerchantMetadata
- StatusDetails
- Buyer
- Address
- CheckoutSession
- CreateCheckoutSessionRequest
- UpdateCheckoutSessionRequest
- Charge
- CreateChargeRequest
- ChargePermission
- Refund
- CreateRefundRequest
context_file: json-ld/amazon-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon/refs/heads/main/json-ld/amazon-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon from Amazon.
layout: jsonld
name: Amazon Context
namespaces:
- prefix: amz
  uri: https://amazon.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: AmazonOrderId
  type: string
- container: ''
  name: PurchaseDate
  type: string
- container: ''
  name: LastUpdateDate
  type: string
- container: ''
  name: OrderStatus
  type: string
- container: ''
  name: FulfillmentChannel
  type: string
- container: ''
  name: OrderTotal
  type: string
- container: ''
  name: NumberOfItemsShipped
  type: string
- container: ''
  name: NumberOfItemsUnshipped
  type: string
- container: ''
  name: ShipServiceLevel
  type: string
- container: ''
  name: MarketplaceId
  type: string
- container: ''
  name: payload
  type: string
- container: ''
  name: ASIN
  type: string
- container: ''
  name: OrderItemId
  type: string
- container: ''
  name: SellerSKU
  type: string
- container: ''
  name: Title
  type: string
- container: ''
  name: QuantityOrdered
  type: string
- container: ''
  name: QuantityShipped
  type: string
- container: ''
  name: ItemPrice
  type: string
- container: ''
  name: asin
  type: string
- container: ''
  name: attributes
  type: string
- container: set
  name: images
  type: string
- container: set
  name: salesRanks
  type: string
- container: ''
  name: numberOfResults
  type: string
- container: ''
  name: pagination
  type: string
- container: set
  name: items
  type: string
- container: ''
  name: sku
  type: string
- container: set
  name: summaries
  type: string
- container: set
  name: issues
  type: string
- container: set
  name: offers
  type: string
- container: ''
  name: productType
  type: string
- container: set
  name: patches
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: submissionId
  type: string
- container: set
  name: inventorySummaries
  type: string
- container: ''
  name: reportId
  type: string
- container: ''
  name: reportType
  type: string
- container: ''
  name: processingStatus
  type: string
- container: ''
  name: reportDocumentId
  type: string
- container: ''
  name: createdTime
  type: string
- container: set
  name: reports
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: dataStartTime
  type: string
- container: ''
  name: dataEndTime
  type: string
- container: set
  name: marketplaceIds
  type: string
- container: set
  name: transactions
  type: string
- container: ''
  name: CurrencyCode
  type: string
- container: ''
  name: Amount
  type: string
- container: ''
  name: previousToken
  type: string
- container: set
  name: errors
  type: string
- container: ''
  name: profileId
  type: string
- container: ''
  name: countryCode
  type: string
- container: ''
  name: currencyCode
  type: string
- container: ''
  name: accountInfo
  type: string
- container: ''
  name: campaignId
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: dailyBudget
  type: string
- container: ''
  name: startDate
  type: string
- container: ''
  name: endDate
  type: string
- container: ''
  name: targetingType
  type: string
- container: ''
  name: premiumBidAdjustment
  type: string
- container: ''
  name: code
  type: string
- container: ''
  name: adGroupId
  type: string
- container: ''
  name: defaultBid
  type: string
- container: ''
  name: keywordId
  type: string
- container: ''
  name: keywordText
  type: string
- container: ''
  name: matchType
  type: string
- container: ''
  name: bid
  type: string
- container: ''
  name: targetId
  type: string
- container: ''
  name: expressionType
  type: string
- container: set
  name: expression
  type: string
- container: ''
  name: reportDate
  type: string
- container: ''
  name: metrics
  type: string
- container: ''
  name: segment
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: fileSize
  type: string
- container: ''
  name: amount
  type: string
- container: ''
  name: merchantReferenceId
  type: string
- container: ''
  name: merchantStoreName
  type: string
- container: ''
  name: noteToBuyer
  type: string
- container: ''
  name: reasonCode
  type: string
- container: ''
  name: reasonDescription
  type: string
- container: ''
  name: buyerId
  type: string
- container: ''
  name: email
  type: string
- container: ''
  name: addressLine1
  type: string
- container: ''
  name: addressLine2
  type: string
- container: ''
  name: addressLine3
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: stateOrRegion
  type: string
- container: ''
  name: postalCode
  type: string
- container: ''
  name: phoneNumber
  type: string
- container: ''
  name: checkoutSessionId
  type: string
- container: ''
  name: statusDetails
  type: string
- container: ''
  name: buyer
  type: string
- container: ''
  name: shippingAddress
  type: string
- container: ''
  name: billingAddress
  type: string
- container: ''
  name: paymentDetails
  type: string
- container: ''
  name: merchantMetadata
  type: string
- container: ''
  name: chargePermissionId
  type: string
- container: ''
  name: chargeId
  type: string
- container: ''
  name: creationTimestamp
  type: string
- container: ''
  name: expirationTimestamp
  type: string
- container: ''
  name: webCheckoutDetails
  type: string
- container: ''
  name: storeId
  type: string
- container: ''
  name: chargePermissionType
  type: string
- container: ''
  name: chargeAmount
  type: string
- container: ''
  name: captureAmount
  type: string
- container: ''
  name: refundedAmount
  type: string
- container: ''
  name: softDescriptor
  type: string
- container: ''
  name: captureNow
  type: string
- container: ''
  name: canHandlePendingAuthorization
  type: string
- container: ''
  name: limits
  type: string
- container: ''
  name: refundId
  type: string
- container: ''
  name: refundAmount
  type: string
property_count: 113
provider_name: Amazon
provider_slug: amazon
slug: amazon-context
tags:
- Amazon
- Advertising
- Alexa
- E-Commerce
- Marketplace
- Payments
- Voice
- JSON-LD
- Linked Data
- Semantic Web
---
