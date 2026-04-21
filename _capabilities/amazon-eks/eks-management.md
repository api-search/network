---
consumed_apis:
- eks
description: Unified capability for managing EKS clusters, node groups, Fargate profiles, and add-ons for platform engineers.
layout: capability
name: Amazon EKS Kubernetes Cluster Management
operations:
- description: Amazon EKS List EKS Clusters
  method: GET
  name: ListClusters
  path: /v1/clusters
- description: Amazon EKS Create a New EKS Cluster
  method: POST
  name: CreateCluster
  path: /v1/clusters
- description: Amazon EKS Describe an EKS Cluster
  method: GET
  name: DescribeCluster
  path: /v1/clusters
- description: Amazon EKS Delete an EKS Cluster
  method: DELETE
  name: DeleteCluster
  path: /v1/clusters
- description: Amazon EKS List Managed Node Groups
  method: GET
  name: ListNodegroups
  path: /v1/clusters/node-groups
- description: Amazon EKS Create a Managed Node Group
  method: POST
  name: CreateNodegroup
  path: /v1/clusters/node-groups
- description: Amazon EKS Describe a Managed Node Group
  method: GET
  name: DescribeNodegroup
  path: /v1/clusters/node-groups
- description: Amazon EKS Delete a Managed Node Group
  method: DELETE
  name: DeleteNodegroup
  path: /v1/clusters/node-groups
- description: Amazon EKS List Fargate Profiles
  method: GET
  name: ListFargateProfiles
  path: /v1/clusters/fargate-profiles
- description: Amazon EKS Create a Fargate Profile
  method: POST
  name: CreateFargateProfile
  path: /v1/clusters/fargate-profiles
personas: []
provider_name: Amazon EKS
provider_slug: amazon-eks
search_terms:
- list nodegroups
- CreateFargateProfile
- ListFargateProfiles
- create fargate profile
- DeleteCluster
- ListNodegroups
- amazon eks delete an eks cluster
- kubernetes
- DescribeCluster
- amazon eks delete a managed node group
- delete nodegroup
- describe nodegroup
- eks
- list clusters
- ListClusters
- amazon eks describe an eks cluster
- workflow capability for kubernetes platform management.
- create nodegroup
- amazon eks list managed node groups
- create cluster
- list fargate profiles
- describe cluster
- CreateCluster
- amazon eks
- amazon eks describe a managed node group
- amazon eks list eks clusters
- DescribeNodegroup
- containers
- aws
- amazon eks create a new eks cluster
- CreateNodegroup
- container orchestration
- amazon eks create a fargate profile
- delete cluster
- kubernetes platform management business domain for amazon eks.
- DeleteNodegroup
- amazon eks list fargate profiles
- engineers managing amazon eks resources on aws.
- amazon eks create a managed node group
slug: eks-management
tags:
- Amazon EKS
- AWS
- Kubernetes
- Container Orchestration
tools:
- description: Amazon EKS List EKS Clusters
  hints:
    destructive: false
    readOnly: true
  name: list-clusters
- description: Amazon EKS Create a New EKS Cluster
  hints:
    destructive: false
    readOnly: false
  name: create-cluster
- description: Amazon EKS Describe an EKS Cluster
  hints:
    destructive: false
    readOnly: true
  name: describe-cluster
- description: Amazon EKS Delete an EKS Cluster
  hints:
    destructive: true
    readOnly: false
  name: delete-cluster
- description: Amazon EKS List Managed Node Groups
  hints:
    destructive: false
    readOnly: true
  name: list-nodegroups
- description: Amazon EKS Create a Managed Node Group
  hints:
    destructive: false
    readOnly: false
  name: create-nodegroup
- description: Amazon EKS Describe a Managed Node Group
  hints:
    destructive: false
    readOnly: true
  name: describe-nodegroup
- description: Amazon EKS Delete a Managed Node Group
  hints:
    destructive: true
    readOnly: false
  name: delete-nodegroup
- description: Amazon EKS List Fargate Profiles
  hints:
    destructive: false
    readOnly: true
  name: list-fargate-profiles
- description: Amazon EKS Create a Fargate Profile
  hints:
    destructive: false
    readOnly: false
  name: create-fargate-profile
---
