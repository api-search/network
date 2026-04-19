---
description: <p>If a service instance is manually updated, Proton wants to prevent accidentally overriding a manual change.</p> <p>A blocker is created because of the manual update or deletion of a service instance. The summary describes the blocker as being active or resolved.</p>
layout: schema
name: ServiceSyncBlockerSummary
properties_list:
- description: ''
  name: latestBlockers
  type: object
- description: ''
  name: serviceInstanceName
  type: object
- description: ''
  name: serviceName
  type: object
provider_name: Amazon Proton
provider_slug: amazon-proton
schema_file: json-schema/amazon-proton-service-sync-blocker-summary-schema.json
slug: amazon-proton-service-sync-blocker-summary
tags:
- AWS
- DevOps
- Infrastructure as Code
- Platform Engineering
- Serverless
- Templates
- Self-Service
- CI/CD
title: ServiceSyncBlockerSummary
---
