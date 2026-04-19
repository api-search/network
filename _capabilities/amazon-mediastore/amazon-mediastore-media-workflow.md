---
consumed_apis:
- mediastore
description: Workflow capability for Amazon MediaStore media processing operations for broadcast engineers and media developers.
layout: capability
name: Amazon MediaStore Workflow
operations:
- description: List jobs
  method: GET
  name: list-jobs
  path: /v1/jobs
personas: []
provider_name: Amazon MediaStore
provider_slug: amazon-mediastore
search_terms:
- deletelifecyclepolicy
- describecontainer
- list jobs
- delete lifecycle policy
- delete metric policy
- delete cors policy
- manage media processing jobs
- deletecontainerpolicy
- describe container
- deletecorspolicy
- engineer managing broadcast media workflows
- broadcasting
- Broadcast Engineer
- createcontainer
- amazon mediastore media processing workflow
- Media Developer
- create container
- deletemetricpolicy
- workflow
- media processing
- delete container policy
- aws
- aws media processing and delivery
- deletecontainer
- media
- getcontainerpolicy
- get container policy
- delete container
- developer building media processing applications
slug: amazon-mediastore-media-workflow
tags:
- AWS
- Media
- Broadcasting
- Workflow
tools:
- description: CreateContainer
  hints:
    openWorld: true
    readOnly: false
  name: create-container
- description: DeleteContainer
  hints:
    openWorld: true
    readOnly: false
  name: delete-container
- description: DeleteContainerPolicy
  hints:
    openWorld: true
    readOnly: false
  name: delete-container-policy
- description: DeleteCorsPolicy
  hints:
    openWorld: true
    readOnly: false
  name: delete-cors-policy
- description: DeleteLifecyclePolicy
  hints:
    openWorld: true
    readOnly: false
  name: delete-lifecycle-policy
- description: DeleteMetricPolicy
  hints:
    openWorld: true
    readOnly: false
  name: delete-metric-policy
- description: DescribeContainer
  hints:
    openWorld: true
    readOnly: false
  name: describe-container
- description: GetContainerPolicy
  hints:
    openWorld: true
    readOnly: false
  name: get-container-policy
---
