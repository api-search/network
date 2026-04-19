---
description: TransactionRule schema from Adyen API
layout: schema
name: TransactionRule
properties_list:
- description: The level at which data must be accumulated, used in rules with `type` **velocity** or **maxUsage**. The level must be the [same or lower in hierarchy](https://docs.adyen.com/issuing/transaction-rules
  name: aggregationLevel
  type: string
- description: Your description for the transaction rule, maximum 300 characters.
  name: description
  type: string
- description: The date when the rule will stop being evaluated, in ISO 8601 extended offset date-time format. For example, **2020-12-18T10:15:30+01:00**. If not provided, the rule will be evaluated until the rule s
  name: endDate
  type: string
- description: The type and unique identifier of the resource to which the rule applies.
  name: entityKey
  type: object
- description: The unique identifier of the transaction rule.
  name: id
  type: string
- description: The [time interval](https://docs.adyen.com/issuing/transaction-rules#time-intervals) when the rule conditions apply.
  name: interval
  type: object
- description: The [outcome](https://docs.adyen.com/issuing/transaction-rules#outcome) that will be applied when a transaction meets the conditions of the rule. If not provided, by default, this is set to **hardBloc
  name: outcomeType
  type: string
- description: Your reference for the transaction rule, maximum 150 characters.
  name: reference
  type: string
- description: 'Indicates the type of request to which the rule applies. If not provided, by default, this is set to **authorization**. Possible values: **authorization**, **authentication**, **tokenization**, **bank'
  name: requestType
  type: string
- description: Contains one or more objects that define the [rule conditions](https://docs.adyen.com/issuing/transaction-rules#conditions). Each object must have a value and an operation which determines how the val
  name: ruleRestrictions
  type: object
- description: A positive or negative score applied to the transaction if it meets the conditions of the rule. Required when `outcomeType` is **scoreBased**. The value must be between **-100** and **100**.
  name: score
  type: integer
- description: The date when the rule will start to be evaluated, in ISO 8601 extended offset date-time format. For example, **2020-12-18T10:15:30+01:00**. If not provided when creating a transaction rule, the `star
  name: startDate
  type: string
- description: 'The status of the transaction rule. If you provide a `startDate` in the request, the rule is automatically created with an **active** status. Possible values: **active**, **inactive**.'
  name: status
  type: string
- description: 'The [type of rule](https://docs.adyen.com/issuing/transaction-rules#rule-types), which defines if a rule blocks transactions based on individual characteristics or accumulates data. Possible values: *'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-transaction-rule-schema.json
slug: configuration-transaction-rule
tags:
- Payments
- Financial Services
- Fintech
title: TransactionRule
---
