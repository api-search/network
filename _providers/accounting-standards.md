---
api_count: 5
apis:
- description: The 2026 GAAP Financial Reporting Taxonomy (GRT) is the official XBRL taxonomy maintained by FASB for SEC financial filings. It incorporates updates for FASB accounting standards published through Dec
  name: US GAAP Financial Reporting Taxonomy 2026
  slug: ''
- description: The SEC EDGAR XBRL APIs provide free, real-time access to structured financial data from public company filings. APIs include company submissions, company facts (all XBRL disclosures), company concept
  name: SEC EDGAR XBRL API
  slug: ''
- description: International Financial Reporting Standards (IFRS) are global accounting standards issued by the International Accounting Standards Board (IASB). IFRS standards govern the financial reporting of compa
  name: IFRS Accounting Standards
  slug: ''
- description: The FASB Accounting Standards Codification (ASC) is the single source of authoritative nongovernmental U.S. GAAP. Organized into Topics, Subtopics, Sections, and Paragraphs, the ASC provides the compl
  name: FASB Accounting Standards Codification
  slug: ''
- description: eXtensible Business Reporting Language (XBRL) is an open international standard for digital business reporting maintained by XBRL International. It enables the exchange of business information in a st
  name: XBRL International Specification
  slug: ''
common:
- title: Financial Accounting Standards Board
  type: Website
  url: https://www.fasb.org/
- title: IFRS Foundation
  type: Website
  url: https://www.ifrs.org/
- title: XBRL US
  type: Website
  url: https://xbrl.us/
- title: XBRL GitHub Organization
  type: GitHubOrganization
  url: https://github.com/xbrl
- title: SEC EDGAR Data Portal
  type: Tools
  url: https://data.sec.gov/
- title: Accounting Standards JSON-LD Context
  type: JSON-LD
  url: https://raw.githubusercontent.com/api-evangelist/accounting-standards/refs/heads/main/json-ld/accounting-standards-context.jsonld
- title: Accounting Standards Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/accounting-standards/refs/heads/main/vocabulary/accounting-standards-vocabulary.yaml
created: '2025-01-01'
description: Accounting Standards are the formal rules and guidelines that govern how financial transactions and statements are recorded, reported, and disclosed. They ensure consistency, transparency, and comparability across financial reports, and include frameworks like GAAP and IFRS. Digital reporting standards like XBRL enable structured, machine-readable financial filings.
features:
- description: XBRL taxonomies enable machine-readable financial statement reporting that regulators, investors, and analysts can process programmatically.
  name: Structured Financial Reporting
- description: The FASB ASC provides the single authoritative source of US GAAP organized by topic for consistent application across entities.
  name: US GAAP Codification
- description: IFRS provides globally harmonized accounting standards enabling cross-border financial comparability in over 140 jurisdictions.
  name: International Standards Harmonization
- description: SEC EDGAR XBRL APIs provide real-time access to structured financial data from all public company filings as JSON.
  name: Real-Time Financial Data Access
- description: The Data Quality Committee Rules Taxonomy (DQCRT) provides machine-enforceable rules for validating XBRL-tagged financial data.
  name: Data Quality Rules
- description: Annual FASB taxonomy releases incorporate new accounting standards and ensure accurate representation of current GAAP requirements.
  name: Taxonomy Versioning
image: /assets/icons/accounting-standards.png
integrations:
- description: The SEC's public filing database mandating XBRL for financial disclosures, providing free API access to all structured filing data.
  name: SEC EDGAR
- description: Industry consortium supporting XBRL adoption in the US, providing taxonomy resources, training, and data quality rule development.
  name: XBRL US
- description: Human-readable HTML combining with machine-readable XBRL tags, now required by the SEC for financial statement filings.
  name: iXBRL (Inline XBRL)
- description: European Securities and Markets Authority mandating IFRS XBRL reporting under the European Single Electronic Format (ESEF).
  name: ESMA / European Reporting
- description: Deloitte's Accounting Research Tool providing access to FASB ASC and IFRS standards with interpretive guidance and examples.
  name: Deloitte DART
jsonld:
- class_count: 6
  name: Accounting Standards Context
  property_count: 39
  slug: accounting-standards-context
layout: provider
modified: '2026-04-19'
name: Accounting Standards
skills: []
slug: accounting-standards
solutions: []
tags:
- Accounting Standards
- Finance
- GAAP
- IFRS
- XBRL
- Financial Reporting
- SEC
- FASB
url: https://raw.githubusercontent.com/api-evangelist/accounting-standards/refs/heads/main/apis.yml
use_cases:
- description: Companies use XBRL taxonomies when filing 10-K, 10-Q, and 8-K reports with the SEC, ensuring structured, machine-readable disclosure.
  name: Public Company Financial Reporting
- description: Investors and analysts use SEC EDGAR XBRL APIs to retrieve structured financial statements for quantitative analysis and screening.
  name: Financial Data Analysis
- description: CPAs and finance professionals use the FASB ASC to research applicable US GAAP guidance for specific transaction types and disclosures.
  name: Accounting Research
- description: Finance teams implement GAAP or IFRS accounting standards to meet regulatory requirements and auditor expectations.
  name: Regulatory Compliance
- description: FinTech platforms integrate with SEC EDGAR APIs to ingest standardized financial data for valuation models, credit analysis, and benchmarking.
  name: FinTech Integration
---
