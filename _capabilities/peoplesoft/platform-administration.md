---
consumed_apis:
- cloud-manager
- update-manager
- process-scheduler
- integration-broker
- rest-api
- asf
- component-interface
description: Unified workflow for IT administrators combining environment provisioning, update management, process scheduling, integration broker, REST API management, application services framework, and component interface operations across PeopleSoft platform APIs.
layout: capability
name: PeopleSoft Platform Administration
operations:
- description: Retrieve provisioned environments.
  method: GET
  name: list-environments
  path: /v1/environments
- description: Provision a new environment.
  method: POST
  name: provision-environment
  path: /v1/environments
- description: Retrieve available provisioning templates.
  method: GET
  name: list-templates
  path: /v1/templates
- description: Retrieve available updates.
  method: GET
  name: list-updates
  path: /v1/updates
- description: Initiate application of a specific update.
  method: POST
  name: apply-update
  path: /v1/updates/{updateId}/apply
- description: Retrieve process requests and their run status.
  method: GET
  name: list-processes
  path: /v1/processes
- description: Submit a new process request.
  method: POST
  name: submit-process
  path: /v1/processes
- description: Retrieve the status of a specific process instance.
  method: GET
  name: get-process-status
  path: /v1/processes/{processInstance}
- description: Invoke a service operation using GET.
  method: GET
  name: get-service-operation
  path: /v1/service-operations/{serviceOperation}
- description: Invoke a service operation using POST.
  method: POST
  name: post-service-operation
  path: /v1/service-operations/{serviceOperation}
- description: Retrieve PeopleSoft resource data.
  method: GET
  name: get-resource
  path: /v1/resources/{resource}
- description: Create a new PeopleSoft resource.
  method: POST
  name: create-resource
  path: /v1/resources/{resource}
- description: Retrieve data from an ASF-defined service.
  method: GET
  name: get-service-resource
  path: /v1/services/{serviceName}
- description: Create a resource via an ASF-defined service.
  method: POST
  name: create-service-resource
  path: /v1/services/{serviceName}
- description: Retrieve data from a component interface.
  method: GET
  name: get-component-data
  path: /v1/component-interfaces/{componentInterface}
- description: Create a new record via a component interface.
  method: POST
  name: create-component-data
  path: /v1/component-interfaces/{componentInterface}
- description: Update an existing record via a component interface.
  method: PUT
  name: update-component-data
  path: /v1/component-interfaces/{componentInterface}
personas: []
provider_name: PeopleSoft
provider_slug: peoplesoft
search_terms:
- apply updates
- get component data
- erp
- retrieve available updates.
- get service operation
- peoplesoft rest resources
- retrieve available provisioning templates.
- provision a new environment.
- create a resource via an asf-defined service.
- invoke a synchronous integration broker service operation using get.
- supply chain management
- peopletools
- create a new peoplesoft resource via rest.
- peopletools platform services.
- list environments
- get resource
- asf service resources
- crm
- list templates
- peoplesoft
- list updates
- retrieve data from a peoplesoft component interface.
- retrieve provisioned peoplesoft environments.
- update an existing record via a peoplesoft component interface.
- invoke an integration broker service operation using post.
- financial management
- devops
- process instance details
- component interface resources
- cloud manager
- initiate application of a specific update.
- update an existing record via a component interface.
- update component data
- post service operation
- initiate application of a specific update or change package.
- integration
- integration broker service operations
- campus solutions.
- create a new peoplesoft resource.
- platform administration
- submit a new process request for scheduling.
- create resource
- create a new record via a peoplesoft component interface.
- peoplesoft environments
- provision a new peoplesoft environment on oci.
- process requests
- get service resource
- enterprise software
- retrieve process requests and their run status.
- submit process
- retrieve available updates and change packages.
- campus solutions
- available updates and change packages
- submit a new process request.
- human capital management.
- list processes
- retrieve peoplesoft resource data via rest.
- create component data
- create service resource
- create a new record via a component interface.
- hcm
- provisioning templates
- financial and supply chain management.
- provision environment
- retrieve data from an asf-defined service.
- retrieve the status of a specific process instance.
- retrieve data from a component interface.
- apply update
- retrieve provisioned environments.
- retrieve peoplesoft resource data.
- invoke a service operation using post.
- invoke a service operation using get.
- get process status
slug: platform-administration
tags:
- PeopleSoft
- Platform Administration
- Cloud Manager
- Integration
- DevOps
- PeopleTools
tools:
- description: Retrieve provisioned PeopleSoft environments.
  hints:
    openWorld: true
    readOnly: true
  name: list-environments
- description: Provision a new PeopleSoft environment on OCI.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: provision-environment
- description: Retrieve available provisioning templates.
  hints:
    openWorld: true
    readOnly: true
  name: list-templates
- description: Retrieve available updates and change packages.
  hints:
    openWorld: true
    readOnly: true
  name: list-updates
- description: Initiate application of a specific update or change package.
  hints:
    destructive: true
    idempotent: false
    readOnly: false
  name: apply-update
- description: Retrieve process requests and their run status.
  hints:
    openWorld: true
    readOnly: true
  name: list-processes
- description: Submit a new process request for scheduling.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: submit-process
- description: Retrieve the status of a specific process instance.
  hints:
    openWorld: true
    readOnly: true
  name: get-process-status
- description: Invoke a synchronous Integration Broker service operation using GET.
  hints:
    openWorld: true
    readOnly: true
  name: get-service-operation
- description: Invoke an Integration Broker service operation using POST.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: post-service-operation
- description: Retrieve PeopleSoft resource data via REST.
  hints:
    openWorld: true
    readOnly: true
  name: get-resource
- description: Create a new PeopleSoft resource via REST.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-resource
- description: Retrieve data from an ASF-defined service.
  hints:
    openWorld: true
    readOnly: true
  name: get-service-resource
- description: Create a resource via an ASF-defined service.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-service-resource
- description: Retrieve data from a PeopleSoft component interface.
  hints:
    openWorld: true
    readOnly: true
  name: get-component-data
- description: Create a new record via a PeopleSoft component interface.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-component-data
- description: Update an existing record via a PeopleSoft component interface.
  hints:
    destructive: false
    idempotent: true
    readOnly: false
  name: update-component-data
---
