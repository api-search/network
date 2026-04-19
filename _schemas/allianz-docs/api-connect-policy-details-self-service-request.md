---
description: Request body for creating a self-service policy completion session
layout: schema
name: PolicyDetailsSelfServiceRequest
properties_list:
- description: Unique identifier of the price estimate to complete
  name: estimate_id
  type: string
- description: URL to redirect customer back to after completing the policy
  name: redirect_url
  type: string
provider_name: Allianz
provider_slug: allianz-docs
schema_file: json-schema/api-connect-policy-details-self-service-request-schema.json
slug: api-connect-policy-details-self-service-request
tags:
- Financial Services
- Insurance
- Asset Management
title: PolicyDetailsSelfServiceRequest
---
