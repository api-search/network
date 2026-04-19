---
consumed_apis:
- reactor
- extension
description: Unified workflow for managing Adobe Experience Platform Tags. Combines the Reactor API and Extension API for marketing technologists and web developers managing tag properties, rules, data elements, extensions, and library builds.
layout: capability
name: Adobe Launch Tag Management
operations:
- description: List all companies
  method: GET
  name: list-companies
  path: /v1/companies
- description: List properties for a company
  method: GET
  name: list-properties
  path: /v1/properties
- description: Create a new tag property
  method: POST
  name: create-property
  path: /v1/properties
- description: List rules for a property
  method: GET
  name: list-rules
  path: /v1/rules
- description: Create a new rule
  method: POST
  name: create-rule
  path: /v1/rules
- description: List data elements for a property
  method: GET
  name: list-data-elements
  path: /v1/data-elements
- description: List extensions installed on a property
  method: GET
  name: list-extensions
  path: /v1/extensions
- description: List available extension packages
  method: GET
  name: list-extension-packages
  path: /v1/extension-packages
- description: List libraries for a property
  method: GET
  name: list-libraries
  path: /v1/libraries
- description: List environments for a property
  method: GET
  name: list-environments
  path: /v1/environments
personas: []
provider_name: Adobe Launch
provider_slug: adobe-launch
search_terms:
- list environments
- search
- adobe launch
- list rules configured for a property
- list extensions installed on a property
- list all companies
- search across all tag management resources
- create a new tag property
- data element management
- list libraries
- list all companies you have access to
- list tag properties for a company
- tag management
- list rules
- create build
- install extension
- get property
- tag property management
- create library
- get details of a specific property
- list extension packages
- company management
- data collection
- list data elements for a property
- list rules for a property
- rule management
- create a new tag rule
- create data element
- create rule
- create a new data element
- event forwarding
- list extensions
- marketing technology
- list properties
- edge network
- list properties for a company
- list available extension packages
- create a new library
- extension management
- extensions
- create a new rule
- library and build management
- list environments for a property
- install an extension on a property
- environment management
- list data elements
- create property
- extension package marketplace
- browse available extension packages in the marketplace
- list companies
- list libraries for a property
- build a library for deployment
slug: tag-management
tags:
- Adobe Launch
- Tag Management
- Marketing Technology
- Extensions
tools:
- description: List all companies you have access to
  hints:
    openWorld: true
    readOnly: true
  name: list-companies
- description: List tag properties for a company
  hints:
    openWorld: true
    readOnly: true
  name: list-properties
- description: Get details of a specific property
  hints:
    openWorld: true
    readOnly: true
  name: get-property
- description: Create a new tag property
  hints:
    readOnly: false
  name: create-property
- description: List rules configured for a property
  hints:
    openWorld: true
    readOnly: true
  name: list-rules
- description: Create a new tag rule
  hints:
    readOnly: false
  name: create-rule
- description: List data elements for a property
  hints:
    openWorld: true
    readOnly: true
  name: list-data-elements
- description: Create a new data element
  hints:
    readOnly: false
  name: create-data-element
- description: List extensions installed on a property
  hints:
    openWorld: true
    readOnly: true
  name: list-extensions
- description: Browse available extension packages in the marketplace
  hints:
    openWorld: true
    readOnly: true
  name: list-extension-packages
- description: Install an extension on a property
  hints:
    readOnly: false
  name: install-extension
- description: List libraries for a property
  hints:
    openWorld: true
    readOnly: true
  name: list-libraries
- description: Create a new library
  hints:
    readOnly: false
  name: create-library
- description: Build a library for deployment
  hints:
    readOnly: false
  name: create-build
- description: List environments for a property
  hints:
    openWorld: true
    readOnly: true
  name: list-environments
- description: Search across all tag management resources
  hints:
    openWorld: true
    readOnly: true
  name: search
---
