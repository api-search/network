---
api_count: 21
apis:
- description: Native database engine APIs for connecting and executing queries against SQL Server.
  name: SQL Server Database Engine API
  slug: ''
- description: REST API for managing SQL Server resources in Azure.
  name: SQL Server REST API
  slug: ''
- description: .NET API for programmatically managing SQL Server instances and databases.
  name: SQL Server Management Objects (SMO)
  slug: ''
- description: REST API for managing and accessing SQL Server Reporting Services.
  name: SQL Server Reporting Services (SSRS) API
  slug: ''
- description: ODBC driver API for connecting applications to SQL Server.
  name: ODBC Driver for SQL Server
  slug: ''
- description: JDBC driver for connecting Java applications to SQL Server.
  name: JDBC Driver for SQL Server
  slug: ''
- description: APIs for managing and querying SQL Server Analysis Services.
  name: SQL Server Analysis Services (SSAS) API
  slug: ''
- description: REST API for managing Azure SQL Database resources.
  name: Azure SQL Database REST API
  slug: ''
- description: REST API for creating, configuring, and managing Azure SQL Managed Instances.
  name: Azure SQL Managed Instance REST API
  slug: ''
- description: Native T-SQL stored procedure sp_invoke_external_rest_endpoint for calling external HTTPS REST endpoints directly from SQL Server 2025 and Azure SQL.
  name: SQL Server External REST Endpoint Invocation
  slug: ''
- description: Open-source tool that generates REST and GraphQL endpoints for SQL Server and Azure SQL databases from configuration, without writing custom API code.
  name: Data API Builder for SQL Server
  slug: ''
- description: The official .NET data provider for Microsoft SQL Server and Azure SQL databases, providing ADO.NET access to SQL Server.
  name: ADO.NET Provider for SQL Server (Microsoft.Data.SqlClient)
  slug: ''
- description: Stand-alone OLE DB data access API for connecting applications to SQL Server.
  name: OLE DB Driver for SQL Server
  slug: ''
- description: Programmable object model for building, managing, and executing ETL data integration packages in SQL Server.
  name: SQL Server Integration Services (SSIS) API
  slug: ''
- description: Node.js driver (tedious/mssql) for connecting JavaScript and TypeScript applications to SQL Server and Azure SQL Database.
  name: Node.js Driver for SQL Server
  slug: ''
- description: Python drivers for connecting to SQL Server including the first-party mssql-python driver, pyodbc, and pymssql.
  name: Python Drivers for SQL Server
  slug: ''
- description: Microsoft Go driver (go-mssqldb) for connecting Go applications to SQL Server and Azure SQL Database using the TDS protocol.
  name: Go Driver for SQL Server
  slug: ''
- description: Microsoft Drivers for PHP for SQL Server providing SQLSRV and PDO_SQLSRV extensions for connecting PHP applications to SQL Server.
  name: PHP Drivers for SQL Server
  slug: ''
- description: Ruby driver (TinyTDS) for connecting Ruby applications to SQL Server using FreeTDS DB-Library bindings.
  name: Ruby Driver for SQL Server
  slug: ''
- description: Entity Framework Core database provider enabling .NET object-relational mapping with SQL Server and Azure SQL databases.
  name: Entity Framework Core SQL Server Provider
  slug: ''
- description: PowerShell cmdlets for managing SQL Server instances, databases, and resources from the command line.
  name: SQL Server PowerShell Module
  slug: ''
common:
- title: ''
  type: Getting Started
  url: https://docs.microsoft.com/en-us/sql/sql-server/
- title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/sql-server/sql-server-2022-pricing
- title: ''
  type: Support
  url: https://support.microsoft.com/sql
- title: ''
  type: Download
  url: https://www.microsoft.com/en-us/sql-server/sql-server-downloads
- title: ''
  type: Blog
  url: https://cloudblogs.microsoft.com/sqlserver/
- title: ''
  type: Community
  url: https://techcommunity.microsoft.com/t5/sql-server/ct-p/SQLServer
- title: ''
  type: Portal
  url: https://portal.azure.com
- title: ''
  type: Status
  url: https://azure.microsoft.com/en-us/status/
- title: ''
  type: Drivers
  url: https://learn.microsoft.com/en-us/sql/connect/sql-connection-libraries
- title: ''
  type: Learning
  url: https://learn.microsoft.com/en-us/sql/sql-server/educational-sql-resources
- title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/modules/introduction-to-sql-server-2022/
- title: ''
  type: Certification
  url: https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/
- title: ''
  type: GitHubRepository
  url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/sql
- title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2022
- title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
created: '2024'
description: A collection of APIs and interfaces for interacting with Microsoft SQL Server.
features:
- description: Full-featured relational database engine with comprehensive T-SQL support for queries, stored procedures, and functions.
  name: T-SQL Query Engine
- description: High availability and disaster recovery with automatic failover for mission-critical databases.
  name: Always On Availability Groups
- description: Memory-optimized tables and natively compiled stored procedures for high-throughput transaction processing.
  name: In-Memory OLTP
- description: Query external data sources including Hadoop, Azure Blob Storage, and Oracle using T-SQL.
  name: PolyBase
- description: Enterprise reporting platform for creating, managing, and delivering paginated reports.
  name: SQL Server Reporting Services
- description: ETL platform for building data integration and transformation packages.
  name: SQL Server Integration Services
- description: Generate REST and GraphQL endpoints from database tables and views without custom code.
  name: Data API Builder
- description: Call external HTTPS REST APIs directly from T-SQL using sp_invoke_external_rest_endpoint.
  name: External REST Endpoint Invocation
image: /assets/icons/sql-server.png
integrations:
- description: Cloud-hosted managed SQL database service with automatic backups and scaling.
  name: Azure SQL Database
- description: Connect Power BI to SQL Server for interactive dashboards and reports.
  name: Power BI
- description: Orchestrate data movement and transformation pipelines with SQL Server as source or destination.
  name: Azure Data Factory
- description: Object-relational mapping for .NET applications with the SQL Server provider.
  name: Entity Framework Core
- description: Develop and manage SQL Server databases with integrated tools in Visual Studio.
  name: Visual Studio
- description: Extend SQL Server data into cloud-scale analytics with Azure Synapse.
  name: Azure Synapse Analytics
layout: provider
modified: '2026-04-18'
name: Microsoft SQL Server APIs
skills: []
slug: sql-server
solutions: []
tags:
- Azure SQL
- Cloud Database
- Data Management
- Database
- Microsoft
- Relational Database
- SQL
url: https://www.microsoft.com/sql-server
use_cases:
- description: Store and manage enterprise data with ACID compliance, security, and high availability.
  name: Enterprise Data Management
- description: Build BI solutions with reporting services, analysis services, and data integration.
  name: Business Intelligence
- description: Migrate on-premises SQL Server databases to Azure SQL Database or Managed Instance.
  name: Cloud Database Migration
- description: Use SQL Server as the data tier for web, mobile, and enterprise applications.
  name: Application Backend
- description: Build data warehouses with columnstore indexes, partitioning, and ETL pipelines.
  name: Data Warehousing
---
