---
description: Specifies service specification with a stage file.
layout: schema
name: ServiceSpecStageFile
properties_list:
- description: Specifies the Snowflake internal stage where the specification file is stored; for example, @tutorial_stage.
  name: stage
  type: string
- description: Specifies the path to the service specification file on the stage; for example, 'some-dir/echo_spec.yaml'.
  name: spec_file
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/service-service-spec-stage-file-schema.json
slug: service-service-spec-stage-file
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: ServiceSpecStageFile
---
