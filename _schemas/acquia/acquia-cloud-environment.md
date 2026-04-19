---
description: environment schema from Acquia Cloud API
layout: schema
name: Environment
properties_list:
- description: The ID of the environment. The ID is a compound key consisting of the internal database ID of the environment and the application UUID.
  name: id
  type: string
- description: The human-readable name of the environment.
  name: label
  type: string
- description: The stage name of the environment.
  name: name
  type: string
- description: ''
  name: application
  type: object
- description: An array of domain names attached to this environment.
  name: domains
  type: array
- description: The active domain name for this environment.
  name: active_domain
  type: string
- description: The default domain name for this environment.
  name: default_domain
  type: string
- description: The URL to the image for this environment.
  name: image_url
  type: string
- description: The URL used to SSH into the environment.
  name: ssh_url
  type: string
- description: An array of IP addresses attached to this environment.
  name: ips
  type: array
- description: The region the environment resides in.
  name: region
  type: string
- description: 'The balancer type. - balancers: The environment is behind a Legacy balancer. - elb: The environment is behind an ELB balancer. - cluster: The environment is behind an Edge Cluster balancer.'
  name: balancer
  type: string
- description: 'The platform type. - cloud: The environment is hosted on a Cloud Classic Platform. - cloud-next: The environment is hosted on a Cloud Next Platform. - unknown: The host information is not available fo'
  name: platform
  type: string
- description: The status of this environment.
  name: status
  type: string
- description: 'The type of environment. - node: A NodeJS environment. - drupal: A Drupal environment. - ssg: A Static Site Generator environment. - unknown: We were unable to determine the environment type.'
  name: type
  type: string
- description: The size of the environment. Will be null if the environment type does not support sizes.
  name: size
  type: string
- description: The environment weight for display purposes.
  name: weight
  type: integer
- description: ''
  name: vcs
  type: object
- description: ''
  name: flags
  type: object
- description: A collection of environment configuration information.
  name: configuration
  type: object
- description: ''
  name: artifact
  type: object
- description: ''
  name: _links
  type: object
provider_name: Acquia
provider_slug: acquia
schema_file: json-schema/acquia-cloud-environment-schema.json
slug: acquia-cloud-environment
tags:
- Content
- Experience
title: Environment
---
