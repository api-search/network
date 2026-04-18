---
class_count: 14
classes:
- EmailChannelDetails
- EmailDetails
- MtNotifAggKey
- MtNotification
- NotifCategoryDetail
- NotifChannel
- NotifFilter
- NotifListApiReqBody
- NotifProfile
- NotifStateChangeApiBody
- NotifSubCategoryDetail
- NotifTypeDetail
- SortBy
- WebhookChannelDetails
context_file: json-ld/palo-alto-sase-multitenant-notifications-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-sase-multitenant-notifications-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Sase Multitenant Notifications Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Sase Multitenant Notifications Api Context
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
  name: action
  type: string
- container: ''
  name: aggKey
  type: reference
- container: ''
  name: authType
  type: string
- container: ''
  name: bestPractice
  type: boolean
- container: ''
  name: body
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: createdTime
  type: decimal
- container: ''
  name: description
  type: string
- container: ''
  name: emailChannelDetails
  type: reference
- container: ''
  name: emailId
  type: string
- container: set
  name: emails
  type: reference
- container: set
  name: excludeTenantList
  type: string
- container: set
  name: failureTenant
  type: string
- container: ''
  name: field
  type: string
- container: set
  name: filters
  type: reference
- container: ''
  name: id
  type: string
- container: ''
  name: impactedTenantCount
  type: decimal
- container: set
  name: impactedTenants
  type: string
- container: ''
  name: inAppFlag
  type: boolean
- container: ''
  name: name
  type: string
- container: ''
  name: needLicense
  type: boolean
- container: set
  name: notifCategoryList
  type: reference
- container: set
  name: notifChannels
  type: reference
- container: set
  name: notifIds
  type: string
- container: ''
  name: notifReadState
  type: string
- container: ''
  name: notifType
  type: string
- container: set
  name: notifTypeDetails
  type: reference
- container: ''
  name: num
  type: integer
- container: ''
  name: opState
  type: string
- container: ''
  name: page
  type: reference
- container: ''
  name: profileName
  type: string
- container: ''
  name: readState
  type: string
- container: ''
  name: size
  type: integer
- container: ''
  name: sortBy
  type: string
- container: set
  name: sortByList
  type: reference
- container: ''
  name: status
  type: string
- container: ''
  name: subCategory
  type: string
- container: set
  name: subCategoryList
  type: reference
- container: set
  name: successTenant
  type: string
- container: ''
  name: tag
  type: reference
- container: ''
  name: template
  type: reference
- container: ''
  name: templateJson
  type: string
- container: set
  name: tenantList
  type: string
- container: ''
  name: token
  type: string
- container: ''
  name: tsgId
  type: string
- container: ''
  name: type
  type: string
- container: set
  name: urls
  type: string
- container: set
  name: values
  type: string
- container: ''
  name: webhookChannelDetails
  type: reference
property_count: 49
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-sase-multitenant-notifications-api-context
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
