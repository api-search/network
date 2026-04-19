---
description: <p>Contains information about a deployment's policy that defines when components are safe to update.</p> <p>Each component on a device can report whether or not it's ready to update. After a component and its dependencies are ready, they can apply the update in the deployment. You can configure whether or not the deployment notifies components of an update and waits for a response. You specify the amount of time each component has to respond to the update notification.</p>
layout: schema
name: DeploymentComponentUpdatePolicy
properties_list:
- description: ''
  name: timeoutInSeconds
  type: object
- description: ''
  name: action
  type: object
provider_name: Amazon IoT Greengrass
provider_slug: amazon-iot-greengrass
schema_file: json-schema/iot-greengrass-deployment-component-update-policy-schema.json
slug: iot-greengrass-deployment-component-update-policy
tags:
- AWS
- Edge Computing
- IoT
- Lambda
- Machine Learning
- Real-Time Processing
title: DeploymentComponentUpdatePolicy
---
