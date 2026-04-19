---
class_count: 10
classes:
- GetMetricDataResponse
- GetMetricStatisticsResponse
- ListMetricsResponse
- DescribeAlarmsResponse
- PutDashboardResponse
- GetDashboardResponse
- ListDashboardsResponse
- Metric
- Alarm
- Dashboard
context_file: json-ld/amazon-cloudwatch-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-cloudwatch/refs/heads/main/json-ld/amazon-cloudwatch-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Cloudwatch from Amazon CloudWatch.
layout: jsonld
name: Amazon Cloudwatch Context
namespaces:
- prefix: cloudwatch
  uri: https://aws.amazon.com/cloudwatch/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: set
  name: metricDataResults
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: label
  type: string
- container: set
  name: datapoints
  type: string
- container: set
  name: metrics
  type: string
- container: set
  name: metricAlarms
  type: string
- container: set
  name: dashboardValidationMessages
  type: string
- container: ''
  name: dashboardArn
  type: string
- container: ''
  name: dashboardBody
  type: string
- container: ''
  name: dashboardName
  type: string
- container: set
  name: dashboardEntries
  type: string
- container: ''
  name: namespace
  type: string
- container: ''
  name: metricName
  type: string
- container: set
  name: dimensions
  type: string
- container: ''
  name: alarmName
  type: string
- container: ''
  name: alarmArn
  type: string
- container: ''
  name: alarmDescription
  type: string
- container: ''
  name: stateValue
  type: string
- container: ''
  name: stateReason
  type: string
- container: ''
  name: stateUpdatedTimestamp
  type: dateTime
- container: ''
  name: statistic
  type: string
- container: ''
  name: period
  type: integer
- container: ''
  name: evaluationPeriods
  type: integer
- container: ''
  name: threshold
  type: decimal
- container: ''
  name: comparisonOperator
  type: string
- container: ''
  name: treatMissingData
  type: string
- container: ''
  name: actionsEnabled
  type: boolean
- container: set
  name: alarmActions
  type: string
- container: set
  name: okActions
  type: string
- container: set
  name: insufficientDataActions
  type: string
- container: ''
  name: lastModified
  type: dateTime
- container: ''
  name: size
  type: integer
property_count: 32
provider_name: Amazon CloudWatch
provider_slug: amazon-cloudwatch
slug: amazon-cloudwatch-context
tags:
- AWS
- CloudWatch
- Monitoring
- Observability
- Metrics
- Logs
- JSON-LD
- Linked Data
- Semantic Web
---
