---
aid: qdrant:qdrant-schemaobjectsupdate
name: Qdrant Update an existing collection.
tags:
- Schema
humanURL: 
properties: []
description: >-
  Alter an existing collection definition. <br/><br/>Note that not all settings are mutable ([see this list](https://weaviate.io/developers/weaviate/config-refs/schema#mutability)). To update any other (i.e. immutable) setting, you need to delete the collection, re-create it with the correct setting and then re-import the data. <br/><br/>This endpoint cannot be used to modify properties. Instead use POST /v1/schema/{className}/properties. A typical use case for this endpoint is to update a inde...

---
