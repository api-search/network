---
description: The root node in the resource hierarchy to which a particular entity's resources belong. An organization is tied to a Google Workspace or Cloud Identity account. Organizations cannot be created or deleted through the API; they are automatically provisioned when a Google Workspace or Cloud Identity account is created.
layout: schema
name: Organization
properties_list:
- description: The resource name of the organization in the form organizations/{organization_id}. Output only.
  name: name
  type: string
- description: A human-readable string that refers to the organization in the Google Cloud Console. This field is output only and derived from the associated Google Workspace or Cloud Identity account.
  name: displayName
  type: string
- description: The unique identifier for the Google Workspace or Cloud Identity account associated with this organization. Output only.
  name: directoryCustomerId
  type: string
- description: The organization lifecycle state. Output only.
  name: state
  type: string
- description: Timestamp when the organization was created. Output only.
  name: createTime
  type: string
- description: Timestamp when the organization was last modified. Output only.
  name: updateTime
  type: string
- description: Timestamp of when the delete request was sent. Output only.
  name: deleteTime
  type: string
- description: A checksum computed by the server based on the current value of the organization resource.
  name: etag
  type: string
provider_name: Google Cloud Platform
provider_slug: google-cloud-platform
schema_file: json-schema/cloud-resource-manager-organization-schema.json
slug: cloud-resource-manager-organization
tags:
- API Management
- Cloud Computing
- Infrastructure
- Platform as a Service
title: Organization
---
