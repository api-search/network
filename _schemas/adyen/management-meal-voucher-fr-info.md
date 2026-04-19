---
description: MealVoucherFRInfo schema from Adyen API
layout: schema
name: MealVoucherFRInfo
properties_list:
- description: 'Meal Voucher conecsId. Format: digits only'
  name: conecsId
  type: string
- description: 'Meal Voucher siret. Format: 14 digits.'
  name: siret
  type: string
- description: 'The list of additional payment methods. Allowed values: **mealVoucher_FR_edenred**, **mealVoucher_FR_groupeup**, **mealVoucher_FR_natixis**, **mealVoucher_FR_sodexo**.'
  name: subTypes
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-meal-voucher-fr-info-schema.json
slug: management-meal-voucher-fr-info
tags:
- Payments
- Financial Services
- Fintech
title: MealVoucherFRInfo
---
