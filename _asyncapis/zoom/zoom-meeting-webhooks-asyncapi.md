---
channels:
- description: Triggered when a meeting is created by a host or on behalf of a host.
  name: meetingCreated
- description: Triggered when a meeting is updated, including changes to topic, time, settings, or other meeting properties.
  name: meetingUpdated
- description: Triggered when a meeting is deleted by the host or an admin.
  name: meetingDeleted
- description: Triggered when a meeting starts. This event fires when the host or the first participant joins the meeting.
  name: meetingStarted
- description: Triggered when a meeting ends. This event fires when all participants have left the meeting or the host ends the meeting.
  name: meetingEnded
- description: Triggered when a previously deleted meeting is recovered from trash.
  name: meetingRecoveredFromTrash
- description: Triggered when a meeting is permanently deleted and can no longer be recovered.
  name: meetingPermanentlyDeleted
- description: Triggered when a participant joins a meeting. Includes participant details such as name, email, and join time.
  name: meetingParticipantJoined
- description: Triggered when a participant leaves a meeting. Includes participant details and leave reason.
  name: meetingParticipantLeft
- description: Triggered when a participant is waiting in the waiting room or waiting for the host to start the meeting.
  name: meetingParticipantWaitingForHost
- description: Triggered when a participant is admitted from the waiting room.
  name: meetingParticipantAdmittedFromWaitingRoom
- description: Triggered when a participant is placed in the waiting room during a meeting.
  name: meetingParticipantPutInWaitingRoom
- description: Triggered when a new registrant registers for a meeting.
  name: meetingRegistrationCreated
- description: Triggered when a meeting registration is approved.
  name: meetingRegistrationApproved
- description: Triggered when a meeting registration is cancelled.
  name: meetingRegistrationCancelled
- description: Triggered when a meeting registration is denied.
  name: meetingRegistrationDenied
- description: Triggered when a participant starts sharing their screen in a meeting.
  name: meetingSharingStarted
- description: Triggered when a participant stops sharing their screen in a meeting.
  name: meetingSharingEnded
- description: Triggered when a cloud recording for a meeting has been processed and is available for download.
  name: meetingRecordingCompleted
- description: Triggered when cloud recording starts for a meeting.
  name: meetingRecordingStarted
- description: Triggered when cloud recording stops for a meeting.
  name: meetingRecordingStopped
- description: Triggered when cloud recording is paused during a meeting.
  name: meetingRecordingPaused
- description: Triggered when cloud recording is resumed during a meeting.
  name: meetingRecordingResumed
- description: Triggered when a cloud recording is moved to trash.
  name: meetingRecordingTrashed
- description: Triggered when a cloud recording is permanently deleted.
  name: meetingRecordingDeleted
- description: Triggered when a cloud recording is recovered from trash.
  name: meetingRecordingRecovered
- description: Triggered when a recording transcript is completed and available.
  name: meetingRecordingTranscriptCompleted
- description: Triggered when a meeting quality alert is detected, such as poor network quality or audio issues.
  name: meetingAlert
description: Zoom delivers webhook event notifications to your application when meeting-related events occur on the Zoom platform. These webhooks enable real-time integration with meeting lifecycle events including creation, updates, starts, ends, participant joins and leaves, recordings, and alerts. Configure your webhook endpoint in the Zoom Marketplace to receive these event notifications.
layout: asyncapi
messages:
- description: ''
  name: MeetingCreated
  summary: A meeting has been created.
  title: Meeting Created
- description: ''
  name: MeetingUpdated
  summary: A meeting has been updated.
  title: Meeting Updated
- description: ''
  name: MeetingDeleted
  summary: A meeting has been deleted.
  title: Meeting Deleted
- description: ''
  name: MeetingStarted
  summary: A meeting has started.
  title: Meeting Started
- description: ''
  name: MeetingEnded
  summary: A meeting has ended.
  title: Meeting Ended
- description: ''
  name: MeetingRecovered
  summary: A deleted meeting has been recovered from trash.
  title: Meeting Recovered from Trash
- description: ''
  name: MeetingPermanentlyDeleted
  summary: A meeting has been permanently deleted.
  title: Meeting Permanently Deleted
- description: ''
  name: ParticipantJoined
  summary: A participant has joined a meeting.
  title: Participant Joined Meeting
- description: ''
  name: ParticipantLeft
  summary: A participant has left a meeting.
  title: Participant Left Meeting
- description: ''
  name: ParticipantWaitingForHost
  summary: A participant is waiting for the host or in the waiting room.
  title: Participant Waiting for Host
- description: ''
  name: ParticipantAdmittedFromWaitingRoom
  summary: A participant has been admitted from the waiting room.
  title: Participant Admitted from Waiting Room
- description: ''
  name: ParticipantPutInWaitingRoom
  summary: A participant has been placed in the waiting room.
  title: Participant Put in Waiting Room
- description: ''
  name: RegistrationCreated
  summary: A new registrant has registered for a meeting.
  title: Meeting Registration Created
- description: ''
  name: RegistrationApproved
  summary: A meeting registration has been approved.
  title: Meeting Registration Approved
- description: ''
  name: RegistrationCancelled
  summary: A meeting registration has been cancelled.
  title: Meeting Registration Cancelled
- description: ''
  name: RegistrationDenied
  summary: A meeting registration has been denied.
  title: Meeting Registration Denied
- description: ''
  name: MeetingSharingStarted
  summary: Screen sharing has started in a meeting.
  title: Meeting Sharing Started
- description: ''
  name: MeetingSharingEnded
  summary: Screen sharing has ended in a meeting.
  title: Meeting Sharing Ended
- description: ''
  name: RecordingCompleted
  summary: Cloud recording has been processed and is available for download.
  title: Recording Completed
- description: ''
  name: RecordingStarted
  summary: Cloud recording has started.
  title: Recording Started
- description: ''
  name: RecordingStopped
  summary: Cloud recording has stopped.
  title: Recording Stopped
- description: ''
  name: RecordingPaused
  summary: Cloud recording has been paused.
  title: Recording Paused
- description: ''
  name: RecordingResumed
  summary: Cloud recording has been resumed.
  title: Recording Resumed
- description: ''
  name: RecordingTrashed
  summary: A cloud recording has been moved to trash.
  title: Recording Trashed
- description: ''
  name: RecordingDeleted
  summary: A cloud recording has been permanently deleted.
  title: Recording Deleted
- description: ''
  name: RecordingRecovered
  summary: A cloud recording has been recovered from trash.
  title: Recording Recovered
- description: ''
  name: RecordingTranscriptCompleted
  summary: A recording transcript has been completed and is available.
  title: Recording Transcript Completed
- description: ''
  name: MeetingAlert
  summary: A meeting quality alert has been triggered, such as poor network quality or audio/video issues.
  title: Meeting Alert
name: Zoom Meeting Webhooks
provider_name: Zoom
provider_slug: zoom
servers:
- description: Your application's webhook endpoint URL. Zoom sends HTTP POST requests to this URL when events occur. Configure this URL in your Zoom Marketplace app settings under the Event Subscriptions section.
  name: zoomWebhookEndpoint
  protocol: https
  url: ''
slug: zoom-meeting-webhooks-asyncapi
spec_file: asyncapi/zoom-meeting-webhooks-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/zoom/refs/heads/main/asyncapi/zoom-meeting-webhooks-asyncapi.yml
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
- AsyncAPI
- Webhooks
- Events
version: 2.0.0
---
