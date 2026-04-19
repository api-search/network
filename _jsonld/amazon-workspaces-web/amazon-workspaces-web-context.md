---
class_count: 139
classes:
- AssociateBrowserSettingsResponse
- AssociateIpAccessSettingsResponse
- AssociateNetworkSettingsResponse
- AssociateTrustStoreResponse
- AssociateUserAccessLoggingSettingsResponse
- AssociateUserSettingsResponse
- CreateBrowserSettingsResponse
- Tag
- CreateIdentityProviderResponse
- CreateIpAccessSettingsResponse
- IpRule
- description
- CreateNetworkSettingsResponse
- CreatePortalResponse
- CreateTrustStoreResponse
- CreateUserAccessLoggingSettingsResponse
- CreateUserSettingsResponse
- DeleteBrowserSettingsResponse
- DeleteIdentityProviderResponse
- DeleteIpAccessSettingsResponse
- DeleteNetworkSettingsResponse
- DeletePortalResponse
- DeleteTrustStoreResponse
- DeleteUserAccessLoggingSettingsResponse
- DeleteUserSettingsResponse
- DisassociateBrowserSettingsResponse
- DisassociateIpAccessSettingsResponse
- DisassociateNetworkSettingsResponse
- DisassociateTrustStoreResponse
- DisassociateUserAccessLoggingSettingsResponse
- DisassociateUserSettingsResponse
- GetBrowserSettingsResponse
- GetIdentityProviderResponse
- GetIpAccessSettingsResponse
- GetNetworkSettingsResponse
- GetPortalResponse
- GetPortalServiceProviderMetadataResponse
- GetTrustStoreResponse
- GetTrustStoreCertificateResponse
- GetUserAccessLoggingSettingsResponse
- GetUserSettingsResponse
- ListBrowserSettingsResponse
- ListIdentityProvidersResponse
- ListIpAccessSettingsResponse
- ListNetworkSettingsResponse
- ListPortalsResponse
- ListTagsForResourceResponse
- ListTrustStoreCertificatesResponse
- ListTrustStoresResponse
- ListUserAccessLoggingSettingsResponse
- ListUserSettingsResponse
- TagResourceResponse
- UntagResourceResponse
- UpdateBrowserSettingsResponse
- UpdateIdentityProviderResponse
- UpdateIpAccessSettingsResponse
- UpdateNetworkSettingsResponse
- UpdatePortalResponse
- UpdateTrustStoreResponse
- UpdateUserAccessLoggingSettingsResponse
- UpdateUserSettingsResponse
- AssociateBrowserSettingsRequest
- AssociateIpAccessSettingsRequest
- AssociateNetworkSettingsRequest
- AssociateTrustStoreRequest
- AssociateUserAccessLoggingSettingsRequest
- AssociateUserSettingsRequest
- BrowserSettings
- BrowserSettingsSummary
- Certificate
- CertificateSummary
- EncryptionContextMap
- CreateBrowserSettingsRequest
- IdentityProviderDetails
- CreateIdentityProviderRequest
- CreateIpAccessSettingsRequest
- CreateNetworkSettingsRequest
- CreatePortalRequest
- CreateTrustStoreRequest
- CreateUserAccessLoggingSettingsRequest
- CreateUserSettingsRequest
- DeleteBrowserSettingsRequest
- DeleteIdentityProviderRequest
- DeleteIpAccessSettingsRequest
- DeleteNetworkSettingsRequest
- DeletePortalRequest
- DeleteTrustStoreRequest
- DeleteUserAccessLoggingSettingsRequest
- DeleteUserSettingsRequest
- DisassociateBrowserSettingsRequest
- DisassociateIpAccessSettingsRequest
- DisassociateNetworkSettingsRequest
- DisassociateTrustStoreRequest
- DisassociateUserAccessLoggingSettingsRequest
- DisassociateUserSettingsRequest
- GetBrowserSettingsRequest
- GetIdentityProviderRequest
- IdentityProvider
- GetIpAccessSettingsRequest
- IpAccessSettings
- GetNetworkSettingsRequest
- NetworkSettings
- GetPortalRequest
- Portal
- GetPortalServiceProviderMetadataRequest
- GetTrustStoreCertificateRequest
- GetTrustStoreRequest
- TrustStore
- GetUserAccessLoggingSettingsRequest
- UserAccessLoggingSettings
- GetUserSettingsRequest
- UserSettings
- IdentityProviderSummary
- IpAccessSettingsSummary
- ListBrowserSettingsRequest
- ListIdentityProvidersRequest
- ListIpAccessSettingsRequest
- ListNetworkSettingsRequest
- ListPortalsRequest
- ListTagsForResourceRequest
- ListTrustStoreCertificatesRequest
- ListTrustStoresRequest
- ListUserAccessLoggingSettingsRequest
- ListUserSettingsRequest
- NetworkSettingsSummary
- PortalSummary
- TagResourceRequest
- TrustStoreSummary
- UntagResourceRequest
- UpdateBrowserSettingsRequest
- UpdateIdentityProviderRequest
- UpdateIpAccessSettingsRequest
- UpdateNetworkSettingsRequest
- UpdatePortalRequest
- UpdateTrustStoreRequest
- UpdateUserAccessLoggingSettingsRequest
- UpdateUserSettingsRequest
- UserAccessLoggingSettingsSummary
- UserSettingsSummary
context_file: json-ld/amazon-workspaces-web-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-workspaces-web/refs/heads/main/json-ld/amazon-workspaces-web-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Workspaces Web from Amazon WorkSpaces Web.
layout: jsonld
name: Amazon Workspaces Web Context
namespaces:
- prefix: amz
  uri: https://amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: browserSettingsArn
  type: string
- container: ''
  name: portalArn
  type: string
- container: ''
  name: ipAccessSettingsArn
  type: string
- container: ''
  name: networkSettingsArn
  type: string
- container: ''
  name: trustStoreArn
  type: string
- container: ''
  name: userAccessLoggingSettingsArn
  type: string
- container: ''
  name: userSettingsArn
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: identityProviderArn
  type: string
- container: ''
  name: ipRange
  type: string
- container: ''
  name: portalEndpoint
  type: string
- container: ''
  name: browserSettings
  type: string
- container: ''
  name: identityProvider
  type: string
- container: ''
  name: ipAccessSettings
  type: string
- container: ''
  name: networkSettings
  type: string
- container: ''
  name: portal
  type: string
- container: ''
  name: serviceProviderSamlMetadata
  type: string
- container: ''
  name: trustStore
  type: string
- container: ''
  name: certificate
  type: string
- container: ''
  name: userAccessLoggingSettings
  type: string
- container: ''
  name: userSettings
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: identityProviders
  type: string
- container: ''
  name: portals
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: certificateList
  type: string
- container: ''
  name: trustStores
  type: string
- container: ''
  name: associatedPortalArns
  type: string
- container: ''
  name: browserPolicy
  type: string
- container: ''
  name: body
  type: string
- container: ''
  name: issuer
  type: string
- container: ''
  name: notValidAfter
  type: string
- container: ''
  name: notValidBefore
  type: string
- container: ''
  name: subject
  type: string
- container: ''
  name: thumbprint
  type: string
- container: ''
  name: additionalEncryptionContext
  type: string
- container: ''
  name: clientToken
  type: string
- container: ''
  name: customerManagedKey
  type: string
- container: ''
  name: identityProviderDetails
  type: string
- container: ''
  name: identityProviderName
  type: string
- container: ''
  name: identityProviderType
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: ipRules
  type: string
- container: ''
  name: securityGroupIds
  type: string
- container: ''
  name: subnetIds
  type: string
- container: ''
  name: vpcId
  type: string
- container: ''
  name: authenticationType
  type: string
- container: ''
  name: kinesisStreamArn
  type: string
- container: ''
  name: copyAllowed
  type: string
- container: ''
  name: disconnectTimeoutInMinutes
  type: string
- container: ''
  name: downloadAllowed
  type: string
- container: ''
  name: idleDisconnectTimeoutInMinutes
  type: string
- container: ''
  name: pasteAllowed
  type: string
- container: ''
  name: printAllowed
  type: string
- container: ''
  name: uploadAllowed
  type: string
- container: ''
  name: creationDate
  type: string
- container: ''
  name: browserType
  type: string
- container: ''
  name: portalStatus
  type: string
- container: ''
  name: rendererType
  type: string
- container: ''
  name: statusReason
  type: string
- container: ''
  name: certificatesToAdd
  type: string
- container: ''
  name: certificatesToDelete
  type: string
property_count: 63
provider_name: Amazon WorkSpaces Web
provider_slug: amazon-workspaces-web
slug: amazon-workspaces-web-context
tags:
- AWS
- End User Computing
- Secure Browser
- Virtual Desktop
- Zero Trust
- JSON-LD
- Linked Data
- Semantic Web
---
