---
class_count: 47
classes:
- AdData
- AdInfo
- AdPageInfo
- Ad
- AirQuality
- AutocompleteLocation
- Bid
- ConfidenceQuantity
- ConfidenceRange
- CurrentConditions
- DailyForecast
- DailyIndex
- DeviceInfo
- EventConfidence
- ExtendedForecastInformation
- FavoriteLocation
- HalfDayForecast
- HourlyForecast
- IndexDay
- LandmarkReference
- LocationSettingsInfo
- MinuteCastForecast
- MinuteCastMinute
- OrtbContent
- OrtbData
- OrtbPublisher
- OrtbSegment
- OrtbSite
- PageInfo
- Partner
- Pollutant
- Polygon
- PrebidTimeoutOutVars
- PrecipitationSummary
- QuantityRangeEstimate
- RainePageView
- RecentLocation
- SessionInfo
- StormPosition
- Storm
- UserInfo
- UserNetwork
- UTMInfo
- UVIndex
- WeatherInfo
- name
- url
context_file: json-ld/accuweather-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/json-ld/accuweather-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Accuweather from AccuWeather.
layout: jsonld
name: Accuweather Context
namespaces:
- prefix: acw
  uri: https://developer.accuweather.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: accuId
  type: integer
- container: ''
  name: activityType
  type: string
- container: ''
  name: adDivId
  type: string
- container: ''
  name: adInfo
  type: string
- container: ''
  name: adPageInfo
  type: string
- container: ''
  name: adSlots
  type: string
- container: ''
  name: adUnitCode
  type: string
- container: ''
  name: adminCode
  type: string
- container: ''
  name: ads
  type: string
- container: ''
  name: airQuality
  type: string
- container: ''
  name: apparentTempImperial
  type: decimal
- container: ''
  name: awxTimeout
  type: integer
- container: ''
  name: basin
  type: string
- container: ''
  name: basinId
  type: string
- container: ''
  name: basinSlug
  type: string
- container: ''
  name: bidder
  type: string
- container: set
  name: bidders
  type: string
- container: ''
  name: bot
  type: boolean
- container: ''
  name: brand
  type: string
- container: ''
  name: bundleId
  type: string
- container: ''
  name: bundleUrl
  type: string
- container: ''
  name: buyItNowSkipGoogleAdManager
  type: boolean
- container: ''
  name: campaign
  type: string
- container: set
  name: categories
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: categoryColor
  type: string
- container: ''
  name: ceiling
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: cloudCover
  type: string
- container: ''
  name: code
  type: string
- container: ''
  name: color
  type: string
- container: ''
  name: concentration
  type: string
- container: ''
  name: conditions
  type: string
- container: ''
  name: content
  type: string
- container: ''
  name: context
  type: string
- container: ''
  name: cookie3p
  type: string
- container: set
  name: coordinates
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: countryCode
  type: string
- container: ''
  name: data
  type: string
- container: ''
  name: date
  type: dateTime
- container: ''
  name: dateTime
  type: string
- container: ''
  name: dateTimeLabel
  type: string
- container: ''
  name: dateTimeLabelShort
  type: string
- container: ''
  name: day
  type: string
- container: ''
  name: dayOfWeek
  type: string
- container: ''
  name: dayOfWeekAbbreviated
  type: string
- container: set
  name: days
  type: string
- container: ''
  name: dbz
  type: decimal
- container: ''
  name: device
  type: string
- container: ''
  name: deviceClass
  type: string
- container: ''
  name: dewPoint
  type: string
- container: ''
  name: direction
  type: string
- container: ''
  name: disableInitialAdLoad
  type: boolean
- container: ''
  name: displayAmount
  type: string
- container: ''
  name: displayDate
  type: string
- container: ''
  name: displayHighTemperature
  type: string
- container: ''
  name: displayLowTemperature
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: displayRealFeel
  type: string
- container: ''
  name: displayRealFeelShade
  type: string
- container: ''
  name: displayTemperature
  type: string
- container: ''
  name: displayTime
  type: string
- container: ''
  name: distance
  type: string
- container: ''
  name: dma
  type: string
- container: ''
  name: domain
  type: string
- container: ''
  name: dominantPollutant
  type: string
- container: ''
  name: end
  type: dateTime
- container: ''
  name: endDate
  type: dateTime
- container: ''
  name: epoch
  type: integer
- container: ''
  name: epochEndDate
  type: integer
- container: ''
  name: epochStartDate
  type: integer
- container: ''
  name: event
  type: string
- container: ''
  name: eventKey
  type: string
- container: ''
  name: eventName
  type: string
- container: ''
  name: extended
  type: string
- container: ''
  name: extensions
  type: string
- container: ''
  name: forecastRanges
  type: string
- container: ''
  name: fullDayOfWeek
  type: string
- container: ''
  name: globalAdConfig
  type: string
- container: ''
  name: governmentId
  type: integer
- container: ''
  name: gptEnableSingleRequest
  type: boolean
- container: ''
  name: gptLazyLoading
  type: string
- container: ''
  name: group
  type: string
- container: ''
  name: gusts
  type: string
- container: ''
  name: hasAlert
  type: boolean
- container: ''
  name: hasPrivacyPolicy
  type: boolean
- container: ''
  name: hazardStatement
  type: string
- container: ''
  name: high
  type: string
- container: ''
  name: higher
  type: string
- container: ''
  name: humidity
  type: string
- container: ''
  name: humidityValue
  type: integer
- container: ''
  name: ice
  type: string
- container: ''
  name: icon
  type: integer
- container: ''
  name: iconCode
  type: integer
- container: ''
  name: iconPhrase
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: index
  type: decimal
- container: ''
  name: indexName
  type: string
- container: ''
  name: indexType
  type: string
- container: ''
  name: indoorHumidity
  type: string
- container: ''
  name: indoorHumidityCategory
  type: string
- container: ''
  name: isActive
  type: boolean
- container: ''
  name: isBefore7PM
  type: boolean
- container: ''
  name: isBuyItNow
  type: boolean
- container: ''
  name: isCurrent
  type: boolean
- container: ''
  name: isDayLight
  type: boolean
- container: ''
  name: isDayTime
  type: boolean
- container: ''
  name: isFuture
  type: boolean
- container: ''
  name: isHistorical
  type: boolean
- container: ''
  name: isMarked
  type: boolean
- container: ''
  name: isOptimizedForMobile
  type: boolean
- container: ''
  name: isPeak
  type: boolean
- container: ''
  name: isPrebidDisabled
  type: boolean
- container: ''
  name: javascriptBody
  type: string
- container: ''
  name: javascriptHead
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: keywords
  type: string
- container: ''
  name: landmark
  type: string
- container: set
  name: landmarkReferences
  type: string
- container: ''
  name: language
  type: string
- container: ''
  name: latitude
  type: decimal
- container: ''
  name: level
  type: string
- container: ''
  name: likely
  type: string
- container: ''
  name: link
  type: string
- container: ''
  name: localDate
  type: dateTime
- container: ''
  name: localDayOfWeek
  type: string
- container: ''
  name: localEnd
  type: dateTime
- container: ''
  name: localStart
  type: dateTime
- container: ''
  name: localTime
  type: string
- container: ''
  name: localizedStartDate
  type: string
- container: ''
  name: localizedStatus
  type: string
- container: ''
  name: locationKey
  type: string
- container: ''
  name: locationSettingsInfo
  type: string
- container: ''
  name: locationType
  type: string
- container: ''
  name: logo
  type: string
- container: ''
  name: longDisplayDate
  type: string
- container: ''
  name: longName
  type: string
- container: ''
  name: longPhrase
  type: string
- container: ''
  name: longitude
  type: decimal
- container: ''
  name: low
  type: string
- container: ''
  name: lower
  type: string
- container: ''
  name: maximumSustainedWind
  type: string
- container: ''
  name: maximumSustainedWindValue
  type: decimal
- container: ''
  name: maximumWindGust
  type: string
- container: ''
  name: maximumWindGustValue
  type: decimal
- container: ''
  name: medium
  type: string
- container: ''
  name: minimumPressure
  type: string
- container: ''
  name: minute
  type: integer
- container: ''
  name: minuteCastForecast
  type: string
- container: set
  name: minutes
  type: string
- container: ''
  name: network
  type: string
- container: ''
  name: night
  type: string
- container: ''
  name: now
  type: string
- container: ''
  name: numberOfAlerts
  type: integer
- container: ''
  name: offset
  type: string
- container: ''
  name: ortbConfig
  type: string
- container: ''
  name: overallIndex
  type: decimal
- container: ''
  name: overallPlumeLabsIndex
  type: decimal
- container: ''
  name: page
  type: string
- container: set
  name: pageCategories
  type: string
- container: ''
  name: pageUrl
  type: string
- container: ''
  name: params
  type: string
- container: ''
  name: partner
  type: string
- container: ''
  name: past12Hours
  type: string
- container: ''
  name: past18Hours
  type: string
- container: ''
  name: past24Hours
  type: string
- container: ''
  name: past3Hours
  type: string
- container: ''
  name: past6Hours
  type: string
- container: ''
  name: past9Hours
  type: string
- container: ''
  name: pastHour
  type: string
- container: ''
  name: peakPosition
  type: string
- container: ''
  name: phrase
  type: string
- container: ''
  name: platform
  type: string
- container: set
  name: pollutants
  type: string
- container: set
  name: position
  type: decimal
- container: ''
  name: postalCode
  type: string
- container: ''
  name: ppid
  type: string
- container: ''
  name: prebidTimeout
  type: integer
- container: ''
  name: precip
  type: string
- container: ''
  name: precipSummary
  type: string
- container: ''
  name: precipitation
  type: string
- container: ''
  name: precipitationType
  type: string
- container: ''
  name: pressure
  type: string
- container: ''
  name: probability
  type: integer
- container: ''
  name: productQuality
  type: string
- container: ''
  name: publisher
  type: string
- container: ''
  name: rain
  type: string
- container: ''
  name: realFeel
  type: string
- container: ''
  name: realFeelPhrase
  type: string
- container: ''
  name: realFeelShade
  type: string
- container: ''
  name: realFeelShadePhrase
  type: string
- container: ''
  name: realFeelShadeValue
  type: decimal
- container: ''
  name: realFeelValue
  type: decimal
- container: ''
  name: referrer
  type: string
- container: ''
  name: referrerUrl
  type: string
- container: ''
  name: region
  type: string
- container: set
  name: sectionCategories
  type: string
- container: set
  name: segments
  type: string
- container: ''
  name: session
  type: string
- container: ''
  name: shortDateShortTimeLabel
  type: string
- container: ''
  name: shortDayOfWeek
  type: string
- container: ''
  name: siteName
  type: string
- container: ''
  name: slot
  type: string
- container: ''
  name: snow
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: sourceRelationship
  type: string
- container: ''
  name: speed
  type: string
- container: ''
  name: start
  type: dateTime
- container: ''
  name: startDate
  type: dateTime
- container: ''
  name: startEpoch
  type: integer
- container: ''
  name: stationCode
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: statusIcon
  type: string
- container: ''
  name: statusIconString
  type: string
- container: ''
  name: statusName
  type: string
- container: ''
  name: stormLink
  type: string
- container: set
  name: stormPositions
  type: string
- container: ''
  name: summary60
  type: string
- container: set
  name: supportedDataSets
  type: string
- container: ''
  name: supportsEventConfidence
  type: boolean
- container: ''
  name: supportsMinuteCast
  type: boolean
- container: ''
  name: temperature
  type: string
- container: ''
  name: temperatureValue
  type: decimal
- container: ''
  name: term
  type: string
- container: ''
  name: test
  type: string
- container: ''
  name: testVariant
  type: string
- container: ''
  name: throughput
  type: string
- container: ''
  name: thunderstormProbability
  type: string
- container: ''
  name: time
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: unit
  type: string
- container: ''
  name: unitType
  type: integer
- container: ''
  name: updatedStormName
  type: string
- container: ''
  name: upr
  type: decimal
- container: ''
  name: user
  type: string
- container: ''
  name: uspString
  type: string
- container: ''
  name: utm
  type: string
- container: ''
  name: uv
  type: string
- container: ''
  name: value
  type: decimal
- container: ''
  name: version
  type: string
- container: ''
  name: visibility
  type: string
- container: ''
  name: weather
  type: string
- container: ''
  name: wind
  type: string
- container: ''
  name: windDegrees
  type: decimal
- container: ''
  name: windDirection
  type: string
- container: ''
  name: windSpeedImperial
  type: decimal
- container: ''
  name: windValue
  type: decimal
- container: ''
  name: year
  type: integer
property_count: 250
provider_name: AccuWeather
provider_slug: accuweather
slug: accuweather-context
tags:
- Weather
- Forecasts
- Meteorology
- Location Services
- Air Quality
- Storms
- JSON-LD
- Linked Data
- Semantic Web
---
