---
description: <p>Contains criteria that define when and how to cancel a job.</p> <p>The deployment stops if the following conditions are true:</p> <ol> <li> <p>The number of things that receive the deployment exceeds the <code>minNumberOfExecutedThings</code>.</p> </li> <li> <p>The percentage of failures with type <code>failureType</code> exceeds the <code>thresholdPercentage</code>.</p> </li> </ol>
layout: schema
name: IoTJobAbortCriteria
properties_list:
- description: ''
  name: failureType
  type: object
- description: ''
  name: action
  type: object
- description: ''
  name: thresholdPercentage
  type: object
- description: ''
  name: minNumberOfExecutedThings
  type: object
provider_name: Amazon IoT Greengrass
provider_slug: amazon-iot-greengrass
schema_file: json-schema/iot-greengrass-io-t-job-abort-criteria-schema.json
slug: iot-greengrass-io-t-job-abort-criteria
tags:
- AWS
- Edge Computing
- IoT
- Lambda
- Machine Learning
- Real-Time Processing
title: IoTJobAbortCriteria
---
