---
description: ''
layout: schema
name: AgreementStatus
properties_list:
- description: Unique identifier assigned by Mastercard to the agreement.
  name: agreementId
  type: string
- description: Status of the Agreement updated by DSP to either Approved or Rejected or Deleted. * Refer to Codes and Formats section for more details.
  name: agreementStatus
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-debtor-service-provider-resources-agreement-status-schema.json
slug: mastercard-debtor-service-provider-resources-agreement-status
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: AgreementStatus
---
