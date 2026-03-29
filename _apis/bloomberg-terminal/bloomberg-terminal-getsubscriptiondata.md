---
aid: bloomberg-terminal:bloomberg-terminal-getsubscriptiondata
name: Poll for subscription data
tags:
- Subscriptions
humanURL: 
properties: []
description: >-
  Retrieves subscription data via long-polling. The pollid query parameter acts as a logical counter and implicit acknowledgement of previously received data. If a GET request with a specified pollid fails, the pollid may be reused to recover the last set of buffered subscription data.

---
