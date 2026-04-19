---
description: 'The FactSet Truvalue Score types being requested. Score Types include the Pulse, Insight, Momentum, Article Volume, Category Volume, Dynamic Materiality Score, Adjusted Insight, and Industry Percentile. When left blank all score types will be returned for the requested Id. To specify select scores returned in the response, provide a comma-separated list of the scores using the description below. <p>These scores use the same underlying data and 100-point scale, except for ranks and percentiles. The cognitive computing system behind FactSet''s Truvalue Platform uses natural language processing to interpret semantic content and generate analytics. It does so by applying criteria that are consistent with established sustainability and ESG frameworks, scoring data points on performance using a 0 to 100 scale. A score of 50 represents a neutral impact. Scores above 50 indicate positive performance, and scores below reflect negative performance.</p> ### SDG Score Types |**SDG Category
  Input**|**Description**| ||| |**PULSE**|*Pulse Score*, is a measure of near-term performance changes that highlights opportunities and controversies, enabling real-time monitoring of companies. It focuses on events of the day and provides a responsive signal to alert investors to dynamic moves.| |**INSIGHT**|*Insight Score*, a measure of a company''s longer-term SDG track record, similar to a ratings system. Scores are less sensitive to daily events and reflect the enduring performance record of a company over time. Scores are derived using an exponentially-weighted moving average of the Pulse, defined below, and the half-life of an event''s influence on the overall score is 6 months.| |**MOMENTUM**|*Momentum Score*, measures the trend of a company''s Insight score. It is a unique SDG metric in the industry that gives investors a high-precision view of the trajectory of a company''s ESG performance, relative to peers. It does so by precisely articulating upward or downward movement, relative
  to that of all others in the universe, making it a measure that enhances quantitative workflows.| |**DYNAMIC_MAT**|*Dynamic Materiality Score*, shows the percentage value of data flow by category compared with the total data flow for the organization | |**ADJ_INSIGHT**|*Adjusted Insight*, Measures company ESG performance, generating scores for lower-volume and zero-volume firms by blending company scores with industry medians. **(ONLY Vaild for `IMPACT` category)**. <p>**Adjusted Insight Score = (# of articles / 5) x Company Insight Score + ((5 - # of articles) / 5) x Industry (or Sector) Median Insight Score.</p>| |**IND_PCTL**|*Industry Percentile*, offers context on company Adjusted Insight scores relative to peers in the same SICS Industry. This value is used to establish the textual ESG Rank. **(ONLY Vaild for `IMPACT` category).**| |**TTM_VOLUME**|*TTM Volume*, measures the data flow over a trailing twelve month period.| |**SDG_RANK**|*SDG Rank*, offers rank leveraging the 16 ESG
  categories defined by Sustainable Development Goals (SDG).**(ONLY Vaild for `IMPACT` category)**The datatype for the data returned when this score types is requested is String.|'
layout: schema
name: sdgScoreTypes
properties_list: []
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-esg-sdg-score-types-schema.json
slug: factset-esg-sdg-score-types
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: sdgScoreTypes
---
