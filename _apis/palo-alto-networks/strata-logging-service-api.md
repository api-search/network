---
aid: palo-alto-networks:strata-logging-service-api
baseURL: https://api.sase.paloaltonetworks.com
description: REST APIs for the Strata Logging Service (formerly Cortex Data Lake) providing log forwarding and query capabilities. The Log Forwarding API manages log forwarding profiles for syslog, HTTPS, and email destinations supporting CSV, LEEF, CEF, JSON, and PARQUET formats with up to 200 syslog destinations per instance. The Query Service API enables programmatic log retrieval and pagination across collected security telemetry data.
humanURL: https://pan.dev/cdl/docs/log-forwarding/
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: Strata Logging Service API
properties:
- type: Documentation
  url: https://pan.dev/cdl/docs/log-forwarding/
- type: ChangeLog
  url: https://pan.dev/cdl/docs/logforwarding/release-notes/relnotes/
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/openapi/palo-alto-strata-logging-service-api-openapi-original.yml
- type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/asyncapi/palo-alto-strata-logging-forwarding-asyncapi-original.yml
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/strata-logging-forwarding-auth-log-payload-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/strata-logging-forwarding-threat-log-payload-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/strata-logging-forwarding-traffic-log-payload-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/strata-logging-forwarding-url-log-payload-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/strata-logging-forwarding-wildfire-log-payload-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/strata-logging-service-api-email-destination-request-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/strata-logging-service-api-email-destination-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/strata-logging-service-api-forwarding-status-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/strata-logging-service-api-https-destination-request-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/strata-logging-service-api-https-destination-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/strata-logging-service-api-log-forwarding-profile-request-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/strata-logging-service-api-log-forwarding-profile-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/strata-logging-service-api-syslog-destination-request-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/strata-logging-service-api-syslog-destination-schema.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/strata-logging-forwarding-auth-log-payload-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/strata-logging-forwarding-threat-log-payload-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/strata-logging-forwarding-traffic-log-payload-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/strata-logging-forwarding-url-log-payload-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/strata-logging-forwarding-wildfire-log-payload-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/strata-logging-service-api-email-destination-request-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/strata-logging-service-api-email-destination-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/strata-logging-service-api-forwarding-status-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/strata-logging-service-api-https-destination-request-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/strata-logging-service-api-https-destination-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/strata-logging-service-api-log-forwarding-profile-request-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/strata-logging-service-api-log-forwarding-profile-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/strata-logging-service-api-syslog-destination-request-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/strata-logging-service-api-syslog-destination-structure.json
- type: JSON-LD
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-strata-logging-forwarding-context.jsonld
- type: JSON-LD
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-strata-logging-service-api-context.jsonld
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/strata-logging-forwarding-auth-log-payload-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/strata-logging-forwarding-threat-log-payload-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/strata-logging-forwarding-traffic-log-payload-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/strata-logging-forwarding-url-log-payload-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/strata-logging-forwarding-wildfire-log-payload-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/strata-logging-service-api-email-destination-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/strata-logging-service-api-email-destination-request-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/strata-logging-service-api-forwarding-status-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/strata-logging-service-api-https-destination-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/strata-logging-service-api-https-destination-request-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/strata-logging-service-api-log-forwarding-profile-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/strata-logging-service-api-log-forwarding-profile-request-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/strata-logging-service-api-syslog-destination-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/strata-logging-service-api-syslog-destination-request-example.json
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: strata-logging-service-api
tags:
- Analytics
- Data Lake
- Log Forwarding
- Logging
- SIEM Integration
---
