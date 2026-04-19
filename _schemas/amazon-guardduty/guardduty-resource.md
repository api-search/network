---
description: Contains information about the Amazon Web Services resource associated with the activity that prompted GuardDuty to generate a finding.
layout: schema
name: Resource
properties_list:
- description: ''
  name: AccessKeyDetails
  type: object
- description: ''
  name: S3BucketDetails
  type: object
- description: ''
  name: InstanceDetails
  type: object
- description: ''
  name: EksClusterDetails
  type: object
- description: ''
  name: KubernetesDetails
  type: object
- description: ''
  name: ResourceType
  type: object
- description: ''
  name: EbsVolumeDetails
  type: object
- description: ''
  name: EcsClusterDetails
  type: object
- description: ''
  name: ContainerDetails
  type: object
- description: ''
  name: RdsDbInstanceDetails
  type: object
- description: ''
  name: RdsDbUserDetails
  type: object
- description: ''
  name: LambdaDetails
  type: object
provider_name: Amazon GuardDuty
provider_slug: amazon-guardduty
schema_file: json-schema/guardduty-resource-schema.json
slug: guardduty-resource
tags:
- Anomaly Detection
- AWS
- Compliance
- Machine Learning
- Monitoring
- Security
- Threat Detection
title: Resource
---
