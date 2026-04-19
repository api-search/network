---
description: ''
layout: schema
name: sasbScoresAll
properties_list:
- description: Date for the period requested expressed in YYYY-MM-DD format.
  name: date
  type: string
- description: FactSet Entity Identifier. Six alpha-numeric characters, excluding vowels, with a -E suffix (XXXXXX-E).
  name: fsymId
  type: string
- description: Identifier that was used for the request.
  name: requestId
  type: string
- description: 'The name of the specific SASB Score type being shown in the response. This will be represented by the scoreTypes input: PULSE, INSIGHT, MOMENTUM, ART_VOL_TTM, CAT_VOL_TTM, or DYNAMIC_MAT.'
  name: scoreType
  type: string
- description: The Access and Affordability SASB Category.
  name: accessAndAffordability
  type: number
- description: The Air Quality SASB Category.
  name: airQuality
  type: number
- description: The All Categories Category. This represents the overall SASB Score for the given 'scoreType'. When scoreType = ESG_RANK, the data type will be string, otherwise data type will be a number with double
  name: allCategories
  type: object
- description: The Business Ethics Category.
  name: businessEthics
  type: number
- description: The Business Model Resilience Category.
  name: businessModelResilience
  type: number
- description: The Competitive Behavior Category.
  name: competitiveBehavior
  type: number
- description: The Critical Incident Risk Management Category.
  name: criticalIncidentRiskManagement
  type: number
- description: The Customer Privacy Category.
  name: customerPrivacy
  type: number
- description: The Customer Welfare Category.
  name: customerWelfare
  type: number
- description: The Data Security Category.
  name: dataSecurity
  type: number
- description: The Ecological Impacts Category.
  name: ecologicalImpacts
  type: number
- description: The Employee Engagement Diversity and Inclusion Category.
  name: employeeEngagementDiversityandInclusion
  type: number
- description: The Employee Health And Safety Category.
  name: employeeHealthAndSafety
  type: number
- description: The Energy Management Category.
  name: energyManagement
  type: number
- description: The Greenhouse Gases Emissions Category.
  name: gHGEmissions
  type: number
- description: The Human Rights and Community Relations Category.
  name: humanRightsandCommunityRelations
  type: number
- description: The Labor Practices Category.
  name: laborPractices
  type: number
- description: The Management of the Legal and Regulatory Environment Category.
  name: managementOfTheLegalAndRegulatoryEnvironment
  type: number
- description: The Materials Sourcing and Efficiency Category.
  name: materialsSourcingAndEfficiency
  type: number
- description: The Materiality Category. When scoreType = ESG_RANK, the data type will be string, otherwise data type will be a number with double format.
  name: materiality
  type: object
- description: The Physical Impacts of Climate Change Category.
  name: physicalImpactsOfClimateChange
  type: number
- description: The Product Quality and Safety Category.
  name: productQualityAndSafety
  type: number
- description: The Product Design And Lifecycle Management Category.
  name: productDesignAndLifecycleManagement
  type: number
- description: The Selling Practices And Product Labeling Category.
  name: sellingPracticesAndProductLabeling
  type: number
- description: The Supply Chain Management Category.
  name: supplyChainManagement
  type: number
- description: The Systemic Risk Management Category.
  name: systemicRiskManagement
  type: number
- description: The Waste and Hazardous Materials Management Category.
  name: wasteAndHazardousMaterialsManagement
  type: number
- description: The Water and Wastewater Management Category.
  name: waterAndWastewaterManagement
  type: number
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-esg-sasb-scores-all-schema.json
slug: factset-esg-sasb-scores-all
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: sasbScoresAll
---
