---
description: <p>Specifies which resource types Config records for configuration changes. In the recording group, you specify whether you want to record all supported resource types or to include or exclude specific types of resources.</p> <p>By default, Config records configuration changes for all supported types of <i>Regional resources</i> that Config discovers in the Amazon Web Services Region in which it is running. Regional resources are tied to a Region and can be used only in that Region. Examples of Regional resources are Amazon EC2 instances and Amazon EBS volumes.</p> <p>You can also have Config record supported types of <i>global resources</i>. Global resources are not tied to a specific Region and can be used in all Regions. The global resource types that Config supports include IAM users, groups, roles, and customer managed policies.</p> <important> <p>Global resource types onboarded to Config recording after February 2022 will be recorded only in the service's home Region for
  the commercial partition and Amazon Web Services GovCloud (US-West) for the Amazon Web Services GovCloud (US) partition. You can view the Configuration Items for these new global resource types only in their home Region and Amazon Web Services GovCloud (US-West).</p> </important> <p>If you don't want Config to record all resources, you can specify which types of resources Config records with the <code>resourceTypes</code> parameter.</p> <p>For a list of supported resource types, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources">Supported Resource Types</a> in the <i>Config developer guide</i>.</p> <p>For more information and a table of the Home Regions for Global Resource Types Onboarded after February 2022, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html">Selecting Which Resources Config Records</a> in the <i>Config developer guide</i>.</p>
layout: schema
name: RecordingGroup
properties_list:
- description: ''
  name: allSupported
  type: object
- description: ''
  name: includeGlobalResourceTypes
  type: object
- description: ''
  name: resourceTypes
  type: object
- description: ''
  name: exclusionByResourceTypes
  type: object
- description: ''
  name: recordingStrategy
  type: object
provider_name: Amazon Config
provider_slug: amazon-config
schema_file: json-schema/config-recording-group-schema.json
slug: config-recording-group
tags:
- Auditing
- AWS
- Compliance
- Configuration Management
- Governance
- Security
title: RecordingGroup
---
