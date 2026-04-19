---
api_count: 4
apis:
- description: REST API for managing InfoScale clusters, storage resources, and high availability configurations. Supports storage configuration and management operations including disk groups, volumes, and file sys
  name: Veritas InfoScale REST API
  slug: rest-api
- description: REST API for centralized monitoring and management of InfoScale environments. Provides meta, query, update, and operational endpoints for managing clusters, service groups, hosts, storage, and extende
  name: Veritas InfoScale Operations Manager API
  slug: operations-manager-api
- description: 'API for managing VCS clusters, service groups, and resources within InfoScale. Provides operations for cluster node management, service group failover and failback, resource dependency configuration, '
  name: Veritas Cluster Server API
  slug: vcs-api
- description: API for storage volume management, including volume creation, resizing, mirroring, and snapshot operations. Manages disk groups, plexes, subdisks, and provides advanced storage features like thin prov
  name: Veritas Volume Manager API
  slug: vxvm-api
capabilities:
- description: Unified infrastructure management workflow combining the Veritas InfoScale REST API for managing clusters, service groups, storage volumes, disk groups, and alerts. Used by infrastructure engineers, s
  name: Veritas InfoScale Infrastructure Management
  slug: infrastructure-management
common:
- title: ''
  type: Portal
  url: https://my.veritas.com
- title: ''
  type: Support
  url: https://www.veritas.com/support
- title: ''
  type: KnowledgeCenter
  url: https://www.veritas.com/support/en_US/dpp.InfoScaleStorageFoundation
- title: ''
  type: Documentation
  url: https://sort.veritas.com
- title: ''
  type: GettingStarted
  url: https://sort.veritas.com/infoscale/intro
- title: ''
  type: Training
  url: https://www.veritas.com/support/training
- title: ''
  type: Blog
  url: https://vox.veritas.com
- title: ''
  type: GitHubOrganization
  url: https://github.com/VeritasOS
- title: InfoScale Ansible Playbooks
  type: GitHubRepository
  url: https://github.com/VeritasOS/infoscale_ansible
- title: ''
  type: TermsOfService
  url: https://www.veritas.com/company/legal/terms-of-use
- title: ''
  type: PrivacyPolicy
  url: https://www.veritas.com/company/legal/privacy
- title: ''
  type: Contact
  url: https://www.veritas.com/form/requestacall
- title: ''
  type: Pricing
  url: https://sort.veritas.com/license_calc
- title: ''
  type: ReleaseNotes
  url: https://www.veritas.com/support/en_US/doc/infoscale
- title: ''
  type: SpectralRules
  url: rules/veritas-infoscale-spectral-rules.yml
- title: Infrastructure Management
  type: NaftikoCapability
  url: capabilities/infrastructure-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/veritas-infoscale-vocabulary.yaml
created: '2025-03-14'
description: APIs for Veritas InfoScale, an enterprise storage and availability management solution that provides high availability, disaster recovery, and storage management capabilities across physical, virtual, and cloud environments.
features:
- description: Provides application-aware clustering with automatic failover and failback to ensure continuous availability of mission-critical applications.
  name: High Availability Clustering
- description: Uses asynchronous event-based monitoring (IMF) to detect failures instantaneously, eliminating CPU overhead of legacy poll-based monitoring.
  name: Intelligent Monitoring Framework
- description: Software-defined storage services for volume management, thin provisioning, data migration, and multi-pathing across heterogeneous storage arrays.
  name: Storage Management
- description: Volume replication (VVR) and file replication (VFR) for real-time data replication across sites with automated disaster recovery orchestration.
  name: Disaster Recovery
- description: Space-optimized snapshots for backup, data analytics, forensic discovery, and point-in-time recovery without impacting production workloads.
  name: Snapshot Management
- description: Native CSI driver providing persistent storage on DAS and SAN with data integrity using I/O fencing for Kubernetes and OpenShift environments.
  name: Kubernetes Integration
- description: Deployment on AWS, Azure, Google Cloud, and Oracle Cloud with solution templates and marketplace offerings for elastic scaling.
  name: Cloud Deployment
- description: Full REST API support for control plane operations enabling automation and integration with DevOps pipelines and orchestration tools.
  name: REST API Management
image: /assets/icons/veritas-infoscale.png
integrations:
- description: Deep integration with Oracle RAC and single-instance databases for storage management, availability, and disaster recovery.
  name: Oracle Database
- description: Certified integration with SAP HANA and SAP applications for high availability and disaster recovery in enterprise environments.
  name: SAP Applications
- description: High availability and storage management for SQL Server Always On availability groups and failover cluster instances.
  name: Microsoft SQL Server
- description: Integration with VMware vSphere and vSAN for virtualized application availability and storage management.
  name: VMware vSphere
- description: CSI driver integration for persistent storage provisioning and management in container orchestration platforms.
  name: Kubernetes and OpenShift
- description: Ansible modules for automated deployment, configuration, and management of InfoScale environments in DevOps pipelines.
  name: Ansible Automation
- description: SRDF MetroCluster support with Dell EMC PowerMax and vMAX arrays for storage replication and disaster recovery.
  name: Dell EMC Storage
- description: Cloud marketplace offerings and solution templates for deployment on Amazon Web Services and Microsoft Azure platforms.
  name: AWS and Azure
jsonld:
- class_count: 10
  name: Veritas Infoscale Rest Api Context
  property_count: 38
  slug: veritas-infoscale-rest-api-context
layout: provider
modified: '2026-04-18'
name: Veritas InfoScale
rules:
- name: Veritas InfoScale API Rules
  rule_count: 39
  severity_counts:
    error: 23
    hint: 0
    info: 6
    warn: 10
  slug: veritas-infoscale-spectral-rules
skills: []
slug: veritas-infoscale
solutions: []
tags:
- Clustering
- Data Management
- Disaster Recovery
- High Availability
- Storage Management
- Virtualization
url: https://raw.githubusercontent.com/api-evangelist/veritas-infoscale/refs/heads/main/apis.yml
use_cases:
- description: Ensure zero-downtime for mission-critical applications like Oracle, SAP, and SQL Server with automatic failover and health monitoring.
  name: Application High Availability
- description: Automate cross-site replication and recovery orchestration to meet RPO and RTO requirements for business continuity planning.
  name: Disaster Recovery Automation
- description: Consolidate heterogeneous storage arrays into a unified software-defined storage layer with volume management.
  name: Storage Consolidation
- description: Migrate on-premises applications to cloud environments with consistent storage and availability management across hybrid infrastructure.
  name: Cloud Migration
- description: Provide enterprise-grade persistent storage for containerized applications on Kubernetes and OpenShift with CSI driver integration.
  name: Container Storage
- description: Protect databases with application-consistent snapshots, online data migration, and real-time replication without application downtime.
  name: Database Protection
---
