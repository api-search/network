---
description: A project is a high-level Google Cloud entity. It is a container for ACLs, APIs, App Engine Apps, VMs, and other Google Cloud Platform resources. Projects are the base-level organizing entity and are required to use service-level resources.
layout: schema
name: Project
properties_list:
- description: The unique resource name of the project in the form projects/{project_number}. Output only.
  name: name
  type: string
- description: The resource name of the parent in the form folders/{folder_id} or organizations/{organization_id}. Required when creating a project.
  name: parent
  type: string
- description: The unique, user-assigned identifier of the project. It must be 6 to 30 lowercase ASCII letters, digits, or hyphens. It must start with a letter and cannot end with a hyphen. Project IDs are immutable
  name: projectId
  type: string
- description: The project lifecycle state. Output only.
  name: state
  type: string
- description: A user-assigned display name for the project. This field is optional and has a maximum length of 30 characters. Display names are used for identification purposes and do not need to be unique.
  name: displayName
  type: string
- description: Timestamp of when the project was created. Output only. Uses RFC 3339 format.
  name: createTime
  type: string
- description: Timestamp of when the project was last modified. Output only. Uses RFC 3339 format.
  name: updateTime
  type: string
- description: Timestamp of when the delete request was sent. Only present when the project is in DELETE_REQUESTED state. Output only.
  name: deleteTime
  type: string
- description: A checksum computed by the server based on the current value of the project resource. Used for optimistic concurrency control.
  name: etag
  type: string
- description: User-defined labels associated with the project. Label keys must be between 1 and 63 characters, and label values must be between 0 and 63 characters. Both keys and values can contain lowercase letter
  name: labels
  type: object
provider_name: Google Cloud Platform
provider_slug: google-cloud-platform
schema_file: json-schema/cloud-resource-manager-project-schema.json
slug: cloud-resource-manager-project
tags:
- API Management
- Cloud Computing
- Infrastructure
- Platform as a Service
title: Project
---
