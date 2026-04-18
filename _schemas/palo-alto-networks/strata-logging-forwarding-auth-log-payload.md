---
description: Schema for a forwarded PAN-OS authentication log entry. Authentication logs capture user authentication events processed by the firewall's Authentication Policy, providing identity-based visibility for security monitoring, compliance, and zero-trust enforcement.
layout: schema
name: AuthLogPayload
properties_list:
- description: Timestamp when the authentication log entry was received by Strata Logging Service.
  name: receive_time
  type: string
- description: Serial number of the Palo Alto Networks device that generated this authentication log entry.
  name: serial
  type: string
- description: Log type identifier, always AUTH for authentication log entries.
  name: type
  type: string
- description: Authentication log subtype indicating the outcome of the authentication event.
  name: subtype
  type: string
- description: Source IP address of the authenticating client.
  name: src
  type: string
- description: Username or user principal name presented during authentication.
  name: src_user
  type: string
- description: Authentication protocol or method used to authenticate the user.
  name: auth_method
  type: string
- description: The name of the authentication source, server profile, or identity provider (e.g., Okta-SAML, corp-ldap, radius-server).
  name: auth_source
  type: string
- description: The result of the authentication attempt indicating whether it succeeded, failed, required an additional challenge, or timed out.
  name: auth_result
  type: string
- description: Multi-factor authentication vendor name if MFA was triggered during authentication (e.g., Duo, Okta, PingID, RSA SecurID).
  name: mfa_vendor
  type: string
- description: Result of the MFA challenge if multi-factor authentication was triggered as part of the authentication flow.
  name: mfa_result
  type: string
- description: Name of the Authentication Policy rule that triggered the authentication challenge for this session.
  name: rule_name
  type: string
- description: Name of the authentication profile configured on the firewall that was used to process this authentication event.
  name: auth_profile
  type: string
- description: Hostname of the firewall that generated this authentication log entry.
  name: device_name
  type: string
- description: Virtual system name or identifier on the firewall.
  name: vsys
  type: string
- description: Name of the log forwarding profile that forwarded this log entry.
  name: log_forwarding_profile
  type: string
- description: Output format in which this log entry was forwarded.
  name: output_format
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/strata-logging-forwarding-auth-log-payload-schema.json
slug: strata-logging-forwarding-auth-log-payload
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AuthLogPayload
---
