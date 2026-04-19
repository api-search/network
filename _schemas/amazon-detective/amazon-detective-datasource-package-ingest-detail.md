---
description: Details about the ingest state of a datasource package
layout: schema
name: DatasourcePackageIngestDetail
properties_list:
- description: Details on which data source packages are ingested for a member account.
  name: DatasourcePackageIngestState
  type: string
- description: The date a data source package type was last updated for a member account.
  name: LastIngestStateChange
  type: object
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-datasource-package-ingest-detail-schema.json
slug: amazon-detective-datasource-package-ingest-detail
tags:
- AWS
- Forensics
- Investigation
- Security
title: DatasourcePackageIngestDetail
---
