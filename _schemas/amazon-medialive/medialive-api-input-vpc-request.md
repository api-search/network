---
description: Settings for a private VPC Input. When this property is specified, the input destination addresses will be created in a VPC rather than with public Internet addresses. This property requires setting the roleArn property on Input creation. Not compatible with the inputSecurityGroups property.
layout: schema
name: InputVpcRequest
properties_list:
- description: ''
  name: SecurityGroupIds
  type: object
- description: ''
  name: SubnetIds
  type: object
provider_name: Amazon MediaLive
provider_slug: amazon-medialive
schema_file: json-schema/medialive-api-input-vpc-request-schema.json
slug: medialive-api-input-vpc-request
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: InputVpcRequest
---
