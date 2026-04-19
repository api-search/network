---
description: Determines whether a TLS/SSL certificate is generated for a fleet. This feature must be enabled when creating the fleet. All instances in a fleet share the same certificate. The certificate can be retrieved by calling the <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk.html">Amazon GameLift Server SDK</a> operation <code>GetInstanceCertificate</code>.
layout: schema
name: CertificateConfiguration
properties_list:
- description: ''
  name: CertificateType
  type: object
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
schema_file: json-schema/gamelift-certificate-configuration-schema.json
slug: gamelift-certificate-configuration
tags:
- AWS
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
title: CertificateConfiguration
---
