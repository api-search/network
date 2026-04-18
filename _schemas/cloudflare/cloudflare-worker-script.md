---
description: A Worker script object from the Cloudflare API, representing serverless code deployed to Cloudflare's global edge network with associated configuration, bindings, and deployment metadata.
layout: schema
name: Cloudflare Worker Script
properties_list:
- description: The unique identifier of the Worker script, typically the script name.
  name: id
  type: string
- description: A unique tag for the Worker script used for caching and versioning.
  name: tag
  type: string
- description: The entity tag for cache validation.
  name: etag
  type: string
- description: List of event handlers the Worker implements (e.g., fetch, scheduled, queue).
  name: handlers
  type: array
- description: Named handlers for Durable Objects and other named event handling.
  name: named_handlers
  type: array
- description: The compatibility date for the Worker runtime.
  name: compatibility_date
  type: string
- description: Compatibility flags enabled for the Worker.
  name: compatibility_flags
  type: array
- description: The usage model for billing.
  name: usage_model
  type: string
- description: Environment bindings configured for the Worker.
  name: bindings
  type: array
- description: Routes that trigger this Worker.
  name: routes
  type: array
- description: Whether Logpush is enabled for the Worker.
  name: logpush
  type: boolean
- description: Smart placement configuration.
  name: placement
  type: object
- description: Workers that receive tail events from this Worker.
  name: tail_consumers
  type: array
- description: When the Worker script was created.
  name: created_on
  type: string
- description: When the Worker script was last modified.
  name: modified_on
  type: string
provider_name: Cloudflare
provider_slug: cloudflare
schema_file: json-schema/cloudflare-worker-script-schema.json
slug: cloudflare-worker-script
tags:
- AI Gateway
- API Gateway
- Artificial Intelligence
- CDN
- Cloud
- Containers
- DDoS Protection
- DNS
- Edge
- Edge Computing
- Object Storage
- Platform
- Real-Time Communication
- Security
- Serverless
- Web Performance
title: Cloudflare Worker Script
---
