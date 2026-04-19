---
description: <p>Contains all error-related information for the deployment record. The status details will be null if the deployment is in a success state.</p> <note> <p>Greengrass nucleus v2.8.0 or later is required to get an accurate <code>errorStack</code> and <code>errorTypes</code> response. This field will not be returned for earlier Greengrass nucleus versions.</p> </note>
layout: schema
name: EffectiveDeploymentStatusDetails
properties_list:
- description: ''
  name: errorStack
  type: object
- description: ''
  name: errorTypes
  type: object
provider_name: Amazon IoT Greengrass
provider_slug: amazon-iot-greengrass
schema_file: json-schema/iot-greengrass-effective-deployment-status-details-schema.json
slug: iot-greengrass-effective-deployment-status-details
tags:
- AWS
- Edge Computing
- IoT
- Lambda
- Machine Learning
- Real-Time Processing
title: EffectiveDeploymentStatusDetails
---
