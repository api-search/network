---
api_count: 4
apis:
- description: FHIR R4 compliant Patient Access API providing members secure access to their health data including claims, clinical data, and coverage information. Required under CMS Interoperability and Patient Acc
  name: Aetna Patient Access FHIR API
  slug: aetna-patient-access-fhir-api
- description: FHIR R4 compliant Provider Directory API providing standardized access to in-network provider and facility information. Enables third-party applications to search for providers, verify network partici
  name: Aetna Provider Directory FHIR API
  slug: aetna-provider-directory-fhir-api
- description: FHIR R4 compliant Drug Formulary API providing standardized access to plan formulary data including covered drugs, tiers, cost-sharing requirements, and prior authorization requirements. Implements th
  name: Aetna Drug Formulary FHIR API
  slug: aetna-drug-formulary-fhir-api
- description: 'Electronic Data Interchange connectivity for healthcare providers enabling electronic submission of claims, eligibility verification, claim status inquiries, and remittance advice. Accessible through '
  name: Aetna Provider EDI API
  slug: aetna-provider-edi-api
common:
- title: ''
  type: Website
  url: https://www.aetna.com
- title: ''
  type: Portal
  url: https://www.aetna.com/health-care-professionals.html
- title: ''
  type: Login
  url: https://member.aetna.com
- title: ''
  type: Support
  url: https://www.aetna.com/individuals-families/contact-aetna.html
- title: ''
  type: PrivacyPolicy
  url: https://www.aetna.com/legal-notices/privacy.html
- title: ''
  type: TermsOfService
  url: https://www.aetna.com/legal-notices/terms-of-use.html
created: ''
description: Aetna, a CVS Health company, offers health insurance, dental, vision, and other plans for individuals, families, employers, health care providers, and insurance agents and brokers. As a major U.S. health insurer, Aetna provides federally mandated FHIR R4 APIs for patient access, provider directory, and drug formulary data under CMS Interoperability and Patient Access Final Rule (CMS-9115-F). Provider connectivity is supported through the Availity portal for EDI transactions.
features:
- description: All patient-facing APIs implement HL7 FHIR Release 4 standard for interoperability.
  name: FHIR R4 Compliance
- description: Secure OAuth 2.0 authorization framework for patient-authorized third-party app access.
  name: SMART on FHIR Authorization
- description: Full compliance with CMS-9115-F Interoperability and Patient Access Final Rule.
  name: CMS Interoperability Compliance
- description: Complete HIPAA-compliant EDI transaction set for provider administrative workflows.
  name: EDI Transaction Support
- description: Supports member-directed payer-to-payer data exchange for continuity of care.
  name: Payer-to-Payer Data Exchange
- description: Implements HL7 DaVinci Project PDEX, PDex Drug Formulary, and Plan Net guides.
  name: DaVinci Implementation Guides
image: ''
integrations:
- description: Integrated pharmacy benefit management for prescription drug coverage and mail-order pharmacy.
  name: CVS Caremark
- description: Primary provider portal for EDI transactions, eligibility, claims, and authorization requests.
  name: Availity
- description: EHR integration enabling clinical workflows including prior authorization and care management.
  name: Epic Payer Platform
- description: FHIR-based integration enabling Aetna members to view health data in Apple Health app.
  name: Apple Health
- description: Interoperability network participation for cross-organization health data exchange.
  name: CommonWell Health Alliance
- description: Alignment with CMS Blue Button 2.0 FHIR API patterns for Medicare data access.
  name: CMS Blue Button 2.0
layout: provider
modified: '2026-04-19'
name: Aetna
skills: []
slug: aetna
solutions: []
tags:
- Health Insurance
- Healthcare
- FHIR
- Patient Access
- Provider Directory
url: https://raw.githubusercontent.com/api-evangelist/aetna/refs/heads/main/apis.yml
use_cases:
- description: Members use SMART on FHIR apps to access their complete health records across providers.
  name: Member Health Record Access
- description: Developers build directory search tools to help patients find in-network providers.
  name: Provider Network Verification
- description: Applications use formulary API to compare medication costs across Aetna plans.
  name: Drug Cost Comparison
- description: Healthcare providers submit claims electronically via EDI 837 transactions through Availity.
  name: Electronic Claims Submission
- description: Providers verify member eligibility and benefits in real time using 270/271 EDI transactions.
  name: Eligibility Verification
- description: Providers receive and process electronic remittance advice via EDI 835 transactions.
  name: Remittance Processing
---
