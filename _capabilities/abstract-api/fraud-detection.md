---
consumed_apis:
- email-reputation
- phone-intelligence
- ip-intelligence
description: Unified fraud detection and risk assessment workflow combining email reputation, phone intelligence, and IP intelligence APIs. Used by security engineers, fraud analysts, and compliance teams to detect and block fraudulent users at signup or transaction time.
layout: capability
name: Abstract API Fraud Detection
operations:
- description: Check email reputation and risk score
  method: GET
  name: check-email-risk
  path: /v1/email-risk
- description: Check phone intelligence and risk score
  method: GET
  name: check-phone-risk
  path: /v1/phone-risk
- description: Check IP intelligence and security flags
  method: GET
  name: check-ip-risk
  path: /v1/ip-risk
personas:
- description: Security professional responsible for detecting and blocking fraudulent users and transactions
  id: fraud-analyst
  name: Fraud Analyst
- description: Engineer building fraud detection and threat intelligence systems
  id: security-engineer
  name: Security Engineer
provider_name: Abstract API
provider_slug: abstract-api
search_terms:
- data engineer
- engineer building data pipelines and enrichment workflows
- email validation
- detection and blocking of fraudulent users, transactions, and bot activity
- screenshots
- finance engineer
- phone validation
- check email address reputation, deliverability, and risk score to detect fraudulent or disposable emails
- product engineer
- automatic enrichment of user profiles with geographic, company, and temporal data
- web scraping
- validate phone number and retrieve carrier, line type, voip status, and risk score
- fraud detection
- check ip intelligence and security flags
- contacts
- fraud analyst
- vat validation
- exchange rates, vat validation, and iban validation for financial compliance
- check ip risk
- currencies
- check ip address risk signals
- security professional responsible for detecting and blocking fraudulent users and transactions
- analyze ip address for vpn, proxy, tor, abuse, hosting, and security risk signals
- engineer building fraud detection and threat intelligence systems
- security
- abstract api
- check email risk
- timezones
- developer building user onboarding and personalization features
- check ip intelligence
- compliance analyst
- check phone intelligence and risk score
- developer building payment, billing, and financial compliance systems
- currency conversion, vat compliance, and banking validation for financial applications
- public holidays
- check email reputation
- check email address risk and reputation
- exchange rates
- check phone number risk and validity
- ip geolocation
- avatars
- email reputation, phone intelligence, and ip intelligence for fraud prevention
- phone intelligence
- ip geolocation, company enrichment, and timezone data for user profile enrichment
- professional ensuring regulatory compliance for vat, banking, and financial reporting
- company enrichment
- iban validation
- image processing
- check phone risk
- check email reputation and risk score
- security engineer
- ip intelligence
- check phone intelligence
- email reputation
slug: fraud-detection
tags:
- Abstract Api
- Fraud Detection
- Security
- Email Reputation
- Phone Intelligence
- Ip Intelligence
tools:
- description: Check email address reputation, deliverability, and risk score to detect fraudulent or disposable emails
  hints:
    openWorld: true
    readOnly: true
  name: check-email-reputation
- description: Validate phone number and retrieve carrier, line type, VoIP status, and risk score
  hints:
    openWorld: true
    readOnly: true
  name: check-phone-intelligence
- description: Analyze IP address for VPN, proxy, Tor, abuse, hosting, and security risk signals
  hints:
    openWorld: true
    readOnly: true
  name: check-ip-intelligence
---
