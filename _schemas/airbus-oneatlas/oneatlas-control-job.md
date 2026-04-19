---
description: ''
layout: schema
name: ControlJob
properties_list:
- description: ''
  name: description
  type: string
- description: The control priority. The highest priority is 1.
  name: priority
  type: number
- description: The control steps to validate in order to complete control.
  name: steps
  type: array
provider_name: Airbus OneAtlas
provider_slug: airbus-oneatlas
schema_file: json-schema/oneatlas-control-job-schema.json
slug: oneatlas-control-job
tags:
- Imagery
- Satellites
title: ControlJob
---
