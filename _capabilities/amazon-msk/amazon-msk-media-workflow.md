---
consumed_apis:
- msk
description: Workflow capability for Amazon MSK media processing operations for broadcast engineers and media developers.
layout: capability
name: Amazon MSK Workflow
operations:
- description: List jobs
  method: GET
  name: list-jobs
  path: /v1/jobs
personas: []
provider_name: Amazon MSK
provider_slug: amazon-msk
search_terms:
- developer building media processing applications
- engineer managing broadcast media workflows
- list jobs
- media
- list clusters v2
- aws media processing and delivery
- list scram secrets
- broadcasting
- create cluster v2
- list clusters
- listconfigurations
- create cluster
- listclustersv2
- createclusterv2
- list configurations
- listscramsecrets
- createcluster
- Media Developer
- aws
- batch disassociate scram secret
- amazon msk media processing workflow
- workflow
- Broadcast Engineer
- media processing
- manage media processing jobs
- batch associate scram secret
- listclusters
- batchassociatescramsecret
- batchdisassociatescramsecret
slug: amazon-msk-media-workflow
tags:
- AWS
- Media
- Broadcasting
- Workflow
tools:
- description: ListScramSecrets
  hints:
    openWorld: true
    readOnly: true
  name: list-scram-secrets
- description: BatchAssociateScramSecret
  hints:
    openWorld: true
    readOnly: false
  name: batch-associate-scram-secret
- description: BatchDisassociateScramSecret
  hints:
    openWorld: true
    readOnly: false
  name: batch-disassociate-scram-secret
- description: ListClusters
  hints:
    openWorld: true
    readOnly: true
  name: list-clusters
- description: CreateCluster
  hints:
    openWorld: true
    readOnly: false
  name: create-cluster
- description: ListClustersV2
  hints:
    openWorld: true
    readOnly: true
  name: list-clusters-v2
- description: CreateClusterV2
  hints:
    openWorld: true
    readOnly: false
  name: create-cluster-v2
- description: ListConfigurations
  hints:
    openWorld: true
    readOnly: true
  name: list-configurations
---
