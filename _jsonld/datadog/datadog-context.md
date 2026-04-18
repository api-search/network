---
class_count: 60
classes:
- APIErrorResponse
- APIKeyCreateAttributes
- APIKeyCreateData
- APIKeyCreateRequest
- APIKeyRelationships
- APIKeyResponse
- APIKeyUpdateAttributes
- APIKeyUpdateData
- APIKeyUpdateRequest
- Creator
- Datadog Event
- Datadog Log Event
- Datadog Metric Series
- Datadog Monitor
- DeletedMonitor
- Event
- EventAttributes
- EventCreateAttributes
- EventCreateRequest
- EventCreateResponse
- EventResponse
- EventsListResponse
- EventsSearchRequest
- HTTPLogItem
- Incident
- IncidentAttributes
- IncidentCreateAttributes
- IncidentCreateRequest
- IncidentResponse
- IncidentTeamCreateRequest
- IncidentTeamUpdateRequest
- IncidentUpdateAttributes
- IncidentUpdateRequest
- IncidentsResponse
- IntakePayloadAccepted
- Log
- LogAttributes
- LogsAggregateRequest
- LogsCompute
- LogsGroupBy
- LogsListRequest
- LogsListResponse
- LogsQueryFilter
- MetricPayload
- MetricPoint
- MetricQueryDefinition
- MetricResource
- MetricSeries
- MetricTimeseriesQuery
- MetricTimeseriesResponse
- Monitor
- MonitorGroupState
- MonitorMuteSettings
- MonitorOptions
- MonitorState
- MonitorThresholds
- MonitorUnmuteSettings
- MonitorUpdateRequest
- QueryFormula
- TimeseriesResult
context_file: json-ld/datadog-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/datadog/refs/heads/main/json-ld/datadog-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Datadog from Datadog.
layout: jsonld
name: Datadog Context
namespaces:
- prefix: dd
  uri: https://docs.datadoghq.com/api/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: aggregation
  type: string
- container: ''
  name: aggregation_key
  type: string
- container: ''
  name: alert_type
  type: string
- container: ''
  name: alias
  type: string
- container: ''
  name: all_scopes
  type: boolean
- container: ''
  name: attributes
  type: string
- container: ''
  name: category
  type: string
- container: set
  name: compute
  type: string
- container: ''
  name: content
  type: string
- container: ''
  name: created
  type: dateTime
- container: ''
  name: created_by
  type: string
- container: ''
  name: creator
  type: string
- container: ''
  name: critical
  type: string
- container: ''
  name: critical_recovery
  type: string
- container: ''
  name: customer_impact_duration
  type: integer
- container: ''
  name: customer_impact_end
  type: dateTime
- container: ''
  name: customer_impact_scope
  type: string
- container: ''
  name: customer_impact_start
  type: dateTime
- container: ''
  name: customer_impacted
  type: boolean
- container: ''
  name: data
  type: string
- container: ''
  name: data_source
  type: string
- container: ''
  name: ddsource
  type: string
- container: ''
  name: ddtags
  type: string
- container: ''
  name: deleted
  type: dateTime
- container: ''
  name: deleted_monitor_id
  type: string
- container: ''
  name: detected
  type: dateTime
- container: ''
  name: email
  type: string
- container: ''
  name: end
  type: string
- container: set
  name: errors
  type: string
- container: ''
  name: escalation_message
  type: string
- container: ''
  name: evaluation_delay
  type: integer
- container: ''
  name: event_id
  type: string
- container: ''
  name: facet
  type: string
- container: ''
  name: fields
  type: reference
- container: ''
  name: filter
  type: reference
- container: ''
  name: formula
  type: string
- container: ''
  name: from
  type: string
- container: set
  name: group_by
  type: string
- container: set
  name: group_tags
  type: string
- container: ''
  name: groups
  type: reference
- container: ''
  name: handle
  type: string
- container: ''
  name: host
  type: string
- container: ''
  name: hostname
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: include_tags
  type: boolean
- container: set
  name: included
  type: string
- container: set
  name: indexes
  type: string
- container: ''
  name: interval
  type: string
- container: ''
  name: last_notified_ts
  type: string
- container: ''
  name: last_resolved_ts
  type: string
- container: ''
  name: last_triggered_ts
  type: string
- container: ''
  name: limit
  type: integer
- container: ''
  name: links
  type: reference
- container: ''
  name: message
  type: string
- container: ''
  name: meta
  type: reference
- container: ''
  name: metric
  type: string
- container: ''
  name: modified
  type: dateTime
- container: ''
  name: modified_by
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: new_group_delay
  type: integer
- container: ''
  name: no_data_timeframe
  type: integer
- container: set
  name: notification_handles
  type: string
- container: ''
  name: notify_audit
  type: boolean
- container: ''
  name: notify_no_data
  type: boolean
- container: ''
  name: ok
  type: string
- container: ''
  name: options
  type: reference
- container: ''
  name: page
  type: reference
- container: set
  name: points
  type: string
- container: ''
  name: priority
  type: string
- container: ''
  name: public_id
  type: integer
- container: ''
  name: query
  type: string
- container: ''
  name: query_index
  type: integer
- container: ''
  name: relationships
  type: reference
- container: ''
  name: remote_config_read_enabled
  type: boolean
- container: ''
  name: renotify_interval
  type: integer
- container: set
  name: renotify_statuses
  type: string
- container: ''
  name: require_full_window
  type: boolean
- container: ''
  name: resolved
  type: dateTime
- container: set
  name: resources
  type: string
- container: set
  name: restricted_roles
  type: string
- container: ''
  name: scope
  type: string
- container: set
  name: series
  type: string
- container: ''
  name: service
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: silenced
  type: reference
- container: ''
  name: sort
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: source_type_name
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: status
  type: string
- container: set
  name: tags
  type: string
- container: ''
  name: thresholds
  type: string
- container: ''
  name: time_to_detect
  type: integer
- container: ''
  name: time_to_internal_response
  type: integer
- container: ''
  name: time_to_repair
  type: integer
- container: ''
  name: timeout_h
  type: integer
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: title
  type: string
- container: ''
  name: to
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: unit
  type: string
- container: ''
  name: unknown
  type: string
- container: ''
  name: value
  type: string
- container: set
  name: values
  type: string
- container: ''
  name: warning
  type: string
- container: ''
  name: warning_recovery
  type: string
property_count: 106
provider_name: Datadog
provider_slug: datadog
slug: datadog-context
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
- JSON-LD
- Linked Data
- Semantic Web
---
