---
consumed_apis:
- nitro
description: Unified capability for managing Citrix NetScaler application delivery controllers, including load balancing, content switching, configuration management, and monitoring. Used by network administrators and platform engineers.
layout: capability
name: Citrix NetScaler ADC Management
operations:
- description: List all load balancing virtual servers
  method: GET
  name: list-lb-vservers
  path: /v1/lb-vservers
- description: Create a load balancing virtual server
  method: POST
  name: create-lb-vserver
  path: /v1/lb-vservers
- description: Get a specific load balancing virtual server
  method: GET
  name: get-lb-vserver
  path: /v1/lb-vservers/{name}
- description: Update a load balancing virtual server
  method: PUT
  name: update-lb-vserver
  path: /v1/lb-vservers/{name}
- description: Delete a load balancing virtual server
  method: DELETE
  name: delete-lb-vserver
  path: /v1/lb-vservers/{name}
- description: Get service bindings for an LB virtual server
  method: GET
  name: get-lb-vserver-service-bindings
  path: /v1/lb-vservers/{name}/bindings
- description: Bind a service to an LB virtual server
  method: POST
  name: bind-service-to-lb-vserver
  path: /v1/lb-vservers/{name}/bindings
- description: List all content switching virtual servers
  method: GET
  name: list-cs-vservers
  path: /v1/cs-vservers
- description: Create a content switching virtual server
  method: POST
  name: create-cs-vserver
  path: /v1/cs-vservers
- description: Get a content switching virtual server
  method: GET
  name: get-cs-vserver
  path: /v1/cs-vservers/{name}
- description: Update a content switching virtual server
  method: PUT
  name: update-cs-vserver
  path: /v1/cs-vservers/{name}
- description: Delete a content switching virtual server
  method: DELETE
  name: delete-cs-vserver
  path: /v1/cs-vservers/{name}
- description: Get NetScaler configuration
  method: GET
  name: get-ns-config
  path: /v1/config
- description: Save running configuration to disk
  method: POST
  name: save-ns-config
  path: /v1/config
- description: List statistics for all LB virtual servers
  method: GET
  name: list-lb-vserver-stats
  path: /v1/stats/lb-vservers
- description: Get statistics for an LB virtual server
  method: GET
  name: get-lb-vserver-stats
  path: /v1/stats/lb-vservers/{name}
- description: List statistics for all CS virtual servers
  method: GET
  name: list-cs-vserver-stats
  path: /v1/stats/cs-vservers
personas: []
provider_name: Citrix NetScaler
provider_slug: citrix-netscaler
search_terms:
- list statistics for all cs virtual servers
- list performance statistics for all lb virtual servers
- list cs vserver stats
- delete lb vserver
- list all load balancing virtual servers
- bind service to lb vserver
- content switching virtual servers
- save the running netscaler configuration to persistent storage
- get details of a specific content switching virtual server
- get statistics for a specific content switching virtual server
- list lb vservers
- get details of a specific load balancing virtual server
- get ns config
- update cs vserver
- bind a service to an lb virtual server
- save running configuration to disk
- get lb vserver stats
- unbind service from lb vserver
- update a load balancing virtual server
- create cs vserver
- content switching virtual server statistics
- get cs vserver stats
- get lb vserver service bindings
- single content switching virtual server
- statistics for a specific lb virtual server
- list lb vserver stats
- update a load balancing virtual server configuration
- network administration
- web application firewall
- application security
- get netscaler appliance configuration
- get all service bindings for a load balancing virtual server
- citrix
- get netscaler configuration
- list statistics for all lb virtual servers
- unbind a service from a load balancing virtual server
- get a content switching virtual server
- get cs vserver
- get lb vserver
- delete a content switching virtual server
- create a new load balancing virtual server
- load balancing virtual servers
- service bindings for a load balancing virtual server
- get service bindings for an lb virtual server
- list all content switching virtual servers
- update lb vserver
- application delivery controller
- api gateway
- delete cs vserver
- load balancing
- save ns config
- update a content switching virtual server
- appliance configuration
- adc management
- netscaler
- single load balancing virtual server
- get statistics for an lb virtual server
- list all load balancing virtual servers on the netscaler
- bind a backend service to a load balancing virtual server
- traffic management
- create a load balancing virtual server
- list cs vservers
- delete a load balancing virtual server
- create lb vserver
- ssl offloading
- create a content switching virtual server
- load balancing virtual server statistics
- list statistics for all content switching virtual servers
- get performance statistics for a specific lb virtual server
- get a specific load balancing virtual server
slug: adc-management
tags:
- Citrix
- NetScaler
- Load Balancing
- ADC Management
- Network Administration
tools:
- description: List all load balancing virtual servers on the NetScaler
  hints:
    openWorld: true
    readOnly: true
  name: list-lb-vservers
- description: Create a new load balancing virtual server
  hints:
    readOnly: false
  name: create-lb-vserver
- description: Get details of a specific load balancing virtual server
  hints:
    openWorld: true
    readOnly: true
  name: get-lb-vserver
- description: Update a load balancing virtual server configuration
  hints:
    idempotent: true
    readOnly: false
  name: update-lb-vserver
- description: Delete a load balancing virtual server
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-lb-vserver
- description: Bind a backend service to a load balancing virtual server
  hints:
    readOnly: false
  name: bind-service-to-lb-vserver
- description: Get all service bindings for a load balancing virtual server
  hints:
    openWorld: true
    readOnly: true
  name: get-lb-vserver-service-bindings
- description: Unbind a service from a load balancing virtual server
  hints:
    destructive: true
    readOnly: false
  name: unbind-service-from-lb-vserver
- description: List all content switching virtual servers
  hints:
    openWorld: true
    readOnly: true
  name: list-cs-vservers
- description: Create a content switching virtual server
  hints:
    readOnly: false
  name: create-cs-vserver
- description: Get details of a specific content switching virtual server
  hints:
    openWorld: true
    readOnly: true
  name: get-cs-vserver
- description: Update a content switching virtual server
  hints:
    idempotent: true
    readOnly: false
  name: update-cs-vserver
- description: Delete a content switching virtual server
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-cs-vserver
- description: Get NetScaler appliance configuration
  hints:
    openWorld: true
    readOnly: true
  name: get-ns-config
- description: Save the running NetScaler configuration to persistent storage
  hints:
    readOnly: false
  name: save-ns-config
- description: List performance statistics for all LB virtual servers
  hints:
    openWorld: true
    readOnly: true
  name: list-lb-vserver-stats
- description: Get performance statistics for a specific LB virtual server
  hints:
    openWorld: true
    readOnly: true
  name: get-lb-vserver-stats
- description: List statistics for all content switching virtual servers
  hints:
    openWorld: true
    readOnly: true
  name: list-cs-vserver-stats
- description: Get statistics for a specific content switching virtual server
  hints:
    openWorld: true
    readOnly: true
  name: get-cs-vserver-stats
---
