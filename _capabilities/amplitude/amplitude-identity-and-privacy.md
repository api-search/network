---
consumed_apis:
- dsar-api
- scim-api
- user-mapping-api
description: SCIM provisioning and privacy compliance. For IT admins and compliance teams.
layout: capability
name: Amplitude Identity and Privacy
operations:
- description: Amplitude Create a Data Subject Access Request
  method: POST
  name: createDsarRequest
  path: /v1/data-access
- description: Amplitude Get DSAR Request Status
  method: GET
  name: getDsarRequestStatus
  path: /v1/data-access
- description: Amplitude List Deletion Requests
  method: GET
  name: listDeletionRequests
  path: /v1/data-deletion
- description: Amplitude Request User Data Deletion
  method: POST
  name: createDeletionRequest
  path: /v1/data-deletion
- description: Amplitude List SCIM Users
  method: GET
  name: listScimUsers
  path: /v1/users
- description: Amplitude Create a SCIM User
  method: POST
  name: createScimUser
  path: /v1/users
- description: Amplitude Get a SCIM User
  method: GET
  name: getScimUser
  path: /v1/users
- description: Amplitude Replace a SCIM User
  method: PUT
  name: replaceScimUser
  path: /v1/users
- description: Amplitude Update a SCIM User
  method: PATCH
  name: updateScimUser
  path: /v1/users
- description: Amplitude Delete a SCIM User
  method: DELETE
  name: deleteScimUser
  path: /v1/users
- description: Amplitude List SCIM Groups
  method: GET
  name: listScimGroups
  path: /v1/groups
- description: Amplitude Create a SCIM Group
  method: POST
  name: createScimGroup
  path: /v1/groups
- description: Amplitude Get a SCIM Group
  method: GET
  name: getScimGroup
  path: /v1/groups
- description: Amplitude Update a SCIM Group
  method: PATCH
  name: updateScimGroup
  path: /v1/groups
- description: Amplitude Delete a SCIM Group
  method: DELETE
  name: deleteScimGroup
  path: /v1/groups
- description: Amplitude Map User Identities
  method: POST
  name: mapUser
  path: /v1/user-mapping
- description: Amplitude Unmap User Identities
  method: POST
  name: unmapUser
  path: /v1/user-mapping
personas: []
provider_name: Amplitude
provider_slug: amplitude
search_terms:
- getScimUser
- scim provisioning and privacy compliance. for it admins and compliance teams.
- manage and evaluate a/b experiments and feature flags. for product managers.
- identity management
- scim api deleteScimGroup
- manages privacy and compliance
- amplitude list deletion requests
- replaceScimUser
- amplitude create a scim user
- analytics
- scim api getScimUser
- scim api createScimGroup
- amplitude list scim groups
- amplitude create a scim group
- mapUser
- amplitude map user identities
- unmapUser
- amplitude unmap user identities
- export raw event data and manage behavioral cohorts. for data analysts.
- analyzes data and manages cohorts
- privacy compliance
- amplitude create a data subject access request
- createDsarRequest
- listScimGroups
- amplitude get a scim user
- amplitude replace a scim user
- amplitude delete a scim user
- feature flags
- getDsarRequestStatus
- listDeletionRequests
- experimentation
- deleteScimGroup
- data governance
- createDeletionRequest
- getScimGroup
- amplitude get dsar request status
- scim api deleteScimUser
- scim api listScimGroups
- createScimGroup
- scim api getScimGroup
- scim api replaceScimUser
- amplitude update a scim user
- dsar api getDsarRequestStatus
- product analytics
- dsar api createDsarRequest
- ingests and exports event data
- scim api createScimUser
- amplitude delete a scim group
- user mapping api mapUser
- manage event schemas and chart annotations. for data governance teams.
- amplitude update a scim group
- a/b testing
- amplitude request user data deletion
- updateScimGroup
- runs experiments and feature flags
- amplitude
- user mapping api unmapUser
- listScimUsers
- amplitude list scim users
- dsar api listDeletionRequests
- deleteScimUser
- scim api listScimUsers
- updateScimUser
- identity
- createScimUser
- unified workflow for sending events and identifying users. for data engineers.
- user behavior
- scim api updateScimGroup
- privacy
- amplitude get a scim group
- dsar api createDeletionRequest
- scim api updateScimUser
slug: amplitude-identity-and-privacy
tags:
- Amplitude
- Identity
- Privacy
tools:
- description: Amplitude Create a Data Subject Access Request
  hints:
    readOnly: false
  name: dsar-api-createDsarRequest
- description: Amplitude Get DSAR Request Status
  hints:
    readOnly: true
  name: dsar-api-getDsarRequestStatus
- description: Amplitude List Deletion Requests
  hints:
    readOnly: true
  name: dsar-api-listDeletionRequests
- description: Amplitude Request User Data Deletion
  hints:
    readOnly: false
  name: dsar-api-createDeletionRequest
- description: Amplitude List SCIM Users
  hints:
    readOnly: true
  name: scim-api-listScimUsers
- description: Amplitude Create a SCIM User
  hints:
    readOnly: false
  name: scim-api-createScimUser
- description: Amplitude Get a SCIM User
  hints:
    readOnly: true
  name: scim-api-getScimUser
- description: Amplitude Replace a SCIM User
  hints:
    readOnly: false
  name: scim-api-replaceScimUser
- description: Amplitude Update a SCIM User
  hints:
    readOnly: false
  name: scim-api-updateScimUser
- description: Amplitude Delete a SCIM User
  hints:
    readOnly: false
  name: scim-api-deleteScimUser
- description: Amplitude List SCIM Groups
  hints:
    readOnly: true
  name: scim-api-listScimGroups
- description: Amplitude Create a SCIM Group
  hints:
    readOnly: false
  name: scim-api-createScimGroup
- description: Amplitude Get a SCIM Group
  hints:
    readOnly: true
  name: scim-api-getScimGroup
- description: Amplitude Update a SCIM Group
  hints:
    readOnly: false
  name: scim-api-updateScimGroup
- description: Amplitude Delete a SCIM Group
  hints:
    readOnly: false
  name: scim-api-deleteScimGroup
- description: Amplitude Map User Identities
  hints:
    readOnly: false
  name: user-mapping-api-mapUser
- description: Amplitude Unmap User Identities
  hints:
    readOnly: false
  name: user-mapping-api-unmapUser
---
