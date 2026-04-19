---
description: <p>Override specific listener ports used to route traffic to endpoints that are part of an endpoint group. For example, you can create a port override in which the listener receives user traffic on ports 80 and 443, but your accelerator routes that traffic to ports 1080 and 1443, respectively, on the endpoints.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups-port-override.html"> Overriding listener ports</a> in the <i>Global Accelerator Developer Guide</i>.</p>
layout: schema
name: PortOverride
properties_list:
- description: ''
  name: ListenerPort
  type: object
- description: ''
  name: EndpointPort
  type: object
provider_name: Amazon Global Accelerator
provider_slug: amazon-global-accelerator
schema_file: json-schema/global-accelerator-port-override-schema.json
slug: global-accelerator-port-override
tags:
- Availability
- AWS
- CDN
- Global
- Load Balancing
- Networking
- Performance
title: PortOverride
---
