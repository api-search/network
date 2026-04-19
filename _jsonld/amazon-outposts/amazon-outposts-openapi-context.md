---
class_count: 118
classes:
- AccessDeniedException
- Arn
- AssetInfo
- AssetListDefinition
- AssetState
- AvailabilityZoneIdList
- AvailabilityZoneList
- CIDR
- CIDRList
- CancelOrderInput
- CancelOrderOutput
- CatalogItemClass
- CatalogItemClassList
- CatalogItemListDefinition
- CatalogItemPowerKva
- CatalogItemStatus
- CatalogItemWeightLbs
- CityList
- ComputeAssetState
- ConflictException
- CountryCodeList
- CreateOrderInput
- CreateOrderOutput
- CreateOutpostInput
- CreateOutpostOutput
- CreateSiteInput
- CreateSiteOutput
- DeleteOutpostInput
- DeleteOutpostOutput
- DeleteSiteInput
- DeleteSiteOutput
- EC2Capacity
- EC2CapacityListDefinition
- EC2FamilyList
- GetCatalogItemInput
- GetCatalogItemOutput
- GetConnectionRequest
- GetConnectionResponse
- GetOrderInput
- GetOrderOutput
- GetOutpostInput
- GetOutpostInstanceTypesInput
- GetOutpostInstanceTypesOutput
- GetOutpostOutput
- GetSiteAddressInput
- GetSiteAddressOutput
- GetSiteInput
- GetSiteOutput
- HostIdList
- ISO8601Timestamp
- InstanceTypeItem
- InstanceTypeListDefinition
- InternalServerException
- LifeCycleStatusList
- LineItem
- LineItemAssetInformation
- LineItemAssetInformationList
- LineItemListDefinition
- LineItemQuantity
- LineItemRequest
- LineItemRequestListDefinition
- LineItemStatus
- LineItemStatusCounts
- ListAssetsInput
- ListAssetsOutput
- ListCatalogItemsInput
- ListCatalogItemsOutput
- ListOrdersInput
- ListOrdersOutput
- ListOutpostsInput
- ListOutpostsOutput
- ListSitesInput
- ListSitesOutput
- ListTagsForResourceRequest
- ListTagsForResourceResponse
- MacAddress
- MaxResults1000
- NotFoundException
- OrderStatus
- OrderSummary
- OrderSummaryListDefinition
- OutpostDescription
- OutpostIdOnly
- OutpostName
- ServiceQuotaExceededException
- SiteDescription
- SiteName
- SiteNotes
- SkuCode
- StartConnectionRequest
- StartConnectionResponse
- StateOrRegionList
- StatusList
- SupportedStorageEnum
- SupportedStorageList
- SupportedUplinkGbpsListDefinition
- TagKey
- TagKeyList
- TagMap
- TagResourceRequest
- TagResourceResponse
- TagValue
- Token
- TrackingId
- UntagResourceRequest
- UntagResourceResponse
- UpdateOutpostInput
- UpdateOutpostOutput
- UpdateSiteAddressInput
- UpdateSiteAddressOutput
- UpdateSiteInput
- UpdateSiteOutput
- UpdateSiteRackPhysicalPropertiesInput
- UpdateSiteRackPhysicalPropertiesOutput
- ValidationException
- WireGuardPublicKey
- outpostListDefinition
- siteListDefinition
context_file: json-ld/amazon-outposts-openapi-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-outposts/refs/heads/main/json-ld/amazon-outposts-openapi-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Outposts Openapi from Amazon Outposts.
layout: jsonld
name: Amazon Outposts Openapi Context
namespaces:
- prefix: outposts
  uri: https://outposts.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: AccountId
  type: string
- container: ''
  name: Address
  type: string
- container: ''
  name: AddressLine1
  type: string
- container: ''
  name: AddressLine2
  type: string
- container: ''
  name: AddressLine3
  type: string
- container: ''
  name: AddressType
  type: string
- container: ''
  name: AssetId
  type: string
- container: ''
  name: AssetLocation
  type: string
- container: ''
  name: AssetType
  type: string
- container: ''
  name: AvailabilityZone
  type: string
- container: ''
  name: AvailabilityZoneId
  type: string
- container: ''
  name: CatalogItem
  type: string
- container: ''
  name: City
  type: string
- container: ''
  name: ComputeAttributes
  type: string
- container: ''
  name: ConnectionDetails
  type: string
- container: ''
  name: ConnectionId
  type: string
- container: ''
  name: ContactName
  type: string
- container: ''
  name: ContactPhoneNumber
  type: string
- container: ''
  name: CountryCode
  type: string
- container: ''
  name: DeviceSerialNumber
  type: string
- container: ''
  name: DistrictOrCounty
  type: string
- container: ''
  name: Family
  type: string
- container: ''
  name: FiberOpticCableType
  type: string
- container: ''
  name: HostId
  type: string
- container: ''
  name: InstanceType
  type: string
- container: ''
  name: LifeCycleStatus
  type: string
- container: ''
  name: LineItemId
  type: string
- container: ''
  name: MacAddressList
  type: string
- container: ''
  name: MaxSize
  type: string
- container: ''
  name: MaximumSupportedWeightLbs
  type: string
- container: ''
  name: Municipality
  type: string
- container: ''
  name: NetworkInterfaceDeviceIndex
  type: string
- container: ''
  name: OpticalStandard
  type: string
- container: ''
  name: Order
  type: string
- container: ''
  name: OrderId
  type: string
- container: ''
  name: OrderType
  type: string
- container: ''
  name: Outpost
  type: string
- container: ''
  name: OutpostArn
  type: string
- container: ''
  name: OutpostId
  type: string
- container: ''
  name: OutpostIdentifier
  type: string
- container: ''
  name: OwnerId
  type: string
- container: ''
  name: PaymentOption
  type: string
- container: ''
  name: PaymentTerm
  type: string
- container: ''
  name: PostalCode
  type: string
- container: ''
  name: PowerConnector
  type: string
- container: ''
  name: PowerDrawKva
  type: string
- container: ''
  name: PowerFeedDrop
  type: string
- container: ''
  name: PowerPhase
  type: string
- container: ''
  name: Quantity
  type: string
- container: ''
  name: RackElevation
  type: string
- container: ''
  name: RackId
  type: string
- container: ''
  name: RackPhysicalProperties
  type: string
- container: ''
  name: ServerEndpoint
  type: string
- container: ''
  name: ShipmentCarrier
  type: string
- container: ''
  name: ShipmentInformation
  type: string
- container: ''
  name: Site
  type: string
- container: ''
  name: SiteArn
  type: string
- container: ''
  name: SiteId
  type: string
- container: ''
  name: StateOrRegion
  type: string
- container: ''
  name: SupportedHardwareType
  type: string
- container: ''
  name: SupportedUplinkGbps
  type: string
- container: ''
  name: UnderlayIpAddress
  type: string
- container: ''
  name: UplinkCount
  type: string
- container: ''
  name: UplinkGbps
  type: string
- container: ''
  name: AllowedIps
  type: string
- container: ''
  name: AssetInformationList
  type: string
- container: ''
  name: Assets
  type: string
- container: ''
  name: CatalogItemId
  type: string
- container: ''
  name: CatalogItems
  type: string
- container: ''
  name: ClientPublicKey
  type: string
- container: ''
  name: ClientTunnelAddress
  type: string
- container: ''
  name: Description
  type: string
- container: ''
  name: EC2Capacities
  type: string
- container: ''
  name: InstanceTypes
  type: string
- container: ''
  name: ItemStatus
  type: string
- container: ''
  name: LineItemCountsByStatus
  type: string
- container: ''
  name: LineItems
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: Notes
  type: string
- container: ''
  name: OperatingAddress
  type: string
- container: ''
  name: OperatingAddressCity
  type: string
- container: ''
  name: OperatingAddressCountryCode
  type: string
- container: ''
  name: OperatingAddressStateOrRegion
  type: string
- container: ''
  name: OrderFulfilledDate
  type: string
- container: ''
  name: OrderSubmissionDate
  type: string
- container: ''
  name: Orders
  type: string
- container: ''
  name: Outposts
  type: string
- container: ''
  name: PowerKva
  type: string
- container: ''
  name: PreviousLineItemId
  type: string
- container: ''
  name: PreviousOrderId
  type: string
- container: ''
  name: ServerPublicKey
  type: string
- container: ''
  name: ServerTunnelAddress
  type: string
- container: ''
  name: ShipmentTrackingNumber
  type: string
- container: ''
  name: ShippingAddress
  type: string
- container: ''
  name: Sites
  type: string
- container: ''
  name: State
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: SupportedStorage
  type: string
- container: ''
  name: Tags
  type: string
- container: ''
  name: WeightLbs
  type: string
property_count: 101
provider_name: Amazon Outposts
provider_slug: amazon-outposts
slug: amazon-outposts-openapi-context
tags:
- AWS
- Edge Computing
- Hybrid Cloud
- Infrastructure
- On-Premises
- JSON-LD
- Linked Data
- Semantic Web
---
