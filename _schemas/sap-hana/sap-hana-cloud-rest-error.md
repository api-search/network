---
description: Standard error response returned by the SAP HANA Cloud REST API when a request fails.
layout: schema
name: Error
properties_list:
- description: The error code identifying the type of error.
  name: error
  type: string
- description: A human-readable description of the error.
  name: description
  type: string
- description: The HTTP status code associated with the error.
  name: statusCode
  type: integer
provider_name: SAP HANA
provider_slug: sap-hana
schema_file: json-schema/sap-hana-cloud-rest-error-schema.json
slug: sap-hana-cloud-rest-error
tags:
- Analytics
- Cloud
- Database
- Enterprise
- In-Memory
title: Error
---
