---
api_count: 26
apis:
- description: Main REST API for managing OpenShift clusters, projects, and resources.
  name: OpenShift REST API
  slug: openshift-rest-api
- description: OAuth authentication and authorization API for OpenShift.
  name: OpenShift OAuth API
  slug: openshift-oauth-api
- description: API for managing application routes and ingress.
  name: OpenShift Routes API
  slug: openshift-routes-api
- description: API for managing application builds and build configurations.
  name: OpenShift Build API
  slug: openshift-build-api
- description: API for managing container images and image streams.
  name: OpenShift Image API
  slug: openshift-image-api
- description: API for managing OpenShift projects (namespace extensions).
  name: OpenShift Project API
  slug: openshift-project-api
- description: API for managing workload resources including Pods, Deployments, DeploymentConfigs, StatefulSets, Jobs, CronJobs, ReplicaSets, and DaemonSets.
  name: OpenShift Workloads API
  slug: openshift-workloads-api
- description: API for managing network configuration including Services, Endpoints, Ingress, NetworkPolicy, and EgressFirewall resources.
  name: OpenShift Network API
  slug: openshift-network-api
- description: API for managing storage resources including PersistentVolumes, PersistentVolumeClaims, StorageClasses, CSI drivers, and VolumeSnapshots.
  name: OpenShift Storage API
  slug: openshift-storage-api
- description: API for managing authorization resources including SubjectAccessReview, SelfSubjectAccessReview, LocalSubjectAccessReview, and TokenReview.
  name: OpenShift Authorization API
  slug: openshift-authorization-api
- description: API for managing autoscaling resources including HorizontalPodAutoscaler, ClusterAutoscaler, and MachineAutoscaler.
  name: OpenShift Autoscale API
  slug: openshift-autoscale-api
- description: API for managing cluster configuration resources including APIServer, Authentication, Infrastructure, Ingress, Network, OAuth, and Scheduler configuration.
  name: OpenShift Config API
  slug: openshift-config-api
- description: API for managing OpenShift web console extensions including ConsoleCLIDownload, ConsoleExternalLogLink, ConsoleLink, ConsoleNotification, and ConsolePlugin.
  name: OpenShift Console API
  slug: openshift-console-api
- description: API for managing cluster-level resources including ClusterVersion, ClusterOperator, and infrastructure resources.
  name: OpenShift Cluster API
  slug: openshift-cluster-api
- description: API for managing machine resources including Machine, MachineSet, MachineHealthCheck, and MachineAutoscaler for cluster node lifecycle management.
  name: OpenShift Machine API
  slug: openshift-machine-api
- description: API for managing OpenShift operator lifecycle and configuration including Etcd, Console, Network, DNS, IngressController, and other operator resources.
  name: OpenShift Operator API
  slug: openshift-operator-api
- description: API for managing OperatorHub resources including CatalogSources, Subscriptions, InstallPlans, and ClusterServiceVersions for the Operator Lifecycle Manager.
  name: OpenShift OperatorHub API
  slug: openshift-operatorhub-api
- description: API for managing templates that provide parameterized sets of objects for creating applications and services.
  name: OpenShift Template API
  slug: openshift-template-api
- description: API for managing security resources including SecurityContextConstraints, RangeAllocation, and PodSecurityPolicyReview for controlling pod security.
  name: OpenShift Security API
  slug: openshift-security-api
- description: API for managing role-based access control resources including Roles, ClusterRoles, RoleBindings, and ClusterRoleBindings.
  name: OpenShift RBAC API
  slug: openshift-rbac-api
- description: API for managing node-level resources including Node, RuntimeClass, and node configuration.
  name: OpenShift Node API
  slug: openshift-node-api
- description: API for managing monitoring and observability resources including Prometheus, Alertmanager, ServiceMonitor, and PrometheusRule.
  name: OpenShift Monitoring API
  slug: openshift-monitoring-api
- description: API for managing bare metal and infrastructure provisioning resources including BareMetalHost, Provisioning, and hardware management.
  name: OpenShift Provisioning API
  slug: openshift-provisioning-api
- description: API for managing scheduling and quota resources including ResourceQuota, LimitRange, PriorityClass, and ClusterResourceQuota.
  name: OpenShift Schedule and Quota API
  slug: openshift-schedule-and-quota-api
- description: API for managing metadata resources including ConfigMaps, Secrets, Events, Namespaces, and ServiceAccounts.
  name: OpenShift Metadata API
  slug: openshift-metadata-api
- description: Managed service API for installing, modifying, operating, and upgrading Red Hat OpenShift clusters across cloud providers.
  name: OpenShift Cluster Manager API
  slug: openshift-cluster-manager-api
capabilities:
- description: Unified platform management capability for OpenShift clusters including projects, builds, deployments, routes, and monitoring. Used by platform engineers and cluster administrators.
  name: OpenShift Platform Management
  slug: platform-management
common:
- title: ''
  type: GettingStarted
  url: https://www.openshift.com/try
- title: ''
  type: Blog
  url: https://www.openshift.com/blog
- title: ''
  type: GitHubOrganization
  url: https://github.com/openshift
- title: ''
  type: TermsOfService
  url: https://www.redhat.com/en/about/terms-use
- title: ''
  type: PrivacyPolicy
  url: https://www.redhat.com/en/about/privacy-policy
- title: ''
  type: ChangeLog
  url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/release_notes/ocp-4-17-release-notes
- title: ''
  type: Login
  url: https://console.redhat.com/openshift
created: '2024-01-01'
description: A comprehensive API definition for Red Hat OpenShift, the enterprise Kubernetes platform.
features:
- description: Production-grade Kubernetes platform with built-in security, monitoring, and lifecycle management.
  name: Enterprise Kubernetes
- description: Automated container image builds directly from source code repositories.
  name: Source-to-Image Builds
- description: Lifecycle management for complex applications through Kubernetes Operators and OperatorHub.
  name: Operator Framework
- description: Centralized management of multiple OpenShift clusters across cloud providers.
  name: Multi-Cluster Management
- description: Integrated Prometheus, Alertmanager, and Grafana for cluster and application observability.
  name: Built-in Monitoring
image: /assets/icons/openshift.png
integrations:
- description: Native integration with AWS (ROSA), Azure (ARO), GCP, and IBM Cloud for managed deployments.
  name: Cloud Providers
- description: Integration with Jenkins, Tekton, GitLab CI, and GitHub Actions for automated pipelines.
  name: CI/CD Tools
- description: Integration with Istio-based service mesh for traffic management, security, and observability.
  name: Service Mesh
jsonld:
- class_count: 0
  name: Openshift Context
  property_count: 16
  slug: openshift-context
- class_count: 0
  name: Openshift Rest Context
  property_count: 0
  slug: openshift-rest-context
layout: provider
modified: '2026-04-18'
name: OpenShift
rules:
- name: OpenShift API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: openshift-spectral-rules
skills: []
slug: openshift
solutions: []
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
url: https://raw.githubusercontent.com/api-evangelist/openshift/refs/heads/main/apis.yml
use_cases:
- description: Migrate monolithic applications to containerized microservices on Kubernetes.
  name: Application Modernization
- description: Automate build, test, and deployment workflows with integrated pipeline capabilities.
  name: CI/CD Pipelines
- description: Deploy and manage applications at edge locations with lightweight OpenShift deployments.
  name: Edge Computing
- description: Run consistent workloads across on-premise, public cloud, and edge environments.
  name: Hybrid Cloud Deployment
---
