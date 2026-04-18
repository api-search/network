---
consumed_apis:
- oci-compute
description: Manage Oracle Cloud Infrastructure compute resources including instances, images, shapes, and attachments. Used by cloud engineers and platform administrators.
layout: capability
name: Oracle Cloud Compute Management
operations:
- description: List compute instances in a compartment
  method: GET
  name: list-instances
  path: /v1/instances
- description: Launch a new compute instance
  method: POST
  name: launch-instance
  path: /v1/instances
- description: Get instance details
  method: GET
  name: get-instance
  path: /v1/instances/{instanceId}
- description: Update instance details
  method: PUT
  name: update-instance
  path: /v1/instances/{instanceId}
- description: Terminate an instance
  method: DELETE
  name: terminate-instance
  path: /v1/instances/{instanceId}
- description: List available compute shapes
  method: GET
  name: list-shapes
  path: /v1/shapes
- description: List compute images
  method: GET
  name: list-images
  path: /v1/images
- description: Create a custom image
  method: POST
  name: create-image
  path: /v1/images
- description: Get image details
  method: GET
  name: get-image
  path: /v1/images/{imageId}
- description: Update image details
  method: PUT
  name: update-image
  path: /v1/images/{imageId}
- description: Delete a custom image
  method: DELETE
  name: delete-image
  path: /v1/images/{imageId}
personas: []
provider_name: Oracle
provider_slug: oracle
search_terms:
- get instance
- launch instance
- compute
- launch a new compute instance
- update image
- get image details
- list volume attachments
- list instances
- manage a specific image
- delete image
- list compute images
- list images
- database
- oracle
- infrastructure
- cloud
- update instance
- update image details
- perform an action on an instance (start, stop, reset)
- get details of a specific image
- saas
- list instance console connections
- update instance details
- list console connections
- delete a custom image
- list compute instances in a compartment
- list shapes
- manage a specific compute instance
- enterprise
- list vnic attachments
- manage compute images
- list volume attachments in a compartment
- get image
- create image
- get details of a specific instance
- instance action
- list available compute shapes
- create a custom image from an instance
- create a custom image
- list vnic attachments in a compartment
- get instance details
- terminate instance
- terminate an instance
- manage compute instances
slug: cloud-compute
tags:
- Oracle
- Cloud
- Compute
- Infrastructure
tools:
- description: List compute instances in a compartment
  hints:
    openWorld: true
    readOnly: true
  name: list-instances
- description: Launch a new compute instance
  hints:
    readOnly: false
  name: launch-instance
- description: Get details of a specific instance
  hints:
    readOnly: true
  name: get-instance
- description: Update instance details
  hints:
    idempotent: true
    readOnly: false
  name: update-instance
- description: Terminate an instance
  hints:
    destructive: true
    idempotent: true
  name: terminate-instance
- description: Perform an action on an instance (start, stop, reset)
  hints:
    readOnly: false
  name: instance-action
- description: List available compute shapes
  hints:
    readOnly: true
  name: list-shapes
- description: List compute images
  hints:
    readOnly: true
  name: list-images
- description: Create a custom image from an instance
  hints:
    readOnly: false
  name: create-image
- description: Get details of a specific image
  hints:
    readOnly: true
  name: get-image
- description: Update image details
  hints:
    idempotent: true
    readOnly: false
  name: update-image
- description: Delete a custom image
  hints:
    destructive: true
    idempotent: true
  name: delete-image
- description: List VNIC attachments in a compartment
  hints:
    readOnly: true
  name: list-vnic-attachments
- description: List volume attachments in a compartment
  hints:
    readOnly: true
  name: list-volume-attachments
- description: List instance console connections
  hints:
    readOnly: true
  name: list-console-connections
---
