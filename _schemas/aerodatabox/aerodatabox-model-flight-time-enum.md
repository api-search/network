---
description: 'Models of calculating the flight time.<p>Possible values:</p> <ul> <li><b>0 - Standard</b>: Standard model of calculation which takes into account the great circle distance and the average speed of all aircraft typically operating on those distances.</li> <li><b>1 - ML01</b>: Experimental machine learning (ML) model, which attempts to provide more accurate prediction of the flight time by taking into account the history of flights on specified route and aircraft type within the recent year. This may come in handy in case when on certain routes flights take significant detours due to extended airspace closures dictated by war conflicts, sanction regulations, etc. This can result in significantly increased flight times comparing to regular estimations. Or, some routes generally experience longer delays than other routes of the same distance. This model attempts to take such factors into account and reflect it in the prediction. If a model cannot be applied due to lack of historical
  and/or aircraft data or prediction is too off set, it automatically fallbacks to `Standard`.</li> </ul>'
layout: schema
name: ModelFlightTimeEnum
properties_list: []
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-model-flight-time-enum-schema.json
slug: aerodatabox-model-flight-time-enum
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: ModelFlightTimeEnum
---
