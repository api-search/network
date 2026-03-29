---
aid: factset:factset-getinsightmapping
name: Redirects to the underlying Insight/Vault data in a Stach format.
tags:
- Analytics
- Swivel
- Document
- Name
- Tile
- Account
- Date
humanURL: 
properties: []
description: >-
  The inclusion of a configId in the path indicates this is for Insight/Vault mappings only, as PA/SPAR mappings do not support the concept of configuration id.  Takes report parameter inputs and returns the object location for the specified report via a 302 redirect.  Note: Due to Swagger UI functionality, the redirect is automatically followed when using 'Try it out', so instead of the 302 Header response, a 200 is returned with the Cargo response Body.

---
