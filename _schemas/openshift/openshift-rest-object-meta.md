---
description: Standard Kubernetes object metadata. Every resource includes metadata such as name, namespace, labels, and annotations.
layout: schema
name: ObjectMeta
properties_list:
- description: The name of the resource, unique within a namespace.
  name: name
  type: string
- description: The namespace in which the resource resides.
  name: namespace
  type: string
- description: A unique identifier for the resource set by the server.
  name: uid
  type: string
- description: An opaque value representing the internal version of the object.
  name: resourceVersion
  type: string
- description: A sequence number representing a specific generation of the desired state.
  name: generation
  type: integer
- description: Timestamp representing when the object was created.
  name: creationTimestamp
  type: string
- description: Timestamp at which the object will be deleted.
  name: deletionTimestamp
  type: string
- description: Map of string keys and values that can be used to organize and categorize objects.
  name: labels
  type: object
- description: Unstructured key-value map stored with a resource for arbitrary metadata.
  name: annotations
  type: object
- description: List of objects depended by this object.
  name: ownerReferences
  type: array
- description: Must be empty before the object is deleted from the registry.
  name: finalizers
  type: array
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-object-meta-schema.json
slug: openshift-rest-object-meta
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: ObjectMeta
---
