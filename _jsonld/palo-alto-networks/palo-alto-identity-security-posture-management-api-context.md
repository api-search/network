---
class_count: 19
classes:
- CreateTicketRequest
- DownloadCsvRequest
- FeatureState
- IdpInfo
- ListResponseIdpInfo
- ListResponseMapStringObject
- ListResponseMfaActivity
- ListResponseSaaSAccount
- ListResponseSaaSActivity
- ListResponseSaaSInstanceInfo
- ListResponseTicket
- MfaActivity
- MfaActivityCountByAppType
- RemediationRequest
- SaaSAccount
- SaaSActivity
- SaaSInstanceInfo
- Ticket
- UnlinkTicketRequest
context_file: json-ld/palo-alto-identity-security-posture-management-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-identity-security-posture-management-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Identity Security Posture Management Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Identity Security Posture Management Api Context
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
  name: accountName
  type: string
- container: ''
  name: accountType
  type: string
- container: ''
  name: activityDateTime
  type: dateTime
- container: ''
  name: activityType
  type: string
- container: ''
  name: admin
  type: boolean
- container: ''
  name: appId
  type: string
- container: ''
  name: appType
  type: string
- container: ''
  name: clientIP
  type: string
- container: ''
  name: count
  type: integer
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: createdTime
  type: dateTime
- container: ''
  name: creator
  type: string
- container: ''
  name: credentialsExpiresAt
  type: dateTime
- container: ''
  name: description
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: email
  type: string
- container: ''
  name: feature
  type: string
- container: ''
  name: fullName
  type: string
- container: ''
  name: githubOrgName
  type: string
- container: ''
  name: iconAppType
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: idpId
  type: string
- container: ''
  name: idpType
  type: string
- container: ''
  name: integrationId
  type: string
- container: ''
  name: ipAddress
  type: string
- container: ''
  name: isElevated
  type: boolean
- container: ''
  name: isLocal
  type: boolean
- container: ''
  name: isNonHuman
  type: boolean
- container: ''
  name: isOrphaned
  type: boolean
- container: ''
  name: issueTypeId
  type: string
- container: set
  name: items
  type: reference
- container: ''
  name: jobId
  type: string
- container: ''
  name: lastCredentialsRotated
  type: dateTime
- container: ''
  name: lastLoginTime
  type: dateTime
- container: ''
  name: lastModifiedTime
  type: dateTime
- container: ''
  name: lastScannedAt
  type: dateTime
- container: ''
  name: latestScanTime
  type: dateTime
- container: ''
  name: linkedHumanAccounts
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: mfaFactors
  type: string
- container: ''
  name: mfaStrength
  type: string
- container: ''
  name: rawData
  type: string
- container: set
  name: resourceIds
  type: string
- container: ''
  name: resourceName
  type: string
- container: ''
  name: resourceType
  type: string
- container: ''
  name: roles
  type: string
- container: ''
  name: rotatedBy
  type: string
- container: ''
  name: saasInstanceId
  type: string
- container: ''
  name: saasProviderId
  type: string
- container: ''
  name: saasProviderMfaType
  type: string
- container: ''
  name: saasProviderNhiName
  type: string
- container: ''
  name: service
  type: string
- container: ''
  name: settings
  type: reference
- container: ''
  name: status
  type: string
- container: ''
  name: summary
  type: string
- container: ''
  name: tenant
  type: string
- container: ''
  name: ticketKey
  type: string
- container: ''
  name: ticketUrl
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: total
  type: integer
- container: ''
  name: type
  type: string
- container: ''
  name: userAgent
  type: string
- container: ''
  name: userEmail
  type: string
- container: ''
  name: userFullName
  type: string
- container: ''
  name: userId
  type: string
- container: ''
  name: users
  type: string
property_count: 66
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-identity-security-posture-management-api-context
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
