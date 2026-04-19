---
consumed_apis:
- cloudflare-dns
- cloudflare-turnstile
- cloudflare-logpush
description: DNS management and web security combining DNS record management with Turnstile bot protection and Logpush observability. Used by site reliability engineers and security teams.
layout: capability
name: Cloudflare DNS and Security
operations:
- description: List DNS records.
  method: GET
  name: list-dns-records
  path: /v1/dns-records
- description: List Turnstile widgets.
  method: GET
  name: list-turnstile-widgets
  path: /v1/turnstile-widgets
- description: List Logpush jobs.
  method: GET
  name: list-logpush-jobs
  path: /v1/logpush-jobs
personas: []
provider_name: Cloudflare
provider_slug: cloudflare
search_terms:
- object storage
- turnstile widget management.
- logpush job management.
- dns list records
- logpush delete job
- logpush get job
- containers
- artificial intelligence
- list dns records
- create a dns record.
- delete a dns record.
- web performance
- security
- cloudflare
- turnstile list widgets
- turnstile create widget
- turnstile delete widget
- edge computing
- observability
- platform
- create a turnstile widget.
- dns record management.
- dns update record
- list logpush jobs
- get dnssec settings.
- update a dns record.
- real-time communication
- logpush list dataset fields
- list logpush jobs.
- dns
- dns batch records
- list dns records.
- dns create record
- list turnstile widgets
- edge
- serverless
- dns delete record
- dns get dnssec
- delete a turnstile widget.
- verify a turnstile token.
- cloud
- list dataset fields.
- api gateway
- dns get record
- create a logpush job.
- cdn
- get dns record details.
- turnstile verify token
- list turnstile widgets.
- logpush list jobs
- ai gateway
- logpush create job
- execute batch dns operations.
- list dns records for a zone.
- ddos protection
- get logpush job details.
- delete a logpush job.
slug: dns-and-security
tags:
- Cloudflare
- DNS
- Security
- Observability
tools:
- description: List DNS records for a zone.
  hints:
    openWorld: true
    readOnly: true
  name: dns-list-records
- description: Create a DNS record.
  hints:
    readOnly: false
  name: dns-create-record
- description: Get DNS record details.
  hints:
    readOnly: true
  name: dns-get-record
- description: Update a DNS record.
  hints:
    idempotent: true
    readOnly: false
  name: dns-update-record
- description: Delete a DNS record.
  hints:
    destructive: true
    idempotent: true
  name: dns-delete-record
- description: Execute batch DNS operations.
  hints:
    readOnly: false
  name: dns-batch-records
- description: Get DNSSEC settings.
  hints:
    readOnly: true
  name: dns-get-dnssec
- description: List Turnstile widgets.
  hints:
    openWorld: true
    readOnly: true
  name: turnstile-list-widgets
- description: Create a Turnstile widget.
  hints:
    readOnly: false
  name: turnstile-create-widget
- description: Verify a Turnstile token.
  hints:
    readOnly: true
  name: turnstile-verify-token
- description: Delete a Turnstile widget.
  hints:
    destructive: true
    idempotent: true
  name: turnstile-delete-widget
- description: List Logpush jobs.
  hints:
    openWorld: true
    readOnly: true
  name: logpush-list-jobs
- description: Create a Logpush job.
  hints:
    readOnly: false
  name: logpush-create-job
- description: Get Logpush job details.
  hints:
    readOnly: true
  name: logpush-get-job
- description: Delete a Logpush job.
  hints:
    destructive: true
    idempotent: true
  name: logpush-delete-job
- description: List dataset fields.
  hints:
    readOnly: true
  name: logpush-list-dataset-fields
---
