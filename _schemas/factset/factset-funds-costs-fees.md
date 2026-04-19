---
description: ''
layout: schema
name: costsFees
properties_list:
- description: FactSet Security Identifier. Six alpha-numeric characters, excluding vowels, with a -S suffix (XXXXXX-S), resolved from the requestId of the Fund requested.
  name: fsymId
  type: string
- description: The management fee, or maintenance fee, is charged by the fund manager. This cost is usually between 0.5% and 2% of assets on average and is a periodic fee.
  name: managementExpenses
  type: number
- description: The Expense Date expressed in YYYY-MM-DD.
  name: date
  type: string
- description: ISO3 Currency
  name: currency
  type: string
- description: The transaction entry fee or purchase fee collected from investors when they join or leave a scheme. The fee is paid to the fund
  name: entryExpenses
  type: number
- description: The transaction exit fee is charged to investors when they redeem shares from a fund.
  name: exitExpenses
  type: number
- description: The Maximum sales load or initial Sales Fee is a reduction made from each investment in the fund, the maximum paid is dependent on the size of the purchase, it decreases as the investment increases. O
  name: frontExpensesMax
  type: number
- description: The Back Expense Maximum
  name: backExpensesMax
  type: number
- description: The Expense Ratio
  name: expenseRatio
  type: number
- description: The Expense Ratio Prospectus
  name: expenseRatioProspectus
  type: number
- description: The Initial Investment Minimum
  name: initInvestmentMin
  type: number
- description: The Initial Investment Individual Retirement Accounts
  name: initInvestmentIra
  type: number
- description: Swing Price. Swing pricing occurs when a fund provider adjusts the net asset value (NAV) of a fund in order to pass on trading costs to purchasing or redeeming shareholders. This anti-dilution techniq
  name: swingPrice
  type: number
- description: Swing Price Date. Swing pricing occurs when a fund provider adjusts the net asset value (NAV) of a fund in order to pass on trading costs to purchasing or redeeming shareholders. This anti-dilution te
  name: swingPriceDate
  type: string
- description: The SRI (Summary Risk Indicator) illustrates PRIIPs' risk and reward profile by measuring the market and credit risk level. Returns 1 for low risk up to 7 for higher risk.
  name: sriPriips
  type: integer
- description: Synthetic Risk and Reward Indicator illustrates a UCITS or NURS (Non-UCITS Retail Scheme) fund's risk and reward profile by measuring the market risk level. Returns 1 for low risk up to 7 for high ris
  name: srriUcits
  type: integer
- description: Represents fees made to an investment manager as a percentage of investment profits for generating positive returns.
  name: performanceFee
  type: number
- description: Represents the amount of trading commissions incurred to manage the portfolio as a percentage of the total assets of the fund.
  name: tradingExpenseRatio
  type: number
- description: The requested Id sent as input.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-funds-costs-fees-schema.json
slug: factset-funds-costs-fees
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: costsFees
---
