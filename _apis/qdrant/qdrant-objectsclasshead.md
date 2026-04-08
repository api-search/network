---
aid: qdrant:qdrant-objectsclasshead
name: Qdrant Check if an object exists.
tags:
- Objects
humanURL: 
properties: []
description: >-
  Checks if a data object exists based on its collection and uuid without retrieving it. <br/><br/>Internally it skips reading the object from disk other than checking if it is present. Thus it does not use resources on marshalling, parsing, etc., and is faster. Note the resulting HTTP request has no body; the existence of an object is indicated solely by the status code.

---
