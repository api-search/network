---
description: ModifyVpcEndpointServicePermissionsRequest schema from Amazon PrivateLink API
layout: schema
name: ModifyVpcEndpointServicePermissionsRequest
properties_list:
- description: ID of the endpoint service
  name: ServiceId
  type: string
- description: Principal ARNs to allow
  name: AddAllowedPrincipals
  type: array
- description: Principal ARNs to remove
  name: RemoveAllowedPrincipals
  type: array
provider_name: Amazon PrivateLink
provider_slug: amazon-privatelink
schema_file: json-schema/amazon-privatelink-modify-vpc-endpoint-service-permissions-request-schema.json
slug: amazon-privatelink-modify-vpc-endpoint-service-permissions-request
tags:
- AWS
- Networking
- Private Connectivity
- Security
- VPC
- Zero Trust
- Endpoint Services
title: ModifyVpcEndpointServicePermissionsRequest
---
