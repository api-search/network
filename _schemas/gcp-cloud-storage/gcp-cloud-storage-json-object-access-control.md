---
description: An access-control entry for an object.
layout: schema
name: ObjectAccessControl
properties_list:
- description: The kind of item this is.
  name: kind
  type: string
- description: The ID of the access-control entry.
  name: id
  type: string
- description: The link to this access-control entry.
  name: selfLink
  type: string
- description: The name of the bucket.
  name: bucket
  type: string
- description: The name of the object.
  name: object
  type: string
- description: The content generation of the object.
  name: generation
  type: string
- description: 'The entity holding the permission, in one of the following forms: user-userId, user-email, group-groupId, group-email, domain-domain, project-team-projectId, allUsers, or allAuthenticatedUsers.'
  name: entity
  type: string
- description: The access permission for the entity.
  name: role
  type: string
- description: The email address associated with the entity, if any.
  name: email
  type: string
- description: The domain associated with the entity, if any.
  name: domain
  type: string
- description: The ID for the entity, if any.
  name: entityId
  type: string
- description: HTTP 1.1 Entity tag for the access-control entry.
  name: etag
  type: string
- description: The project team associated with the entity, if any.
  name: projectTeam
  type: object
provider_name: Google Cloud Storage
provider_slug: gcp-cloud-storage
schema_file: json-schema/gcp-cloud-storage-json-object-access-control-schema.json
slug: gcp-cloud-storage-json-object-access-control
tags:
- Archival
- Backup
- Blob Storage
- Cloud Storage
- Data
- File Storage
- Google Cloud
- Object Storage
- Storage
title: ObjectAccessControl
---
