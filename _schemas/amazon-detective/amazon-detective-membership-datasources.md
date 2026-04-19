---
description: Details on data source packages for a member account in a behavior graph
layout: schema
name: MembershipDatasources
properties_list:
- description: The account identifier of the AWS account.
  name: AccountId
  type: string
- description: The ARN of the organization behavior graph.
  name: GraphArn
  type: string
- description: Details on when a data source package was added to a behavior graph.
  name: DatasourcePackageIngestHistory
  type: object
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-membership-datasources-schema.json
slug: amazon-detective-membership-datasources
tags:
- AWS
- Forensics
- Investigation
- Security
title: MembershipDatasources
---
