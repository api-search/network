---
aid: dropbox:dropbox-post-2-file-properties-properties-overwrite
name: properties/overwrite
tags:
- file_properties
humanURL: 
properties: []
description: >-
  [properties/overwrite](https://www.dropbox.com/developers/documentation/http/documentation#file_properties-properties-overwrite)  scope: `files.metadata.write`  Overwrite property groups associated with a file. This endpoint should be used instead of `properties/update` when property groups are being updated via a "snapshot" instead of via a "delta". In other words, this endpoint will delete all omitted fields from a property group, whereas `properties/update` will only delete fields that are...

---
