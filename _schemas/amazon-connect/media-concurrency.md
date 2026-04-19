---
description: Contains information about which channels are supported, and how many contacts an agent can have on a channel simultaneously.
layout: schema
name: MediaConcurrency
properties_list:
- description: The channels that agents can handle in the Contact Control Panel (CCP).
  name: Channel
  type: string
- description: The number of contacts an agent can have on a channel simultaneously.
  name: Concurrency
  type: integer
provider_name: Amazon Connect
provider_slug: amazon-connect
schema_file: json-schema/media-concurrency-schema.json
slug: media-concurrency
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
title: MediaConcurrency
---
