---
description: Container for the objects to delete.
layout: schema
name: Delete
properties_list:
- description: Container element that describes the delete request for an object.
  name: Object
  type: array
- description: Element to enable quiet mode for the request. When added, it must be set to true.
  name: Quiet
  type: boolean
provider_name: Amazon S3
provider_slug: amazon-s3
schema_file: json-schema/amazon-s3-rest-delete-schema.json
slug: amazon-s3-rest-delete
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
title: Delete
---
