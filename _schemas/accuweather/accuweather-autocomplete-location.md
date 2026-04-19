---
description: A location that can be used to plot on a map.
layout: schema
name: AutocompleteLocation
properties_list:
- description: Type of location, eg. address or postalcode
  name: locationType
  type: string
- description: City name of the location, usually used for display purposes when sourcing weather data.
  name: city
  type: string
- description: The admin code for the location.
  name: adminCode
  type: string
- description: County code for the location.
  name: countryCode
  type: string
- description: Postal Code of the location, usually used for display purposes when sourcing weather data.
  name: postalCode
  type: string
- description: City name of the location, usually used for display purposes when sourcing weather data.
  name: position
  type: array
- description: Editable name of the location to display to the user.
  name: name
  type: string
- description: Longer name of the location to display to the user, typically the full address.
  name: longName
  type: string
- description: Detailed keys for the location from AccuWeather to aid in weather data retrieval.
  name: locationSettingsInfo
  type: object
- description: The parent provider of the location.
  name: source
  type: string
provider_name: AccuWeather
provider_slug: accuweather
schema_file: json-schema/accuweather-autocomplete-location-schema.json
slug: accuweather-autocomplete-location
tags:
- Weather
- Forecasts
- Meteorology
- Location Services
- Air Quality
- Storms
title: AutocompleteLocation
---
