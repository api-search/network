---
description: <p>Event within a workflow execution. A history event can be one of these types:</p> <ul> <li> <p> <code>ActivityTaskCancelRequested</code> – A <code>RequestCancelActivityTask</code> decision was received by the system.</p> </li> <li> <p> <code>ActivityTaskCanceled</code> – The activity task was successfully canceled.</p> </li> <li> <p> <code>ActivityTaskCompleted</code> – An activity worker successfully completed an activity task by calling <a>RespondActivityTaskCompleted</a>.</p> </li> <li> <p> <code>ActivityTaskFailed</code> – An activity worker failed an activity task by calling <a>RespondActivityTaskFailed</a>.</p> </li> <li> <p> <code>ActivityTaskScheduled</code> – An activity task was scheduled for execution.</p> </li> <li> <p> <code>ActivityTaskStarted</code> – The scheduled activity task was dispatched to a worker.</p> </li> <li> <p> <code>ActivityTaskTimedOut</code> – The activity task timed out.</p> </li> <li> <p> <code>CancelTimerFailed</code> – Failed to process
  CancelTimer decision. This happens when the decision isn't configured properly, for example no timer exists with the specified timer Id.</p> </li> <li> <p> <code>CancelWorkflowExecutionFailed</code> – A request to cancel a workflow execution failed.</p> </li> <li> <p> <code>ChildWorkflowExecutionCanceled</code> – A child workflow execution, started by this workflow execution, was canceled and closed.</p> </li> <li> <p> <code>ChildWorkflowExecutionCompleted</code> – A child workflow execution, started by this workflow execution, completed successfully and was closed.</p> </li> <li> <p> <code>ChildWorkflowExecutionFailed</code> – A child workflow execution, started by this workflow execution, failed to complete successfully and was closed.</p> </li> <li> <p> <code>ChildWorkflowExecutionStarted</code> – A child workflow execution was successfully started.</p> </li> <li> <p> <code>ChildWorkflowExecutionTerminated</code> – A child workflow execution, started by this workflow execution, was
  terminated.</p> </li> <li> <p> <code>ChildWorkflowExecutionTimedOut</code> – A child workflow execution, started by this workflow execution, timed out and was closed.</p> </li> <li> <p> <code>CompleteWorkflowExecutionFailed</code> – The workflow execution failed to complete.</p> </li> <li> <p> <code>ContinueAsNewWorkflowExecutionFailed</code> – The workflow execution failed to complete after being continued as a new workflow execution.</p> </li> <li> <p> <code>DecisionTaskCompleted</code> – The decider successfully completed a decision task by calling <a>RespondDecisionTaskCompleted</a>.</p> </li> <li> <p> <code>DecisionTaskScheduled</code> – A decision task was scheduled for the workflow execution.</p> </li> <li> <p> <code>DecisionTaskStarted</code> – The decision task was dispatched to a decider.</p> </li> <li> <p> <code>DecisionTaskTimedOut</code> – The decision task timed out.</p> </li> <li> <p> <code>ExternalWorkflowExecutionCancelRequested</code> – Request to cancel an external workflow
  execution was successfully delivered to the target execution.</p> </li> <li> <p> <code>ExternalWorkflowExecutionSignaled</code> – A signal, requested by this workflow execution, was successfully delivered to the target external workflow execution.</p> </li> <li> <p> <code>FailWorkflowExecutionFailed</code> – A request to mark a workflow execution as failed, itself failed.</p> </li> <li> <p> <code>MarkerRecorded</code> – A marker was recorded in the workflow history as the result of a <code>RecordMarker</code> decision.</p> </li> <li> <p> <code>RecordMarkerFailed</code> – A <code>RecordMarker</code> decision was returned as failed.</p> </li> <li> <p> <code>RequestCancelActivityTaskFailed</code> – Failed to process RequestCancelActivityTask decision. This happens when the decision isn't configured properly.</p> </li> <li> <p> <code>RequestCancelExternalWorkflowExecutionFailed</code> – Request to cancel an external workflow execution failed.</p> </li> <li> <p> <code>RequestCancelExternalWorkflowExecutionInitiated</code>
  – A request was made to request the cancellation of an external workflow execution.</p> </li> <li> <p> <code>ScheduleActivityTaskFailed</code> – Failed to process ScheduleActivityTask decision. This happens when the decision isn't configured properly, for example the activity type specified isn't registered.</p> </li> <li> <p> <code>SignalExternalWorkflowExecutionFailed</code> – The request to signal an external workflow execution failed.</p> </li> <li> <p> <code>SignalExternalWorkflowExecutionInitiated</code> – A request to signal an external workflow was made.</p> </li> <li> <p> <code>StartActivityTaskFailed</code> – A scheduled activity task failed to start.</p> </li> <li> <p> <code>StartChildWorkflowExecutionFailed</code> – Failed to process StartChildWorkflowExecution decision. This happens when the decision isn't configured properly, for example the workflow type specified isn't registered.</p> </li> <li> <p> <code>StartChildWorkflowExecutionInitiated</code> – A request was made
  to start a child workflow execution.</p> </li> <li> <p> <code>StartTimerFailed</code> – Failed to process StartTimer decision. This happens when the decision isn't configured properly, for example a timer already exists with the specified timer Id.</p> </li> <li> <p> <code>TimerCanceled</code> – A timer, previously started for this workflow execution, was successfully canceled.</p> </li> <li> <p> <code>TimerFired</code> – A timer, previously started for this workflow execution, fired.</p> </li> <li> <p> <code>TimerStarted</code> – A timer was started for the workflow execution due to a <code>StartTimer</code> decision.</p> </li> <li> <p> <code>WorkflowExecutionCancelRequested</code> – A request to cancel this workflow execution was made.</p> </li> <li> <p> <code>WorkflowExecutionCanceled</code> – The workflow execution was successfully canceled and closed.</p> </li> <li> <p> <code>WorkflowExecutionCompleted</code> – The workflow execution was closed due to successful completion.</p> </li>
  <li> <p> <code>WorkflowExecutionContinuedAsNew</code> – The workflow execution was closed and a new execution of the same type was created with the same workflowId.</p> </li> <li> <p> <code>WorkflowExecutionFailed</code> – The workflow execution closed due to a failure.</p> </li> <li> <p> <code>WorkflowExecutionSignaled</code> – An external signal was received for the workflow execution.</p> </li> <li> <p> <code>WorkflowExecutionStarted</code> – The workflow execution was started.</p> </li> <li> <p> <code>WorkflowExecutionTerminated</code> – The workflow execution was terminated.</p> </li> <li> <p> <code>WorkflowExecutionTimedOut</code> – The workflow execution was closed because a time out was exceeded.</p> </li> </ul>
layout: schema
name: HistoryEvent
properties_list:
- description: ''
  name: eventTimestamp
  type: object
- description: ''
  name: eventType
  type: object
- description: ''
  name: eventId
  type: object
- description: ''
  name: workflowExecutionStartedEventAttributes
  type: object
- description: ''
  name: workflowExecutionCompletedEventAttributes
  type: object
- description: ''
  name: completeWorkflowExecutionFailedEventAttributes
  type: object
- description: ''
  name: workflowExecutionFailedEventAttributes
  type: object
- description: ''
  name: failWorkflowExecutionFailedEventAttributes
  type: object
- description: ''
  name: workflowExecutionTimedOutEventAttributes
  type: object
- description: ''
  name: workflowExecutionCanceledEventAttributes
  type: object
- description: ''
  name: cancelWorkflowExecutionFailedEventAttributes
  type: object
- description: ''
  name: workflowExecutionContinuedAsNewEventAttributes
  type: object
- description: ''
  name: continueAsNewWorkflowExecutionFailedEventAttributes
  type: object
- description: ''
  name: workflowExecutionTerminatedEventAttributes
  type: object
- description: ''
  name: workflowExecutionCancelRequestedEventAttributes
  type: object
- description: ''
  name: decisionTaskScheduledEventAttributes
  type: object
- description: ''
  name: decisionTaskStartedEventAttributes
  type: object
- description: ''
  name: decisionTaskCompletedEventAttributes
  type: object
- description: ''
  name: decisionTaskTimedOutEventAttributes
  type: object
- description: ''
  name: activityTaskScheduledEventAttributes
  type: object
- description: ''
  name: activityTaskStartedEventAttributes
  type: object
- description: ''
  name: activityTaskCompletedEventAttributes
  type: object
- description: ''
  name: activityTaskFailedEventAttributes
  type: object
- description: ''
  name: activityTaskTimedOutEventAttributes
  type: object
- description: ''
  name: activityTaskCanceledEventAttributes
  type: object
- description: ''
  name: activityTaskCancelRequestedEventAttributes
  type: object
- description: ''
  name: workflowExecutionSignaledEventAttributes
  type: object
- description: ''
  name: markerRecordedEventAttributes
  type: object
- description: ''
  name: recordMarkerFailedEventAttributes
  type: object
- description: ''
  name: timerStartedEventAttributes
  type: object
- description: ''
  name: timerFiredEventAttributes
  type: object
- description: ''
  name: timerCanceledEventAttributes
  type: object
- description: ''
  name: startChildWorkflowExecutionInitiatedEventAttributes
  type: object
- description: ''
  name: childWorkflowExecutionStartedEventAttributes
  type: object
- description: ''
  name: childWorkflowExecutionCompletedEventAttributes
  type: object
- description: ''
  name: childWorkflowExecutionFailedEventAttributes
  type: object
- description: ''
  name: childWorkflowExecutionTimedOutEventAttributes
  type: object
- description: ''
  name: childWorkflowExecutionCanceledEventAttributes
  type: object
- description: ''
  name: childWorkflowExecutionTerminatedEventAttributes
  type: object
- description: ''
  name: signalExternalWorkflowExecutionInitiatedEventAttributes
  type: object
- description: ''
  name: externalWorkflowExecutionSignaledEventAttributes
  type: object
- description: ''
  name: signalExternalWorkflowExecutionFailedEventAttributes
  type: object
- description: ''
  name: externalWorkflowExecutionCancelRequestedEventAttributes
  type: object
- description: ''
  name: requestCancelExternalWorkflowExecutionInitiatedEventAttributes
  type: object
- description: ''
  name: requestCancelExternalWorkflowExecutionFailedEventAttributes
  type: object
- description: ''
  name: scheduleActivityTaskFailedEventAttributes
  type: object
- description: ''
  name: requestCancelActivityTaskFailedEventAttributes
  type: object
- description: ''
  name: startTimerFailedEventAttributes
  type: object
- description: ''
  name: cancelTimerFailedEventAttributes
  type: object
- description: ''
  name: startChildWorkflowExecutionFailedEventAttributes
  type: object
- description: ''
  name: lambdaFunctionScheduledEventAttributes
  type: object
- description: ''
  name: lambdaFunctionStartedEventAttributes
  type: object
- description: ''
  name: lambdaFunctionCompletedEventAttributes
  type: object
- description: ''
  name: lambdaFunctionFailedEventAttributes
  type: object
- description: ''
  name: lambdaFunctionTimedOutEventAttributes
  type: object
- description: ''
  name: scheduleLambdaFunctionFailedEventAttributes
  type: object
- description: ''
  name: startLambdaFunctionFailedEventAttributes
  type: object
provider_name: Amazon Simple Workflow Service
provider_slug: amazon-swf
schema_file: json-schema/amazon-swf-historyevent-schema.json
slug: amazon-swf-historyevent
tags:
- Automation
- AWS
- Task Coordination
- Workflow
title: HistoryEvent
---
