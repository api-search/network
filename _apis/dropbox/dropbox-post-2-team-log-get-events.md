---
aid: dropbox:dropbox-post-2-team-log-get-events
name: get_events
tags:
- team_log
humanURL: 
properties: []
description: >-
  [get_events](https://www.dropbox.com/developers/documentation/http/teams#team_log-get_events)  scope: `events.read`  Retrieves team events. If the result's `GetTeamEventsResult.has_more` field is `true`, call `get_events/continue` with the returned cursor to retrieve more entries. If end_time is not specified in your request, you may use the returned cursor to poll `get_events/continue` for new events. Many attributes note 'may be missing due to historical data gap'. Note that the file_operat...

---
