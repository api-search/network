---
api_count: 3
apis:
- description: 'REST API for managing Ivanti Connect Secure (formerly Pulse Connect Secure) VPN appliances. Provides endpoints for system configuration, user and role management, authentication server configuration, '
  name: Ivanti Connect Secure REST API
  slug: ivanti-connect-secure-rest-api
- description: REST API for managing Ivanti Policy Secure (formerly Pulse Policy Secure) network access control appliances.
  name: Ivanti Policy Secure REST API
  slug: ivanti-policy-secure-rest-api
- description: REST API for managing Ivanti Neurons for Zero Trust Access (nZTA), providing endpoints for managing zero trust access policies, gateways, and user access.
  name: Ivanti Neurons for Zero Trust Access REST API
  slug: ivanti-neurons-zero-trust-rest-api
common:
- title: ''
  type: Website
  url: https://www.ivanti.com/products/connect-secure-vpn
- title: ''
  type: Documentation
  url: https://www.ivanti.com/support/product-documentation
- title: ''
  type: PrivacyPolicy
  url: https://www.ivanti.com/company/legal/privacy-policy
- title: ''
  type: TermsOfService
  url: https://www.ivanti.com/company/legal
- title: ''
  type: Status
  url: https://status.ivanticloud.com/
- title: ''
  type: Blog
  url: https://www.ivanti.com/blog
- title: ''
  type: Community
  url: https://forums.ivanti.com/s/welcome-pulse-secure?language=en_US
created: '2024-01-15'
description: APIs for Ivanti Pulse Secure (formerly Pulse Secure), providing secure remote access VPN, network access control, and zero trust access solutions.
features:
- description: Secure remote access to corporate resources through SSL VPN tunnels with granular access policies.
  name: SSL VPN Remote Access
- description: Identity-aware, application-level access control without exposing network resources.
  name: Zero Trust Network Access
- description: Enforce security policies on endpoints before granting network access with 802.1X and agent-based checks.
  name: Network Access Control
- description: Integrate with MFA providers for strong authentication on VPN and network access.
  name: Multi-Factor Authentication
- description: Validate endpoint compliance with security policies before granting access.
  name: Host Checker
- description: Define granular access policies based on user roles, device type, and compliance status.
  name: Role-Based Access Control
image: /assets/icons/pulse.png
integrations:
- description: Authenticate users against Active Directory for single sign-on and role mapping.
  name: Microsoft Active Directory
- description: Integrate with RADIUS for centralized authentication and accounting.
  name: RADIUS Servers
- description: Forward access logs and security events to SIEM platforms for monitoring and analysis.
  name: SIEM Platforms
- description: Integrate with mobile device management solutions for endpoint compliance verification.
  name: MDM Solutions
- description: Connect with SAML and OIDC identity providers for federated authentication.
  name: Identity Providers
layout: provider
modified: '2026-04-18'
name: Pulse
skills: []
slug: pulse
solutions: []
tags:
- Ivanti
- Network Security
- Secure Access
- SSL VPN
- VPN
- Zero Trust
url: https://raw.githubusercontent.com/api-evangelist/pulse/refs/heads/main/apis.yml
use_cases:
- description: Provide secure remote access to corporate applications and resources for distributed teams.
  name: Remote Workforce Access
- description: Implement zero trust security with per-application access controls and continuous verification.
  name: Zero Trust Architecture
- description: Securely enable bring-your-own-device access with endpoint compliance checking.
  name: BYOD Management
- description: Grant controlled, time-limited access to third-party partners and contractors.
  name: Partner and Contractor Access
---
