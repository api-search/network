---
description: AdditionalDataTemporaryServices schema from Adyen API
layout: schema
name: AdditionalDataTemporaryServices
properties_list:
- description: 'The customer code, if supplied by a customer. * Encoding: ASCII * maxLength: 25'
  name: enhancedSchemeData.customerReference
  type: string
- description: 'The name or ID of the person working in a temporary capacity. * maxLength: 40. * Must not be all spaces. *Must not be all zeros.'
  name: enhancedSchemeData.employeeName
  type: string
- description: 'The job description of the person working in a temporary capacity. * maxLength: 40 * Must not be all spaces. *Must not be all zeros.'
  name: enhancedSchemeData.jobDescription
  type: string
- description: 'The amount paid for regular hours worked, [minor units](https://docs.adyen.com/development-resources/currency-codes). * maxLength: 7 * Must not be empty * Can be all zeros'
  name: enhancedSchemeData.regularHoursRate
  type: string
- description: 'The hours worked. * maxLength: 7 * Must not be empty * Can be all zeros'
  name: enhancedSchemeData.regularHoursWorked
  type: string
- description: 'The name of the person requesting temporary services. * maxLength: 40 * Must not be all zeros * Must not be all spaces'
  name: enhancedSchemeData.requestName
  type: string
- description: 'The billing period start date. * Format: ddMMyy * maxLength: 6'
  name: enhancedSchemeData.tempStartDate
  type: string
- description: 'The billing period end date. * Format: ddMMyy * maxLength: 6'
  name: enhancedSchemeData.tempWeekEnding
  type: string
- description: 'The total tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes). For example, 2000 means USD 20.00 * maxLength: 12'
  name: enhancedSchemeData.totalTaxAmount
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-additional-data-temporary-services-schema.json
slug: checkout-additional-data-temporary-services
tags:
- Payments
- Financial Services
- Fintech
title: AdditionalDataTemporaryServices
---
