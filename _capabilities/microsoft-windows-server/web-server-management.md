---
consumed_apis:
- iis-administration
description: Unified workflow for IT administrators to manage IIS web sites, applications, and application pools for enterprise web hosting on Windows Server.
layout: capability
name: Windows Server Web Management
operations:
- description: List all web sites
  method: GET
  name: list-websites
  path: /v1/websites
- description: Create a web site
  method: POST
  name: create-website
  path: /v1/websites
- description: Get web site details
  method: GET
  name: get-website
  path: /v1/websites/{id}
- description: Update a web site
  method: PATCH
  name: update-website
  path: /v1/websites/{id}
- description: Delete a web site
  method: DELETE
  name: delete-website
  path: /v1/websites/{id}
- description: List all applications
  method: GET
  name: list-applications
  path: /v1/applications
- description: Create an application
  method: POST
  name: create-application
  path: /v1/applications
- description: List all application pools
  method: GET
  name: list-application-pools
  path: /v1/application-pools
- description: Create an application pool
  method: POST
  name: create-application-pool
  path: /v1/application-pools
personas: []
provider_name: Microsoft Windows Server
provider_slug: microsoft-windows-server
search_terms:
- list all iis web sites on the server
- iis
- get application pool details
- list all web sites
- update website
- delete website
- microsoft
- get web application details
- create a web site
- get website
- list all iis application pools
- update application
- delete an application pool
- delete application pool
- list application pools
- list all applications
- list all web applications
- create a new web application
- server management
- get application pool
- get details for a specific web site
- create a new iis web site
- list websites
- create an application
- delete an iis web site
- windows server
- application pool management
- update an iis web site configuration
- web site management
- list all application pools
- update a web application
- delete application
- web server
- delete a web application
- get application
- single web site operations
- get web site details
- update an application pool configuration
- datacenter
- update application pool
- create application pool
- web application management
- operating system
- create an application pool
- create website
- windows server 2025
- create an iis application pool
- update a web site
- enterprise
- create application
- list applications
- delete a web site
- infrastructure
slug: web-server-management
tags:
- Microsoft
- Windows Server
- IIS
- Web Server
tools:
- description: List all IIS web sites on the server
  hints:
    openWorld: true
    readOnly: true
  name: list-websites
- description: Create a new IIS web site
  hints:
    readOnly: false
  name: create-website
- description: Get details for a specific web site
  hints:
    readOnly: true
  name: get-website
- description: Update an IIS web site configuration
  hints:
    idempotent: true
    readOnly: false
  name: update-website
- description: Delete an IIS web site
  hints:
    destructive: true
  name: delete-website
- description: List all web applications
  hints:
    readOnly: true
  name: list-applications
- description: Create a new web application
  hints:
    readOnly: false
  name: create-application
- description: Get web application details
  hints:
    readOnly: true
  name: get-application
- description: Update a web application
  hints:
    idempotent: true
    readOnly: false
  name: update-application
- description: Delete a web application
  hints:
    destructive: true
  name: delete-application
- description: List all IIS application pools
  hints:
    readOnly: true
  name: list-application-pools
- description: Create an IIS application pool
  hints:
    readOnly: false
  name: create-application-pool
- description: Get application pool details
  hints:
    readOnly: true
  name: get-application-pool
- description: Update an application pool configuration
  hints:
    idempotent: true
    readOnly: false
  name: update-application-pool
- description: Delete an application pool
  hints:
    destructive: true
  name: delete-application-pool
---
