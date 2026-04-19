---
description: List of the statistics such as the average age, tenure, compensation of leadership, the number of executives, and the gender diversity of leadership for the requested identifier.
layout: schema
name: companyStats
properties_list:
- description: Average compensation for the executives
  name: averageMgmtCompensation
  type: number
- description: Avergae tenure of the people
  name: averageTenure
  type: number
- description: Median tenure
  name: medianTenure
  type: number
- description: Average of the executives on the management and board
  name: averageAge
  type: number
- description: Maximum age of the people on Management & Board
  name: maxAge
  type: number
- description: Minimum age of the person on board
  name: minimumAge
  type: number
- description: Median age of the people on board
  name: medianAge
  type: number
- description: Independent directors on the board
  name: boardIndependentDirectors
  type: number
- description: Number of female members on the board
  name: femaleBoardMembers
  type: number
- description: Percentage of female members on the board
  name: femaleBoardMembersPercent
  type: number
- description: Number of people on board.
  name: numberOfMembers
  type: number
- description: On Other Boards All
  name: onOtherBoardsAll
  type: number
- description: On Other Boards Corporate
  name: onOtherBoardsCorporate
  type: number
- description: Management and Board type, where MB = Management & Board, MGMT = Management, and BRD = Board. This is a pass-through value from the input used in the `mbType` query parameter.
  name: mbType
  type: string
- description: Original identifier used for the request.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-people-company-stats-schema.json
slug: factset-people-company-stats
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: companyStats
---
