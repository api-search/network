---
description: AcceptTermsOfServiceRequest schema from Adyen API
layout: schema
name: AcceptTermsOfServiceRequest
properties_list:
- description: The legal entity ID of the user accepting the Terms of Service. For organizations, this must be the individual legal entity ID of an authorized signatory for the organization. For sole proprietorships
  name: acceptedBy
  type: string
- description: The IP address of the user accepting the Terms of Service.
  name: ipAddress
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-accept-terms-of-service-request-schema.json
slug: legal-entity-accept-terms-of-service-request
tags:
- Payments
- Financial Services
- Fintech
title: AcceptTermsOfServiceRequest
---
