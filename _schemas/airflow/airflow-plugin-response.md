---
description: Plugin serializer.
layout: schema
name: PluginResponse
properties_list:
- description: ''
  name: name
  type: string
- description: ''
  name: macros
  type: array
- description: ''
  name: flask_blueprints
  type: array
- description: ''
  name: fastapi_apps
  type: array
- description: ''
  name: fastapi_root_middlewares
  type: array
- description: Aggregate all external views. Both 'external_views' and 'appbuilder_menu_items' are included here.
  name: external_views
  type: array
- description: ''
  name: react_apps
  type: array
- description: ''
  name: appbuilder_views
  type: array
- description: ''
  name: appbuilder_menu_items
  type: array
- description: ''
  name: global_operator_extra_links
  type: array
- description: ''
  name: operator_extra_links
  type: array
- description: ''
  name: source
  type: string
- description: ''
  name: listeners
  type: array
- description: ''
  name: timetables
  type: array
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-plugin-response-schema.json
slug: airflow-plugin-response
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: PluginResponse
---
