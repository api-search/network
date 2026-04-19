---
categories:
- asyncapi
description: Spectral linting rules defining API design standards and conventions for AMQP.
layout: rules
name: AMQP API Rules
provider_name: AMQP
provider_slug: amqp
rule_count: 9
rules:
- description: AsyncAPI info must have a description
  given: $.info
  name: asyncapi-info-description
  severity: error
- description: AsyncAPI info must have a version
  given: $.info
  name: asyncapi-info-version
  severity: error
- description: At least one server must be defined
  given: $
  name: asyncapi-servers-defined
  severity: warn
- description: Every channel should have a description
  given: $.channels[*]
  name: asyncapi-channel-description
  severity: warn
- description: Every message should have a description
  given: $.components.messages[*]
  name: asyncapi-message-description
  severity: warn
- description: Schema properties should have explicit types
  given: $.components.schemas[*].properties[*]
  name: asyncapi-schema-type
  severity: info
- description: AMQP bindings should define exchange type
  given: $.channels[*].bindings.amqp.exchange
  name: asyncapi-amqp-exchange-type
  severity: info
- description: Operations should have an operationId
  given: $.channels[*].messages[*]
  name: asyncapi-operation-id
  severity: warn
- description: Descriptions must not be empty
  given: $..description
  name: asyncapi-no-empty-description
  severity: warn
rules_file: rules/amqp-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amqp/refs/heads/main/rules/amqp-spectral-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 2
  warn: 5
slug: amqp-spectral-rules
tags:
- AMQP
- Asynchronous
- Message Queue
- Messaging
- Middleware
- Open Standard
- Publish Subscribe
- Spectral
- Linting
- API Governance
---
