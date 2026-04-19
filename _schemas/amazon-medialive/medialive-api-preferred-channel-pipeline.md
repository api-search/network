---
description: Indicates which pipeline is preferred by the multiplex for program ingest. If set to \"PIPELINE_0\" or \"PIPELINE_1\" and an unhealthy ingest causes the multiplex to switch to the non-preferred pipeline, it will switch back once that ingest is healthy again. If set to \"CURRENTLY_ACTIVE\", it will not switch back to the other pipeline based on it recovering to a healthy state, it will only switch if the active pipeline becomes unhealthy.
layout: schema
name: PreferredChannelPipeline
properties_list: []
provider_name: Amazon MediaLive
provider_slug: amazon-medialive
schema_file: json-schema/medialive-api-preferred-channel-pipeline-schema.json
slug: medialive-api-preferred-channel-pipeline
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: PreferredChannelPipeline
---
