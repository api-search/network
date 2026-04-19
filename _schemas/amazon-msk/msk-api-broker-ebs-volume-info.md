---
description: <p>Specifies the EBS volume upgrade information. The broker identifier must be set to the keyword ALL. This means the changes apply to all the brokers in the cluster.</p>
layout: schema
name: BrokerEBSVolumeInfo
properties_list:
- description: ''
  name: KafkaBrokerNodeId
  type: object
- description: ''
  name: ProvisionedThroughput
  type: object
- description: ''
  name: VolumeSizeGB
  type: object
provider_name: Amazon MSK
provider_slug: amazon-msk
schema_file: json-schema/msk-api-broker-ebs-volume-info-schema.json
slug: msk-api-broker-ebs-volume-info
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: BrokerEBSVolumeInfo
---
