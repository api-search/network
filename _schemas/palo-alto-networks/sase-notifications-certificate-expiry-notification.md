---
description: CertificateExpiryNotification schema from SASE Multitenant Notifications
layout: schema
name: CertificateExpiryNotification
properties_list:
- description: Unique identifier for this notification delivery.
  name: notificationId
  type: string
- description: Notification type identifier.
  name: type
  type: string
- description: Tenant Service Group identifier for the affected tenant.
  name: tsg_id
  type: string
- description: Name of the certificate approaching expiration.
  name: certificateName
  type: string
- description: Certificate serial number.
  name: serialNumber
  type: string
- description: Certificate issuer distinguished name.
  name: issuer
  type: string
- description: Certificate subject distinguished name.
  name: subject
  type: string
- description: Certificate expiration date and time.
  name: expirationDate
  type: string
- description: Number of days remaining until the certificate expires.
  name: daysUntilExpiry
  type: integer
- description: List of SASE services or configurations using this certificate.
  name: usedBy
  type: array
- description: Timestamp when this notification was generated.
  name: timestamp
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-notifications-certificate-expiry-notification-schema.json
slug: sase-notifications-certificate-expiry-notification
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: CertificateExpiryNotification
---
