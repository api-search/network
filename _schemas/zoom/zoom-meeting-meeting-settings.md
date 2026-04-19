---
description: Meeting settings and options.
layout: schema
name: MeetingSettings
properties_list:
- description: Start video when the host joins the meeting.
  name: host_video
  type: boolean
- description: Start video when participants join the meeting.
  name: participant_video
  type: boolean
- description: Host meeting in China.
  name: cn_meeting
  type: boolean
- description: Host meeting in India.
  name: in_meeting
  type: boolean
- description: Allow participants to join before the host.
  name: join_before_host
  type: boolean
- description: Minutes before the host joins that participants can join. 0 - any time, 5 - 5 minutes, 10 - 10 minutes.
  name: jbh_time
  type: integer
- description: Mute participants upon entry.
  name: mute_upon_entry
  type: boolean
- description: Add watermark when viewing a shared screen.
  name: watermark
  type: boolean
- description: Use Personal Meeting ID instead of generated meeting ID.
  name: use_pmi
  type: boolean
- description: Registration approval type. 0 - Automatically approve, 1 - Manually approve, 2 - No registration required.
  name: approval_type
  type: integer
- description: Registration type for recurring meetings. 1 - Register once and attend any, 2 - Register for each, 3 - Register once and choose occurrences.
  name: registration_type
  type: integer
- description: Determine how participants can join the meeting audio.
  name: audio
  type: string
- description: Automatic recording configuration.
  name: auto_recording
  type: string
- description: Only authenticated users can join the meeting.
  name: enforce_login
  type: boolean
- description: Only users with specific email domain(s) can join. Comma separated for multiple domains.
  name: enforce_login_domains
  type: string
- description: Alternative host email addresses. Comma separated for multiple alternative hosts.
  name: alternative_hosts
  type: string
- description: Send email notification to alternative hosts.
  name: alternative_hosts_email_notification
  type: boolean
- description: Close registration after event date.
  name: close_registration
  type: boolean
- description: Enable the waiting room.
  name: waiting_room
  type: boolean
- description: List of countries for global dial-in numbers.
  name: global_dial_in_countries
  type: array
- description: Contact name for meeting registration.
  name: contact_name
  type: string
- description: Contact email for meeting registration.
  name: contact_email
  type: string
- description: Send email notifications to registrants.
  name: registrants_email_notification
  type: boolean
- description: Send confirmation email to registrants.
  name: registrants_confirmation_email
  type: boolean
- description: Require authentication to join.
  name: meeting_authentication
  type: boolean
- description: Meeting authentication option ID.
  name: authentication_option
  type: string
- description: Allowed authentication domains.
  name: authentication_domains
  type: string
- description: Authentication name set in the authentication profile.
  name: authentication_name
  type: string
- description: Show social share buttons on the registration page.
  name: show_share_button
  type: boolean
- description: Allow attendees to join from multiple devices.
  name: allow_multiple_devices
  type: boolean
- description: Meeting encryption type.
  name: encryption_type
  type: string
- description: Approve or block users from specific countries.
  name: approved_or_denied_countries_or_regions
  type: object
- description: Breakout room settings.
  name: breakout_room
  type: object
- description: Language interpretation settings.
  name: language_interpretation
  type: object
- description: Enable focus mode.
  name: focus_mode
  type: boolean
- description: List of users invited to the meeting.
  name: meeting_invitees
  type: array
- description: Make the meeting private.
  name: private_meeting
  type: boolean
- description: Send email notification when meeting starts.
  name: email_notification
  type: boolean
- description: Allow host to save the order of gallery view.
  name: host_save_video_order
  type: boolean
- description: Continuous meeting chat settings.
  name: continuous_meeting_chat
  type: object
provider_name: Zoom
provider_slug: zoom
schema_file: json-schema/zoom-meeting-meeting-settings-schema.json
slug: zoom-meeting-meeting-settings
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
title: MeetingSettings
---
