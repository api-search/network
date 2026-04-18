---
class_count: 7
classes:
- AnnouncementNotification
- CertificateExpiryNotification
- DataplaneUpgradeNotification
- IncidentDetail
- IncidentNotification
- ServiceInfo
- TenantContext
context_file: json-ld/palo-alto-sase-notifications-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-sase-notifications-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Sase Notifications from Palo Alto Networks.
layout: jsonld
name: Palo Alto Sase Notifications Context
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
- container: set
  name: affectedResources
  type: reference
- container: set
  name: affectedServices
  type: string
- container: ''
  name: body
  type: string
- container: ''
  name: callbackUrl
  type: reference
- container: ''
  name: category
  type: string
- container: ''
  name: certificateName
  type: string
- container: ''
  name: currentVersion
  type: string
- container: ''
  name: daysUntilExpiry
  type: integer
- container: ''
  name: description
  type: string
- container: ''
  name: detectionSource
  type: string
- container: ''
  name: effectiveDate
  type: dateTime
- container: ''
  name: estimatedEndTime
  type: dateTime
- container: ''
  name: expirationDate
  type: dateTime
- container: ''
  name: incidentId
  type: string
- container: ''
  name: issuer
  type: string
- container: ''
  name: notificationId
  type: string
- container: ''
  name: parentTsgId
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: resourceId
  type: string
- container: ''
  name: resourceType
  type: string
- container: ''
  name: scheduledTime
  type: dateTime
- container: ''
  name: serialNumber
  type: string
- container: ''
  name: serviceName
  type: string
- container: ''
  name: serviceStatus
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: subject
  type: string
- container: ''
  name: targetVersion
  type: string
- container: ''
  name: tenantName
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: title
  type: string
- container: ''
  name: tsgId
  type: string
- container: ''
  name: type
  type: string
- container: set
  name: usedBy
  type: string
property_count: 34
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-sase-notifications-context
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
