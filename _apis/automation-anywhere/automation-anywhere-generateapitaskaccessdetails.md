---
aid: automation-anywhere:automation-anywhere-generateapitaskaccessdetails
name: Generate API Task execution URL and token
tags:
- AccessDetails
humanURL: 
properties: []
description: >-
  Generates a unique execution URL and short-lived authorization token for one or more API Tasks identified by their repository paths. The returned URL is used to invoke the API Task directly without going through the standard Control Room authentication flow. Both the URL and token are time-limited and should be refreshed periodically (recommended every 5 minutes) to prevent authorization failures during long-running integrations.

---
