---
description: ''
layout: schema
name: band
properties_list:
- description: cf ABPP de NITF
  name: actualBitDepth
  type: number
- description: possible values one of `RED`, `GREEN`, `BLUE`, `GRAY`, `ALPHA` or a custom string (ex `NIR`)
  name: colorInterpretation
  type: string
- description: TO BE DISCUSSED (raw, deflate,...)
  name: compression
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: isMask
  type: boolean
- description: 'The name of the **mask bands** are normalized as: - `CLD` for Cloud Cotation - `COR` for Correlation - `DET` for Detector Quality - `EXO` for Exogenous mask - `MER` for Dem merging mask - `QTE` for Te'
  name: name
  type: string
- description: the value of a pixel that does not correspond to a real data
  name: noDataValue
  type: number
- description: offset used in the buffer for this band
  name: offset
  type: number
- description: the type of pixel of the buffer
  name: pixelType
  type: string
- description: size of this band in the buffer
  name: size
  type: number
provider_name: Airbus OneAtlas
provider_slug: airbus-oneatlas
schema_file: json-schema/oneatlas-band-schema.json
slug: oneatlas-band
tags:
- Imagery
- Satellites
title: band
---
