---
class_count: 128
classes:
- DagStatsCollectionResponse
- ExternalLogUrlResponse
- ConfigOption
- BackfillPostBody
- TaskDependencyCollectionResponse
- XComResponseString
- DAGWarningResponse
- LastAssetEventResponse
- DAGWarningCollectionResponse
- MaterializeAssetBody
- HITLDetailHistory
- DagTagResponse
- ProviderResponse
- EventLogCollectionResponse
- EventLogResponse
- BulkDeleteAction_BulkTaskInstanceBody_
- BulkActionResponse
- TriggerResponse
- DagRunAssetReference
- ConfigSection
- DAGRunCollectionResponse
- BulkBody_PoolBody_
- CreateAssetEventsBody
- HITLDetailResponse
- BulkBody_BulkTaskInstanceBody_
- StructuredLogMessage
- ImportErrorCollectionResponse
- ExternalViewResponse
- DagStatsStateResponse
- BulkBody_VariableBody_
- ConnectionCollectionResponse
- BulkResponse
- JobCollectionResponse
- Config
- ConnectionBody
- VariableResponse
- DAGTagCollectionResponse
- BulkCreateAction_VariableBody_
- TriggerDAGRunPostBody
- TaskInstancesBatchBody
- ExtraLinkCollectionResponse
- TaskCollectionResponse
- DAGRunResponse
- BulkDeleteAction_VariableBody_
- ReactAppResponse
- QueuedEventCollectionResponse
- TriggererInfoResponse
- VersionInfo
- DryRunBackfillResponse
- PoolCollectionResponse
- TaskInletAssetReference
- TaskInstanceCollectionResponse
- DagScheduleAssetReference
- UpdateHITLDetailPayload
- VariableBody
- DAGSourceResponse
- BackfillCollectionResponse
- DAGRunPatchBody
- TaskInstanceResponse
- HITLDetail
- XComResponseNative
- XComResponse
- XComUpdateBody
- QueuedEventResponse
- AssetWatcherResponse
- BulkUpdateAction_PoolBody_
- ConnectionTestResponse
- TaskOutletAssetReference
- PoolBody
- DagProcessorInfoResponse
- XComCollectionResponse
- DagStatsResponse
- FastAPIRootMiddlewareResponse
- DAGVersionCollectionResponse
- AppBuilderViewResponse
- DAGPatchBody
- BulkCreateAction_PoolBody_
- PluginResponse
- TaskResponse
- SchedulerInfoResponse
- ImportErrorResponse
- TaskInstancesLogResponse
- HITLUser
- VariableCollectionResponse
- TaskInstanceHistoryResponse
- TimeDelta
- PoolPatchBody
- ClearTaskInstancesBody
- BaseInfoResponse
- DAGCollectionResponse
- ProviderCollectionResponse
- JobResponse
- HTTPExceptionResponse
- BulkCreateAction_BulkTaskInstanceBody_
- BulkBody_ConnectionBody_
- XComCreateBody
- BulkUpdateAction_ConnectionBody_
- PatchTaskInstanceBody
- PluginCollectionResponse
- HITLDetailCollection
- AssetAliasResponse
- AssetEventCollectionResponse
- TaskDependencyResponse
- PoolResponse
- DAGDetailsResponse
- BulkTaskInstanceBody
- AssetEventResponse
- DAGRunClearBody
- AssetCollectionResponse
- BulkUpdateAction_VariableBody_
- DAGRunsBatchBody
- AssetResponse
- BackfillResponse
- BulkDeleteAction_PoolBody_
- AppBuilderMenuItemResponse
- BulkDeleteAction_ConnectionBody_
- BulkUpdateAction_BulkTaskInstanceBody_
- FastAPIAppResponse
- TaskInstanceHistoryCollectionResponse
- PluginImportErrorCollectionResponse
- AssetAliasCollectionResponse
- BulkCreateAction_ConnectionBody_
- DAGResponse
- PluginImportErrorResponse
- ConnectionResponse
- DryRunBackfillCollectionResponse
- DagVersionResponse
- HealthInfoResponse
context_file: json-ld/airflow-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/airflow/refs/heads/main/json-ld/airflow-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Airflow from Apache Airflow.
layout: jsonld
name: Airflow Context
namespaces:
- prefix: airflow
  uri: https://airflow.apache.org/schema/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: schema
  type: ''
- container: ''
  name: dags
  type: ''
- container: ''
  name: totalEntries
  type: integer
- container: ''
  name: url
  type: ''
- container: ''
  name: key
  type: ''
- container: ''
  name: value
  type: ''
- container: ''
  name: dagId
  type: ''
- container: ''
  name: fromDate
  type: dateTime
- container: ''
  name: toDate
  type: dateTime
- container: ''
  name: runBackwards
  type: boolean
- container: ''
  name: dagRunConf
  type: ''
- container: ''
  name: reprocessBehavior
  type: ''
- container: ''
  name: maxActiveRuns
  type: ''
- container: ''
  name: runOnLatestVersion
  type: boolean
- container: ''
  name: dependencies
  type: ''
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: logicalDate
  type: ''
- container: ''
  name: mapIndex
  type: ''
- container: ''
  name: taskId
  type: ''
- container: ''
  name: runId
  type: ''
- container: ''
  name: dagDisplayName
  type: ''
- container: ''
  name: taskDisplayName
  type: ''
- container: ''
  name: runAfter
  type: dateTime
- container: ''
  name: warningType
  type: ''
- container: ''
  name: message
  type: ''
- container: ''
  name: id
  type: ''
- container: ''
  name: dagWarnings
  type: ''
- container: ''
  name: dagRunId
  type: ''
- container: ''
  name: dataIntervalStart
  type: ''
- container: ''
  name: dataIntervalEnd
  type: ''
- container: ''
  name: conf
  type: ''
- container: ''
  name: note
  type: ''
- container: ''
  name: partitionKey
  type: ''
- container: ''
  name: options
  type: ''
- container: ''
  name: subject
  type: ''
- container: ''
  name: body
  type: ''
- container: ''
  name: defaults
  type: ''
- container: ''
  name: multiple
  type: boolean
- container: ''
  name: params
  type: ''
- container: ''
  name: assignedUsers
  type: ''
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: respondedByUser
  type: ''
- container: ''
  name: respondedAt
  type: ''
- container: ''
  name: chosenOptions
  type: ''
- container: ''
  name: paramsInput
  type: ''
- container: ''
  name: responseReceived
  type: boolean
- container: ''
  name: taskInstance
  type: ''
- container: ''
  name: name
  type: ''
- container: ''
  name: packageName
  type: ''
- container: ''
  name: description
  type: ''
- container: ''
  name: version
  type: ''
- container: ''
  name: documentationUrl
  type: ''
- container: ''
  name: eventLogs
  type: ''
- container: ''
  name: eventLogId
  type: integer
- container: ''
  name: when
  type: dateTime
- container: ''
  name: tryNumber
  type: integer
- container: ''
  name: event
  type: ''
- container: ''
  name: owner
  type: ''
- container: ''
  name: extra
  type: ''
- container: ''
  name: action
  type: ''
- container: ''
  name: entities
  type: ''
- container: ''
  name: actionOnNonExistence
  type: ''
- container: ''
  name: success
  type: ''
- container: ''
  name: errors
  type: ''
- container: ''
  name: classpath
  type: ''
- container: ''
  name: kwargs
  type: ''
- container: ''
  name: createdDate
  type: dateTime
- container: ''
  name: queue
  type: ''
- container: ''
  name: triggererId
  type: ''
- container: ''
  name: startDate
  type: ''
- container: ''
  name: endDate
  type: ''
- container: ''
  name: state
  type: ''
- container: ''
  name: dagRuns
  type: ''
- container: ''
  name: actions
  type: ''
- container: ''
  name: assetId
  type: integer
- container: ''
  name: respondedBy
  type: ''
- container: ''
  name: importErrors
  type: ''
- container: ''
  name: icon
  type: ''
- container: ''
  name: iconDarkMode
  type: ''
- container: ''
  name: urlRoute
  type: ''
- container: ''
  name: category
  type: ''
- container: ''
  name: href
  type: ''
- container: ''
  name: destination
  type: ''
- container: ''
  name: count
  type: integer
- container: ''
  name: connections
  type: ''
- container: ''
  name: create
  type: ''
- container: ''
  name: update
  type: ''
- container: ''
  name: delete
  type: ''
- container: ''
  name: jobs
  type: ''
- container: ''
  name: sections
  type: ''
- container: ''
  name: connectionId
  type: ''
- container: ''
  name: connType
  type: ''
- container: ''
  name: host
  type: ''
- container: ''
  name: login
  type: ''
- container: ''
  name: port
  type: ''
- container: ''
  name: password
  type: ''
- container: ''
  name: teamName
  type: ''
- container: ''
  name: isEncrypted
  type: boolean
- container: ''
  name: tags
  type: ''
- container: ''
  name: actionOnExistence
  type: ''
- container: ''
  name: dagIds
  type: ''
- container: ''
  name: dagRunIds
  type: ''
- container: ''
  name: taskIds
  type: ''
- container: ''
  name: runAfterGte
  type: ''
- container: ''
  name: runAfterGt
  type: ''
- container: ''
  name: runAfterLte
  type: ''
- container: ''
  name: runAfterLt
  type: ''
- container: ''
  name: logicalDateGte
  type: ''
- container: ''
  name: logicalDateGt
  type: ''
- container: ''
  name: logicalDateLte
  type: ''
- container: ''
  name: logicalDateLt
  type: ''
- container: ''
  name: startDateGte
  type: ''
- container: ''
  name: startDateGt
  type: ''
- container: ''
  name: startDateLte
  type: ''
- container: ''
  name: startDateLt
  type: ''
- container: ''
  name: endDateGte
  type: ''
- container: ''
  name: endDateGt
  type: ''
- container: ''
  name: endDateLte
  type: ''
- container: ''
  name: endDateLt
  type: ''
- container: ''
  name: durationGte
  type: ''
- container: ''
  name: durationGt
  type: ''
- container: ''
  name: durationLte
  type: ''
- container: ''
  name: durationLt
  type: ''
- container: ''
  name: pool
  type: ''
- container: ''
  name: executor
  type: ''
- container: ''
  name: pageOffset
  type: integer
- container: ''
  name: pageLimit
  type: integer
- container: ''
  name: orderBy
  type: ''
- container: ''
  name: extraLinks
  type: ''
- container: ''
  name: tasks
  type: ''
- container: ''
  name: queuedAt
  type: ''
- container: ''
  name: duration
  type: ''
- container: ''
  name: lastSchedulingDecision
  type: ''
- container: ''
  name: runType
  type: ''
- container: ''
  name: triggeredBy
  type: ''
- container: ''
  name: triggeringUserName
  type: ''
- container: ''
  name: dagVersions
  type: ''
- container: ''
  name: bundleVersion
  type: ''
- container: ''
  name: bundleUrl
  type: ''
- container: ''
  name: queuedEvents
  type: ''
- container: ''
  name: status
  type: ''
- container: ''
  name: latestTriggererHeartbeat
  type: ''
- container: ''
  name: gitVersion
  type: ''
- container: ''
  name: partitionDate
  type: ''
- container: ''
  name: pools
  type: ''
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: taskInstances
  type: ''
- container: ''
  name: nextCursor
  type: ''
- container: ''
  name: previousCursor
  type: ''
- container: ''
  name: content
  type: ''
- container: ''
  name: versionNumber
  type: integer
- container: ''
  name: backfills
  type: ''
- container: ''
  name: maxTries
  type: integer
- container: ''
  name: hostname
  type: ''
- container: ''
  name: unixname
  type: ''
- container: ''
  name: poolSlots
  type: integer
- container: ''
  name: priorityWeight
  type: ''
- container: ''
  name: operator
  type: ''
- container: ''
  name: operatorName
  type: ''
- container: ''
  name: queuedWhen
  type: ''
- container: ''
  name: scheduledWhen
  type: ''
- container: ''
  name: pid
  type: ''
- container: ''
  name: executorConfig
  type: ''
- container: ''
  name: renderedMapIndex
  type: ''
- container: ''
  name: renderedFields
  type: ''
- container: ''
  name: trigger
  type: ''
- container: ''
  name: triggererJob
  type: ''
- container: ''
  name: dagVersion
  type: ''
- container: ''
  name: triggerId
  type: integer
- container: ''
  name: updateMask
  type: ''
- container: ''
  name: slots
  type: integer
- container: ''
  name: includeDeferred
  type: boolean
- container: ''
  name: latestDagProcessorHeartbeat
  type: ''
- container: ''
  name: xcomEntries
  type: ''
- container: ''
  name: stats
  type: ''
- container: ''
  name: middleware
  type: ''
- container: ''
  name: view
  type: ''
- container: ''
  name: label
  type: ''
- container: ''
  name: isPaused
  type: boolean
- container: ''
  name: macros
  type: ''
- container: ''
  name: flaskBlueprints
  type: ''
- container: ''
  name: fastapiApps
  type: ''
- container: ''
  name: fastapiRootMiddlewares
  type: ''
- container: ''
  name: externalViews
  type: ''
- container: ''
  name: reactApps
  type: ''
- container: ''
  name: appbuilderViews
  type: ''
- container: ''
  name: appbuilderMenuItems
  type: ''
- container: ''
  name: globalOperatorExtraLinks
  type: ''
- container: ''
  name: operatorExtraLinks
  type: ''
- container: ''
  name: source
  type: ''
- container: ''
  name: listeners
  type: ''
- container: ''
  name: timetables
  type: ''
- container: ''
  name: triggerRule
  type: ''
- container: ''
  name: dependsOnPast
  type: boolean
- container: ''
  name: waitForDownstream
  type: boolean
- container: ''
  name: retries
  type: ''
- container: ''
  name: executionTimeout
  type: ''
- container: ''
  name: retryDelay
  type: ''
- container: ''
  name: retryExponentialBackoff
  type: decimal
- container: ''
  name: weightRule
  type: ''
- container: ''
  name: uiColor
  type: ''
- container: ''
  name: uiFgcolor
  type: ''
- container: ''
  name: templateFields
  type: ''
- container: ''
  name: downstreamTaskIds
  type: ''
- container: ''
  name: docMd
  type: ''
- container: ''
  name: classRef
  type: ''
- container: ''
  name: isMapped
  type: ''
- container: ''
  name: latestSchedulerHeartbeat
  type: ''
- container: ''
  name: importErrorId
  type: integer
- container: ''
  name: filename
  type: ''
- container: ''
  name: bundleName
  type: ''
- container: ''
  name: stackTrace
  type: ''
- container: ''
  name: continuationToken
  type: ''
- container: ''
  name: variables
  type: ''
- container: ''
  name: Type
  type: ''
- container: ''
  name: days
  type: integer
- container: ''
  name: seconds
  type: integer
- container: ''
  name: microseconds
  type: integer
- container: ''
  name: dryRun
  type: boolean
- container: ''
  name: onlyFailed
  type: boolean
- container: ''
  name: onlyRunning
  type: boolean
- container: ''
  name: resetDagRuns
  type: boolean
- container: ''
  name: includeUpstream
  type: boolean
- container: ''
  name: includeDownstream
  type: boolean
- container: ''
  name: includeFuture
  type: boolean
- container: ''
  name: includePast
  type: boolean
- container: ''
  name: preventRunningTask
  type: boolean
- container: ''
  name: providers
  type: ''
- container: ''
  name: jobType
  type: ''
- container: ''
  name: latestHeartbeat
  type: ''
- container: ''
  name: executorClass
  type: ''
- container: ''
  name: detail
  type: ''
- container: ''
  name: newState
  type: ''
- container: ''
  name: plugins
  type: ''
- container: ''
  name: hitlDetails
  type: ''
- container: ''
  name: group
  type: ''
- container: ''
  name: assetEvents
  type: ''
- container: ''
  name: reason
  type: ''
- container: ''
  name: occupiedSlots
  type: integer
- container: ''
  name: runningSlots
  type: integer
- container: ''
  name: queuedSlots
  type: integer
- container: ''
  name: scheduledSlots
  type: integer
- container: ''
  name: openSlots
  type: integer
- container: ''
  name: deferredSlots
  type: integer
- container: ''
  name: isStale
  type: boolean
- container: ''
  name: lastParsedTime
  type: ''
- container: ''
  name: lastParseDuration
  type: ''
- container: ''
  name: lastExpired
  type: ''
- container: ''
  name: relativeFileloc
  type: ''
- container: ''
  name: fileloc
  type: ''
- container: ''
  name: timetableSummary
  type: ''
- container: ''
  name: timetableDescription
  type: ''
- container: ''
  name: timetablePartitioned
  type: boolean
- container: ''
  name: timetablePeriodic
  type: boolean
- container: ''
  name: maxActiveTasks
  type: integer
- container: ''
  name: maxConsecutiveFailedDagRuns
  type: integer
- container: ''
  name: hasTaskConcurrencyLimits
  type: boolean
- container: ''
  name: hasImportErrors
  type: boolean
- container: ''
  name: nextDagrunLogicalDate
  type: ''
- container: ''
  name: nextDagrunDataIntervalStart
  type: ''
- container: ''
  name: nextDagrunDataIntervalEnd
  type: ''
- container: ''
  name: nextDagrunRunAfter
  type: ''
- container: ''
  name: allowedRunTypes
  type: ''
- container: ''
  name: owners
  type: ''
- container: ''
  name: catchup
  type: boolean
- container: ''
  name: dagRunTimeout
  type: ''
- container: ''
  name: assetExpression
  type: ''
- container: ''
  name: isPausedUponCreation
  type: ''
- container: ''
  name: renderTemplateAsNativeObj
  type: boolean
- container: ''
  name: templateSearchPath
  type: ''
- container: ''
  name: timezone
  type: ''
- container: ''
  name: lastParsed
  type: ''
- container: ''
  name: defaultArgs
  type: ''
- container: ''
  name: ownerLinks
  type: ''
- container: ''
  name: isFavorite
  type: boolean
- container: ''
  name: activeRunsCount
  type: integer
- container: ''
  name: isBackfillable
  type: boolean
- container: ''
  name: fileToken
  type: ''
- container: ''
  name: concurrency
  type: integer
- container: ''
  name: latestDagVersion
  type: ''
- container: ''
  name: uri
  type: ''
- container: ''
  name: sourceTaskId
  type: ''
- container: ''
  name: sourceDagId
  type: ''
- container: ''
  name: sourceRunId
  type: ''
- container: ''
  name: sourceMapIndex
  type: integer
- container: ''
  name: createdDagruns
  type: ''
- container: ''
  name: assets
  type: ''
- container: ''
  name: states
  type: ''
- container: ''
  name: confContains
  type: ''
- container: ''
  name: scheduledDags
  type: ''
- container: ''
  name: producingTasks
  type: ''
- container: ''
  name: consumingTasks
  type: ''
- container: ''
  name: aliases
  type: ''
- container: ''
  name: watchers
  type: ''
- container: ''
  name: lastAssetEvent
  type: ''
- container: ''
  name: completedAt
  type: ''
- container: ''
  name: app
  type: ''
- container: ''
  name: urlPrefix
  type: ''
- container: ''
  name: assetAliases
  type: ''
- container: ''
  name: error
  type: ''
- container: ''
  name: metadatabase
  type: ''
- container: ''
  name: scheduler
  type: ''
- container: ''
  name: triggerer
  type: ''
- container: ''
  name: dagProcessor
  type: ''
property_count: 304
provider_name: Apache Airflow
provider_slug: airflow
slug: airflow-context
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
- JSON-LD
- Linked Data
- Semantic Web
---
