---
description: The traffic-shifting configuration of a Lambda function alias. Used for weighted alias routing to enable canary deployments.
layout: schema
name: AliasRoutingConfiguration
properties_list:
- description: The secondary version weight. The key is the version number or alias name and the value is the percentage of traffic (0.0-1.0).
  name: AdditionalVersionWeights
  type: object
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-alias-routing-configuration-schema.json
slug: aws-lambda-alias-routing-configuration
tags: []
title: AliasRoutingConfiguration
---
