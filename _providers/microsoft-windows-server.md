---
api_count: 16
apis:
- description: PowerShell and WMI-based management APIs for Windows Server administration.
  name: Windows Server Management API
  slug: ''
- description: WS-Management protocol implementation for remote management of Windows servers using SOAP-based web services for configuration and operations.
  name: Windows Remote Management (WinRM)
  slug: ''
- description: LDAP and REST APIs for Active Directory management and authentication.
  name: Active Directory Domain Services API
  slug: ''
- description: APIs for managing Hyper-V virtualization platform including virtual machines, virtual switches, and virtual storage.
  name: Hyper-V Management API
  slug: ''
- description: APIs for managing Windows updates across enterprise environments.
  name: Windows Server Update Services (WSUS) API
  slug: ''
- description: Modern web-based management interface REST API for Windows Server that provides a gateway service for relaying commands and scripts to managed nodes.
  name: Windows Admin Center API
  slug: ''
- description: APIs for managing Windows DNS Server services.
  name: DNS Server Management API
  slug: ''
- description: Infrastructure for management data and operations on Windows-based operating systems providing COM, scripting, and .NET APIs for system administration and monitoring.
  name: Windows Management Instrumentation (WMI) API
  slug: ''
- description: REST API for managing Internet Information Services (IIS) web servers that enables configuration and monitoring from any HTTP client.
  name: IIS Administration API
  slug: ''
- description: Win32 API for managing Remote Desktop Services including session management, virtual channels, user configuration, and the Remote Desktop Protocol.
  name: Remote Desktop Services API
  slug: ''
- description: APIs for defining and managing software and hardware components on failover clusters to increase application scalability and availability.
  name: Failover Clustering API
  slug: ''
- description: APIs and PowerShell cmdlets for managing Dynamic Host Configuration Protocol server services including leases, reservations, and scopes.
  name: DHCP Server Management API
  slug: ''
- description: Server Message Block protocol APIs and WMI management classes for managing file shares, share access, and network file sharing across Windows Server environments.
  name: SMB File Server API
  slug: ''
- description: API for instrumenting, querying, and consuming event logs on Windows Server for diagnostics, monitoring, and auditing.
  name: Windows Event Log API
  slug: ''
- description: APIs and PowerShell management for software-defined storage enabling clustering of servers with internal storage for hyper-converged infrastructure.
  name: Storage Spaces Direct API
  slug: ''
- description: Network Policy Server providing centralized RADIUS authentication, authorization, and accounting for wireless, VPN, and dial-up connections.
  name: Network Policy Server (NPS) RADIUS API
  slug: ''
capabilities:
- description: Unified workflow for IT administrators to manage IIS web sites, applications, and application pools for enterprise web hosting on Windows Server.
  name: Windows Server Web Management
  slug: web-server-management
common:
- title: ''
  type: Portal
  url: https://portal.azure.com
- title: ''
  type: Documentation
  url: https://docs.microsoft.com/windows-server/
- title: ''
  type: Support
  url: https://support.microsoft.com/windows-server
- title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/windows-server/bg-p/WindowsServer
- title: ''
  type: TermsOfService
  url: https://www.microsoft.com/licensing/terms/
- title: ''
  type: ReleaseNotes
  url: https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/privacystatement
- title: ''
  type: GitHubRepository
  url: https://github.com/MicrosoftDocs/windowsserverdocs
- title: ''
  type: Security
  url: https://learn.microsoft.com/en-us/windows-server/security/tls/tls-ssl-schannel-ssp-overview
- title: ''
  type: NaftikoCapability
  url: capabilities/web-server-management.yaml
created: '2024'
description: APIs and integration points for Microsoft Windows Server operating system including management, networking, storage, virtualization, security, and remote administration capabilities for enterprise server infrastructure.
features:
- description: REST API for managing IIS web sites, applications, and application pools with full CRUD operations and configuration management.
  name: Web Server Management
- description: LDAP and API-based management of directory services, user authentication, group policies, and domain controllers.
  name: Active Directory Services
- description: Create, manage, and monitor virtual machines, virtual switches, and storage with PowerShell and WMI APIs.
  name: Hyper-V Virtualization
- description: Manage servers remotely through WinRM, PowerShell Remoting, Windows Admin Center, and Remote Desktop Services.
  name: Remote Server Administration
- description: High availability clustering with automatic failover for critical workloads including SQL Server, Hyper-V, and file servers.
  name: Failover Clustering
- description: Storage Spaces Direct for hyper-converged infrastructure with pool management, tiering, and resilient storage volumes.
  name: Software-Defined Storage
- description: Network infrastructure services with APIs for DNS zone management and DHCP scope configuration.
  name: DNS and DHCP Services
- description: RADIUS authentication via NPS, TLS/SSL management, Windows Event Log auditing, and security policy enforcement.
  name: Security and Compliance
image: /assets/icons/microsoft-windows-server.png
integrations:
- description: Extend on-premises Windows Server to Azure with Azure Arc, Azure Backup, Azure Site Recovery, and hybrid networking.
  name: Microsoft Azure
- description: Enterprise management with System Center Configuration Manager, Operations Manager, and Virtual Machine Manager.
  name: System Center
- description: Integrated security with Microsoft Defender for Servers, threat detection, and vulnerability management.
  name: Microsoft Defender
- description: Enable single sign-on and federated identity across on-premises and cloud applications with ADFS.
  name: Active Directory Federation Services
- description: Collect and analyze Windows Server performance metrics, logs, and diagnostics in Azure Monitor.
  name: Azure Monitor
jsonld:
- class_count: 0
  name: Iis Administration Context
  property_count: 0
  slug: iis-administration-context
- class_count: 0
  name: Microsoft Windows Server Context
  property_count: 3
  slug: microsoft-windows-server-context
layout: provider
modified: '2026-04-19'
name: Microsoft Windows Server
rules:
- name: Microsoft Windows Server API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: microsoft-windows-server-spectral-rules
skills: []
slug: microsoft-windows-server
solutions: []
tags:
- Datacenter
- Enterprise
- Infrastructure
- Microsoft
- Operating System
- Server Management
- Windows Server
- Windows Server 2025
url: https://www.microsoft.com/windows-server
use_cases:
- description: Deploy and manage web applications on IIS with automated site provisioning, SSL certificate management, and application pool isolation.
  name: Enterprise Web Hosting
- description: Automate server provisioning, configuration management, and patch deployment using PowerShell, WMI, and REST APIs.
  name: Infrastructure Automation
- description: Manage on-premises Windows Server infrastructure alongside Azure resources through Windows Admin Center and Azure Arc.
  name: Hybrid Cloud Management
- description: Deploy and manage Remote Desktop Services for virtual desktop and application delivery to remote workers.
  name: Virtual Desktop Infrastructure
- description: Configure failover clustering and storage replication for mission-critical applications requiring zero downtime.
  name: High Availability Deployments
---
