---
description: Schema representing an AWS Shield protection resource. A protection enables AWS Shield Advanced DDoS protection for a specific AWS resource such as an Elastic IP, CloudFront distribution, or Application Load Balancer.
layout: schema
name: Amazon Shield Protection
properties_list:
- description: The unique identifier (ID) of the protection.
  name: Id
  type: string
- description: The name of the protection.
  name: Name
  type: string
- description: The ARN of the AWS resource that is protected.
  name: ResourceArn
  type: string
- description: The ARN of the protection.
  name: ProtectionArn
  type: string
- description: The unique identifiers for the health check associations.
  name: HealthCheckIds
  type: array
- description: ''
  name: ApplicationLayerAutomaticResponseConfiguration
  type: object
- description: Tags associated with the protection.
  name: Tags
  type: array
provider_name: Amazon Shield
provider_slug: amazon-shield
schema_file: json-schema/amazon-shield-protection-schema.json
slug: amazon-shield-protection
tags:
- AWS
- DDoS Protection
- Networking
- Security
title: Amazon Shield Protection
---
