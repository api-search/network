---
aid: qdrant:qdrant-objectscreate
name: Qdrant Create a new object.
tags:
- Objects
humanURL: 
properties: []
description: >-
  Create a new object. <br/><br/>Meta-data and schema values are validated. <br/><br/>**Note: Use `/batch` for importing many objects**: <br/>If you plan on importing a large number of objects, it's much more efficient to use the `/batch` endpoint. Otherwise, sending multiple single requests sequentially would incur a large performance penalty. <br/><br/>**Note: idempotence of `/objects`**: <br/>POST /objects will fail if an id is provided which already exists in the class. To update an existin...

---
