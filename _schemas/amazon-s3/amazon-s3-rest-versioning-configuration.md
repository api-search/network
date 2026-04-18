---
description: Container for setting the versioning state.
layout: schema
name: VersioningConfiguration
properties_list:
- description: The versioning state of the bucket.
  name: Status
  type: string
- description: Specifies whether MFA delete is enabled in the bucket versioning configuration.
  name: MFADelete
  type: string
provider_name: Amazon S3
provider_slug: amazon-s3
schema_file: json-schema/amazon-s3-rest-versioning-configuration-schema.json
slug: amazon-s3-rest-versioning-configuration
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
title: VersioningConfiguration
---
