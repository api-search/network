---
description: A structure containing the identity provider (IdP) metadata used to integrate the identity provider with this workspace. You can specify the metadata either by providing a URL to its location in the <code>url</code> parameter, or by specifying the full metadata in XML format in the <code>xml</code> parameter. Specifying both will cause an error.
layout: schema
name: IdpMetadata
properties_list:
- description: ''
  name: url
  type: object
- description: ''
  name: xml
  type: object
provider_name: Amazon Managed Grafana
provider_slug: amazon-managed-grafana
schema_file: json-schema/amazon-managed-grafana-idp-metadata-schema.json
slug: amazon-managed-grafana-idp-metadata
tags:
- AWS
- Dashboards
- Monitoring
- Observability
- Visualization
title: IdpMetadata
---
