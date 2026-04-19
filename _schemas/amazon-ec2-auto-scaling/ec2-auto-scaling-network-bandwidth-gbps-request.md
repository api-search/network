---
description: <p>Specifies the minimum and maximum for the <code>NetworkBandwidthGbps</code> object when you specify <a>InstanceRequirements</a> for an Auto Scaling group.</p> <note> <p>Setting the minimum bandwidth does not guarantee that your instance will achieve the minimum bandwidth. Amazon EC2 will identify instance types that support the specified minimum bandwidth, but the actual bandwidth of your instance might go below the specified minimum at times. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html#available-instance-bandwidth">Available instance bandwidth</a> in the <i>Amazon EC2 User Guide for Linux Instances</i>.</p> </note>
layout: schema
name: NetworkBandwidthGbpsRequest
properties_list:
- description: ''
  name: Min
  type: object
- description: ''
  name: Max
  type: object
provider_name: Amazon EC2 Auto Scaling
provider_slug: amazon-ec2-auto-scaling
schema_file: json-schema/ec2-auto-scaling-network-bandwidth-gbps-request-schema.json
slug: ec2-auto-scaling-network-bandwidth-gbps-request
tags:
- Amazon Web Services
- Auto Scaling
- AWS
- Compute
- EC2
- High Availability
- Scaling
title: NetworkBandwidthGbpsRequest
---
