---
aid: convex:convex-runfunction
name: Execute any function by identifier
tags:
- Functions
humanURL: 
properties: []
description: >-
  Executes any deployed Convex function — query, mutation, or action — identified by the function path in the URL. The function identifier follows the format "module:exportName" (e.g. "messages:list" or "users:createUser"). Named arguments are passed as a JSON object in the request body. This unified endpoint automatically dispatches to the appropriate function type. Returns the function's return value and any console log output produced during execution.

---
