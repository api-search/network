---
description: ''
layout: schema
name: DescribeAlarmsInput
properties_list:
- description: The names of the alarms to retrieve information about.
  name: AlarmNames
  type: array
- description: An alarm name prefix. If specified, only alarms with names that start with this prefix are returned.
  name: AlarmNamePrefix
  type: string
- description: Specify this parameter to receive information only about alarms of the specified types.
  name: AlarmTypes
  type: array
- description: If you use this parameter and specify the name of a composite alarm, the operation returns information about the child alarms.
  name: ChildrenOfAlarmName
  type: string
- description: If you use this parameter and specify the name of a metric alarm, the operation returns information about the composite alarms that reference it.
  name: ParentsOfAlarmName
  type: string
- description: Use this parameter to filter the results to only those alarms that use a certain alarm action.
  name: ActionPrefix
  type: string
- description: The maximum number of alarm descriptions to retrieve.
  name: MaxRecords
  type: integer
- description: The token returned by a previous call to indicate there is more data available.
  name: NextToken
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-describe-alarms-input-schema.json
slug: cloudwatch-describe-alarms-input
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: DescribeAlarmsInput
---
