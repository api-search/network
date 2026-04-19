---
description: Age prediction result for a first name from the Agify.io API.
layout: schema
name: AgePrediction
properties_list:
- description: Number of data points used to make the prediction. Higher count indicates greater confidence.
  name: count
  type: integer
- description: The first name that was evaluated.
  name: name
  type: string
- description: Predicted age for the given name. Null if there is insufficient data for a prediction.
  name: age
  type: integer
- description: The ISO 3166-1 alpha-2 country code used for localization, if provided in the request.
  name: country_id
  type: string
provider_name: Agify.io
provider_slug: agify-io
schema_file: json-schema/agify-io-age-prediction-schema.json
slug: agify-io-age-prediction
tags:
- Age Prediction
- Name Analysis
- Demographics
- REST API
title: AgePrediction
---
