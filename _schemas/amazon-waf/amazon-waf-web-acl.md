---
description: Schema representing an AWS WAF Web ACL (Access Control List) resource.
layout: schema
name: AWS WAF Web ACL
properties_list:
- description: The name of the web ACL.
  name: Name
  type: string
- description: A unique identifier for the web ACL.
  name: Id
  type: string
- description: The Amazon Resource Name (ARN) of the web ACL.
  name: ARN
  type: string
- description: Specifies whether this is for CloudFront or for a regional application.
  name: Scope
  type: string
- description: The action to perform if none of the rules match.
  name: DefaultAction
  type: object
- description: The rules associated with the web ACL.
  name: Rules
  type: array
- description: Defines the CloudWatch metrics and sampling configuration.
  name: VisibilityConfig
  type: object
- description: The web ACL capacity units (WCUs) consumed by this web ACL.
  name: Capacity
  type: integer
- description: A token for optimistic locking.
  name: LockToken
  type: string
- description: Tags associated with the web ACL.
  name: Tags
  type: array
provider_name: Amazon WAF
provider_slug: amazon-waf
schema_file: json-schema/amazon-waf-web-acl-schema.json
slug: amazon-waf-web-acl
tags:
- AWS
- Bot Management
- Ddos Protection
- Security
- WAF
- Web Application Firewall
title: AWS WAF Web ACL
---
