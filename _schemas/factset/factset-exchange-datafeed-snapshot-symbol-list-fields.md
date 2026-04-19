---
description: All available fields in service. FID = Field ID Number.
layout: schema
name: fields
properties_list:
- description: 'Field ID # 20. Exchange ISO-Code. Enumeration in Data Service Manual.'
  name: Exchange
  type: string
- description: 'Field ID # 4. Product identifier. Enumeration in Data Service Manual.'
  name: product
  type: string
- description: 'Field ID # 509. Current bid price'
  name: Bid
  type: number
- description: 'Field ID # 386. Current bid date'
  name: Bid_Date
  type: string
- description: 'Field ID # 385. Current bid time'
  name: Bid_Time
  type: integer
- description: 'Field ID # 505. Current bid size'
  name: Bid_Vol
  type: integer
- description: 'Field ID # 518. Current bid tick direction. Enumeration in Data Service Manual.'
  name: Bid_Tick
  type: string
- description: 'Field ID # 648. Official Closing Bid'
  name: Bid_Close
  type: number
- description: 'Field ID # 1062. Official Closing Bid Date'
  name: Bid_Close_Date
  type: string
- description: 'Field ID # 296. Official Closing Bid Volume'
  name: Bid_Close_Vol
  type: integer
- description: 'Field ID # 506. Exchange of the current bid price. Enumeration in Data Service Manual.'
  name: Bid_Exch
  type: string
- description: 'Field ID # 609. Current ask price'
  name: Ask
  type: number
- description: 'Field ID # 388. Current ask date'
  name: Ask_Date
  type: string
- description: 'Field ID # 387. Current ask time'
  name: Ask_Time
  type: integer
- description: 'Field ID # 605. Current ask size'
  name: Ask_Vol
  type: integer
- description: 'Field ID # 649. Official Closing ask'
  name: Ask_Close
  type: number
- description: 'Field ID # 1064. Official Closing ask Date'
  name: Ask_Close_Date
  type: string
- description: 'Field ID # 297. Official Closing ask Volume'
  name: Ask_Close_Vol
  type: integer
- description: 'Field ID # 606. Exchange of the current ask price. Enumeration in Data Service Manual.'
  name: Ask_Exch
  type: string
- description: 'Field ID # 277. Flag to indicate if a security is restricted from being sold short'
  name: Short_Sale_Indicator
  type: integer
- description: 'Field ID # 38. Current Quote Condition. Enumeration in Data Service Manual.'
  name: Quote_Condition
  type: string
- description: 'Field ID # 50. Official last trade price'
  name: Last_Price
  type: number
- description: 'Field ID # 384. Last Date'
  name: Last_Date
  type: string
- description: 'Field ID # 383. Official last traded time'
  name: Last_Time
  type: integer
- description: 'Field ID # 31. Official last traded volume'
  name: Last_Vol
  type: integer
- description: 'Field ID # 25. Official last tick. Enumeration in Data Service Manual.'
  name: Last_Tick
  type: string
- description: 'Field ID # 526. Official Close/Close Range 1 Price'
  name: Official_Close
  type: number
- description: 'Field ID # 1065. Official Close/Close Range 1 Time'
  name: Official_Close_Time
  type: integer
- description: 'Field ID # 33. Official last traded exchange. Enumeration in Data Service Manual.'
  name: Last_Exch
  type: string
- description: 'Field ID # 815. Settle Price'
  name: Settlement
  type: number
- description: 'Field ID # 912. Last traded Price'
  name: Traded_Price
  type: number
- description: 'Field ID # 868. Last traded Date'
  name: Traded_Date
  type: string
- description: 'Field ID # 916. Last traded Time'
  name: Traded_Time
  type: integer
- description: 'Field ID # 918. Last traded Volume'
  name: Traded_Vol
  type: integer
- description: 'Field ID # 1098. Last traded trade condition'
  name: Traded_Condition
  type: string
- description: 'Field ID # 662. Official last change'
  name: Net_Change
  type: number
- description: 'Field ID # 816. Official last percentage change'
  name: Percent_Change
  type: number
- description: 'Field ID # 1019. Unofficial last premarket trade price'
  name: Premkt_Price
  type: number
- description: 'Field ID # 1075. Unofficial last premarket traded time'
  name: Premkt_Time
  type: integer
- description: 'Field ID # 1832. Unofficial last premarket traded volume'
  name: Premkt_Vol
  type: integer
- description: 'Field ID # 1836. Unofficial last premarket cumulative volume'
  name: Premkt_CVol
  type: integer
- description: 'Field ID # 2029. Unofficial last post market trade price'
  name: Postmkt_Price
  type: number
- description: 'Field ID # 1076. Unofficial last post market traded time'
  name: Postmkt_Time
  type: integer
- description: 'Field ID # 1860. Unofficial last post market traded volume'
  name: Postmkt_Vol
  type: integer
- description: 'Field ID # 1864. Unofficial last post market cumulative volume'
  name: Postmkt_Cvol
  type: integer
- description: 'Field ID # 528. Off Book Cumulative Volume'
  name: Offbook_Cum_Vol
  type: integer
- description: 'Field ID # 448. The bid close price of today'
  name: Official_Bid_Close
  type: number
- description: 'Field ID # 476. The ask close price of today'
  name: Official_Ask_Close
  type: number
- description: 'Field ID # 136. Current mid date'
  name: Mid_Date
  type: string
- description: 'Field ID # 135. Current mid price time'
  name: Mid_Time
  type: integer
- description: 'Field ID # 132. Cumulative volume'
  name: Cvol
  type: integer
- description: 'Field ID # 341. Turnover'
  name: Turnover
  type: number
- description: 'Field ID # 780. Volume Weighted Average Price'
  name: Vwap
  type: number
- description: 'Field ID # 267. Cumulative trade count'
  name: Trade_Count
  type: integer
- description: 'Field ID # 269. Cumulative block count'
  name: Block_Trade_Count
  type: integer
- description: 'Field ID # 271. Cumulative block volume'
  name: Block_Cvol
  type: integer
- description: 'Field ID # 208. Previous trading days Close'
  name: Prev_Close
  type: number
- description: 'Field ID # 1051. Previous trading days Closing Date'
  name: Close_Date
  type: string
- description: 'Field ID # 892. Unadjusted Previous trading days Close'
  name: Prev_Close_Unadj
  type: number
- description: 'Field ID # 1172. Previous trading days Close late rollover[1]'
  name: Prev_Close_2
  type: number
- description: 'Field ID # 1176. Unadjusted Previous trading days Close late rollover'
  name: Prev_Close_Unadj_2
  type: number
- description: 'Field ID # 1093. Lower trading band'
  name: Lower_Trading_Band
  type: number
- description: 'Field ID # 1087. Upper trading band'
  name: Upper_Trading_Band
  type: number
- description: 'Field ID # 495. NYSE buy imbalance'
  name: Buy_Imbalance
  type: integer
- description: 'Field ID # 496. NYSE sell imbalance'
  name: Sell_Imbalance
  type: integer
- description: 'Field ID # 948. NAS buy imbalance'
  name: Nas_Buy_Imbalance
  type: integer
- description: 'Field ID # 949. NAS sell imbalance'
  name: Nas_Sell_Imbalance
  type: integer
- description: 'Field ID # 158. The Open Range 1 or Open Price'
  name: Open
  type: number
- description: 'Field ID # 107. Current high for the day'
  name: High
  type: number
- description: 'Field ID # 307. Current low for the day'
  name: Low
  type: number
- description: 'Field ID # 530. Venue'
  name: Venue
  type: string
- description: 'Field ID # 1820. Buy Id'
  name: Buy_Id
  type: string
- description: 'Field ID # 1824. Sell Id'
  name: Sell_Id
  type: string
- description: 'Field ID # 637. VWAP including only order book (automatic) trades'
  name: Auto_Trade_Vwap
  type: number
- description: 'Field ID # 635. Cumulative Volume calculated on all automated trading volumes for order-based segments'
  name: Auto_Trade_Cvol
  type: integer
- description: 'Field ID # 636. Trade Quantity including only order book (automatic) trades'
  name: Auto_Trade_Count
  type: integer
- description: 'Field ID # 531. Ex-Date Status'
  name: Ex_Date_Status
  type: string
- description: 'Field ID # 896. Net change in pre-market session(US stocks only)'
  name: Premkt_Net_Change
  type: number
- description: 'Field ID # 897. Percent change in pre-market session(US stocks only)'
  name: Premkt_Percent_Change
  type: number
- description: 'Field ID # 1345. Volume of the closing trade'
  name: Closing_Vol
  type: integer
- description: 'Field ID # 1517. FactSet Exchange Code of primary market for instrument. Determined by highest trading volume over a 3-day calendar period'
  name: Primary_Market
  type: string
- description: 'Field ID # 1621. Three Letter Country Code from ISO-3166'
  name: Iso_Country_Exchange
  type: string
- description: 'Field ID # 1743. Premarket Exchange. Enumeration in Data Service Manual.'
  name: Premkt_Exch
  type: string
- description: 'Field ID # 1744. Post Market Exchange. Enumeration in Data Service Manual.'
  name: Postmkt_Exch
  type: string
- description: 'Field ID # 1751. The Security type returned by FREF_SECURITY_type'
  name: Fref_Security_type
  type: string
- description: 'Field ID # 1762. Sub type of the security populated for funds right now'
  name: Security_Sub_type
  type: string
- description: 'Field ID # 1881. Post Market Net Change'
  name: Postmkt_Net_Change
  type: number
- description: 'Field ID # 1882. Post Market Percent Change.'
  name: Postmkt_Percent_Change
  type: number
- description: 'Field ID # 12. ISIN'
  name: Isin
  type: string
- description: 'Field ID # 14. CUSIP'
  name: Cusip
  type: string
- description: 'Field ID # 15. SEDOL'
  name: Sedol
  type: string
- description: 'Field ID # 8. Security Description'
  name: description
  type: string
- description: 'Field ID # 29. Total number of shares outstanding'
  name: Shares_Outstanding
  type: number
- description: 'Field ID # 62. Price currency code'
  name: Price_Currency
  type: string
- description: 'Field ID # 2800. Security Status or Halt Indicator. Enumeration in Data manual'
  name: Security_Status
  type: string
- description: 'Field ID # 389. GMT Offset in Minutes'
  name: Gmt_Offset
  type: integer
- description: 'Field ID # 650. Market segment'
  name: Market_Segment
  type: string
- description: 'Field ID # 651. Market sector'
  name: Market_Sector
  type: string
- description: 'Field ID # 633. Period'
  name: Period
  type: string
- description: 'Field ID # 652. ISO Country code'
  name: Country_Code
  type: string
- description: 'Field ID # 1896. Financial Status Enumeration Table'
  name: Financial_Status
  type: integer
- description: 'Field ID # 722. FactSet Industry Classification'
  name: Factset_Industry
  type: string
- description: 'Field ID # 723. FactSet Sector Classification'
  name: Factset_Sector
  type: string
- description: 'Field ID # 1414. Halt Status'
  name: Halt_Info
  type: integer
- description: 'Field ID # 724. Company Homepage'
  name: Homepage
  type: string
- description: 'Field ID # 1184. Halt description'
  name: Halt_description
  type: string
- description: 'Field ID # 1182. Currency the Exchange sends the prices to FactSet in'
  name: Feed_Currency
  type: string
- description: 'Field ID # 1190. Name of Country'
  name: Country_Name
  type: string
- description: 'Field ID # 427. Number of securities in a lot'
  name: Order_Lot_Size
  type: integer
- description: 'Field ID # 1335. The minimum number of lots required to trade'
  name: Trade_Lot_Size
  type: integer
- description: 'Field ID # 1499. Tick Size'
  name: Tick_Size
  type: number
- description: 'Field ID # 1507. Tick Group'
  name: Tick_Group
  type: string
- description: 'Field ID # 1508. Tick Pilot effective day'
  name: Tick_Pilot_Eff_Date
  type: string
- description: 'Field ID # 709. Average cumulative volume for last 30 days'
  name: Avg_30Day_Vol
  type: number
- description: 'Field ID # 719. Average cumulative volume over last 5 trading days'
  name: Avg_5Day_Vol
  type: number
- description: 'Field ID # 767. 52 Week High Price'
  name: High_52Week
  type: number
- description: 'Field ID # 768. 52 Week Low Price'
  name: Low_52Week
  type: number
- description: 'Field ID # 1220. 52 Week High Price Date'
  name: High_52Week_Date
  type: string
- description: 'Field ID # 1295. 52 Week Low Price Date'
  name: Low_52Week_Date
  type: string
- description: 'Field ID # 174. Trade Condition'
  name: Trade_Condition
  type: string
- description: 'Field ID # 746. 3 Month return for US mutual funds'
  name: Total_Return_3M
  type: number
- description: 'Field ID # 747. 52-Week Total Return for US mutual funds'
  name: Total_Return_52W
  type: number
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-exchange-datafeed-snapshot-symbol-list-fields-schema.json
slug: factset-exchange-datafeed-snapshot-symbol-list-fields
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: fields
---
