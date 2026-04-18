---
class_count: 66
classes:
- ChangePasswordRequest
- ContactInfo
- CreateManagedTenantRequest
- CreateMsspRequest
- CreatePolicyGroupResponse
- CreateTenantGroupRequest
- FormLoginRequest
- FormLoginResponse
- JwkResponse
- JwksResponse
- LicenseInfo
- LicensePoolInfo
- ManagedTenantDetailedResponse
- ManagedTenantLicenseResponse
- ManagedTenantResponse
- ManagedTenantsResponse
- ModuleInfo
- ModuleInfoRequest
- MsspLicenseInfoResponse
- MsspLicensePoolRequest
- MsspLicensePoolResponse
- MsspLicensePoolsResponse
- MsspLicenseUsageRequestObject
- MsspLicenseUsageResponse
- MsspListUserResponse
- MsspResponse
- MsspUserRequest
- MsspUserResponse
- OperationAckRequest
- OperationResponse
- OperationsResponse
- PolicyGroupInfo
- PolicyGroupListResponse
- PolicyGroupRequest
- PolicyGroupResponse
- PolicyGroupsListResponse
- RecurString
- RelativeTimeDuration
- RelativeTimeRangeConfig
- ScheduleTaskRequest
- SeamlessLoginResponse
- StackMappingPlanTypesListResponse
- StackMappingResponse
- Task
- TenantChangeResponse
- TenantGroupLicenseInfo
- TenantGroupMappingDetails
- TenantGroupPolicyGroupMapRequest
- TenantGroupPolicyGroupMapping
- TenantGroupPolicyGroupMappingResponse
- TenantGroupPolicyGroupMappingsResponse
- TenantGroupResponse
- TenantGroupsResponse
- TenantIds
- TenantLicenseUsage
- TenantUpdate
- TimeRangeConfigObject
- ToNowTimeRangeConfig
- TokenRefreshResponse
- UpdateManagedTenantRequest
- UpdateMsspRequest
- UpdateTenantGroupRequest
- V1Response
- ValidateTokenRequest
- ValidateTokenResponse
- timeRange
context_file: json-ld/palo-alto-prisma-cloud-mssp-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-prisma-cloud-mssp-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Prisma Cloud Mssp Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Prisma Cloud Mssp Api Context
namespaces:
- prefix: pan
  uri: https://pan.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: addLicensePool
  type: reference
- container: ''
  name: additionalData
  type: reference
- container: ''
  name: alg
  type: string
- container: ''
  name: allocatedCredits
  type: integer
- container: ''
  name: amount
  type: integer
- container: ''
  name: apiHost
  type: string
- container: ''
  name: avgConsumption
  type: integer
- container: ''
  name: balanceCredit
  type: integer
- container: ''
  name: baseApiUrl
  type: string
- container: ''
  name: billingType
  type: string
- container: ''
  name: cancel
  type: boolean
- container: ''
  name: companyName
  type: string
- container: ''
  name: contactInfo
  type: reference
- container: ''
  name: createdAt
  type: integer
- container: ''
  name: createdBy
  type: string
- container: ''
  name: createdOn
  type: integer
- container: ''
  name: credits
  type: integer
- container: ''
  name: creditsAllocated
  type: integer
- container: ''
  name: creditsPurchased
  type: integer
- container: ''
  name: customerName
  type: string
- container: ''
  name: customerSupportId
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: e
  type: string
- container: ''
  name: email
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: endDate
  type: integer
- container: ''
  name: endTime
  type: integer
- container: ''
  name: errorMessage
  type: string
- container: ''
  name: erroredBy
  type: string
- container: ''
  name: expiringOn
  type: integer
- container: ''
  name: externalTenantId
  type: string
- container: ''
  name: featureName
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: groupName
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: isRetryable
  type: boolean
- container: ''
  name: isSynthetic
  type: boolean
- container: set
  name: keyOps
  type: string
- container: set
  name: keys
  type: reference
- container: ''
  name: kid
  type: string
- container: ''
  name: kty
  type: string
- container: ''
  name: lastModifiedAt
  type: integer
- container: ''
  name: lastModifiedBy
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: lastUpdated
  type: integer
- container: ''
  name: licenseInfo
  type: reference
- container: ''
  name: licensePool
  type: reference
- container: ''
  name: licensePoolId
  type: string
- container: ''
  name: licensePoolName
  type: string
- container: ''
  name: location
  type: string
- container: set
  name: mappings
  type: reference
- container: ''
  name: matureTime
  type: integer
- container: ''
  name: message
  type: string
- container: set
  name: modules
  type: reference
- container: ''
  name: msspId
  type: string
- container: set
  name: msspLicensePoolInfos
  type: reference
- container: ''
  name: n
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: nextPageToken
  type: string
- container: ''
  name: numOfTenant
  type: integer
- container: ''
  name: operationDescription
  type: string
- container: ''
  name: operationName
  type: string
- container: ''
  name: operationType
  type: string
- container: ''
  name: password
  type: string
- container: ''
  name: planType
  type: string
- container: set
  name: planTypes
  type: string
- container: set
  name: policies
  type: string
- container: ''
  name: policyCount
  type: integer
- container: ''
  name: policyGroupId
  type: string
- container: set
  name: policyGroupIds
  type: string
- container: set
  name: policyGroups
  type: reference
- container: ''
  name: poolName
  type: string
- container: ''
  name: prismaId
  type: string
- container: set
  name: prismaIds
  type: integer
- container: ''
  name: properties
  type: reference
- container: ''
  name: recur
  type: reference
- container: ''
  name: recurString
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: requestId
  type: string
- container: ''
  name: resetToken
  type: string
- container: ''
  name: retriedBy
  type: string
- container: ''
  name: retryOf
  type: string
- container: ''
  name: scheduledTime
  type: integer
- container: ''
  name: serialNumber
  type: string
- container: ''
  name: stack
  type: string
- container: ''
  name: stackBaseUrl
  type: string
- container: set
  name: stackMappings
  type: reference
- container: ''
  name: stackName
  type: string
- container: ''
  name: startDate
  type: integer
- container: ''
  name: startTime
  type: integer
- container: ''
  name: startedAt
  type: integer
- container: ''
  name: startedBy
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: submitTime
  type: integer
- container: ''
  name: tenantChangeId
  type: string
- container: set
  name: tenantChanges
  type: reference
- container: ''
  name: tenantCount
  type: integer
- container: ''
  name: tenantGroupCount
  type: integer
- container: ''
  name: tenantGroupId
  type: string
- container: set
  name: tenantGroupLicenseInfos
  type: reference
- container: ''
  name: tenantGroupName
  type: string
- container: set
  name: tenantGroups
  type: reference
- container: set
  name: tenantIds
  type: string
- container: ''
  name: tenantLicense
  type: reference
- container: ''
  name: tenantLicenseId
  type: string
- container: set
  name: tenantLicenses
  type: reference
- container: ''
  name: tenantName
  type: string
- container: ''
  name: tenantPrismaId
  type: string
- container: ''
  name: tenantUpdate
  type: reference
- container: set
  name: tenants
  type: reference
- container: ''
  name: timeUnit
  type: string
- container: ''
  name: timeValue
  type: integer
- container: ''
  name: token
  type: string
- container: ''
  name: totalCredits
  type: integer
- container: ''
  name: type
  type: string
- container: ''
  name: unallocatedCredits
  type: integer
- container: ''
  name: unit
  type: string
- container: ''
  name: updatedAt
  type: integer
- container: ''
  name: username
  type: string
- container: set
  name: value
  type: reference
- container: ''
  name: wasMigrated
  type: boolean
- container: ''
  name: webhookUrl
  type: string
property_count: 124
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-prisma-cloud-mssp-api-context
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
- JSON-LD
- Linked Data
- Semantic Web
---
