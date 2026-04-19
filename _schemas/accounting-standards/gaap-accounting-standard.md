---
description: A US GAAP accounting standard entry from the FASB Accounting Standards Codification, representing a topic, subtopic, or accounting standards update.
layout: schema
name: GaapAccountingStandard
properties_list:
- description: FASB ASC topic or ASU identifier
  name: id
  type: string
- description: Title of the accounting standard or update
  name: title
  type: string
- description: FASB ASC topic number
  name: topic
  type: string
- description: Name of the ASC topic area
  name: topicName
  type: string
- description: Date the standard or update was issued
  name: issuedDate
  type: string
- description: Mandatory effective date for public business entities
  name: effectiveDate
  type: string
- description: Brief description of the standard's purpose and key requirements
  name: summary
  type: string
- description: Entities to which the standard applies
  name: applicability
  type: string
- description: URL to the standard in the FASB ASC or on fasb.org
  name: url
  type: string
- description: Other ASC topic numbers related to this standard
  name: relatedTopics
  type: array
provider_name: Accounting Standards
provider_slug: accounting-standards
schema_file: json-schema/gaap-accounting-standard-schema.json
slug: gaap-accounting-standard
tags:
- Accounting Standards
- Finance
- GAAP
- IFRS
- XBRL
- Financial Reporting
- SEC
- FASB
title: GaapAccountingStandard
---
