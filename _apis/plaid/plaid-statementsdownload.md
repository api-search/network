---
aid: plaid:plaid-statementsdownload
name: Plaid Retrieve a single statement.
tags:
- Plaid
humanURL: 
properties: []
description: >-
  The `/statements/download` endpoint retrieves a single statement PDF in binary format.  The response will contain a `Plaid-Content-Hash` header containing a SHA 256 checksum of the statement. This can be used to verify that the file being sent by Plaid is the same file that was downloaded to your system.

---
