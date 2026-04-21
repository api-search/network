---
consumed_apis:
- fis
description: Workflow capability for executing chaos engineering experiments using AWS FIS. Enables resilience engineers and SREs to design, execute, and monitor fault injection experiments across AWS infrastructure.
layout: capability
name: AWS FIS Chaos Engineering
operations:
- description: List templates
  method: GET
  name: list-experiment-templates
  path: /v1/experiment-templates
- description: Create template
  method: POST
  name: create-experiment-template
  path: /v1/experiment-templates
- description: Get template
  method: GET
  name: get-experiment-template
  path: /v1/experiment-templates/{id}
- description: Update template
  method: PATCH
  name: update-experiment-template
  path: /v1/experiment-templates/{id}
- description: Delete template
  method: DELETE
  name: delete-experiment-template
  path: /v1/experiment-templates/{id}
- description: List experiments
  method: GET
  name: list-experiments
  path: /v1/experiments
- description: Start experiment
  method: POST
  name: start-experiment
  path: /v1/experiments
- description: Get experiment
  method: GET
  name: get-experiment
  path: /v1/experiments/{id}
- description: Stop experiment
  method: DELETE
  name: stop-experiment
  path: /v1/experiments/{id}
- description: Get safety lever
  method: GET
  name: get-safety-lever
  path: /v1/safety-levers/{id}
- description: Update safety lever state
  method: PATCH
  name: update-safety-lever-state
  path: /v1/safety-levers/{id}
personas: []
provider_name: Amazon Fault Injection Simulator
provider_slug: amazon-fault-injection-simulator
search_terms:
- discover all available fault injection action types
- engage or disengage a safety lever to allow or block experiments
- create experiment template
- engineers integrating fis into ci/cd for automated resilience testing
- abort a running fault injection experiment
- design a new fault injection scenario with targets, actions, and stop conditions
- check the status of a safety lever for experiment control
- update template
- get action
- deliberate fault injection to test system resilience
- list templates
- update safety lever state
- monitor the status and progress of a fault injection experiment
- devops
- get safety lever
- monitoring system behavior during controlled experiments
- list actions
- manage specific experiment
- list all experiments and their current status
- create template
- list all fault injection experiment templates
- manage experiments
- execute a fault injection experiment from a template
- engineers designing and running chaos experiments to improve system reliability
- list experiment templates
- get the configuration of an experiment template
- sre
- chaos engineering
- aws fis
- update experiment template
- start experiment
- get details and parameters for a specific fis action
- SRE
- DevOps Engineer
- get template
- list experiments
- Resilience Engineer
- delete experiment template
- get experiment
- validating application behavior under failure conditions
- full chaos engineering lifecycle
- fault injection
- resilience testing
- aws
- get experiment template
- sres using fis to validate service resilience targets
- delete template
- resilience
- modify targets, actions, or stop conditions of an experiment template
- manage specific template
- safety lever control
- remove an experiment template
- manage experiment templates
- stop experiment
slug: amazon-fis-chaos-engineering
tags:
- AWS FIS
- Chaos Engineering
- Resilience
- SRE
- DevOps
tools:
- description: List all fault injection experiment templates
  hints:
    openWorld: true
    readOnly: true
  name: list-experiment-templates
- description: Design a new fault injection scenario with targets, actions, and stop conditions
  hints:
    readOnly: false
  name: create-experiment-template
- description: Get the configuration of an experiment template
  hints:
    readOnly: true
  name: get-experiment-template
- description: Modify targets, actions, or stop conditions of an experiment template
  hints:
    readOnly: false
  name: update-experiment-template
- description: Remove an experiment template
  hints:
    destructive: true
    readOnly: false
  name: delete-experiment-template
- description: Execute a fault injection experiment from a template
  hints:
    destructive: true
    readOnly: false
  name: start-experiment
- description: Monitor the status and progress of a fault injection experiment
  hints:
    readOnly: true
  name: get-experiment
- description: List all experiments and their current status
  hints:
    readOnly: true
  name: list-experiments
- description: Abort a running fault injection experiment
  hints:
    destructive: true
    readOnly: false
  name: stop-experiment
- description: Discover all available fault injection action types
  hints:
    readOnly: true
  name: list-actions
- description: Get details and parameters for a specific FIS action
  hints:
    readOnly: true
  name: get-action
- description: Check the status of a safety lever for experiment control
  hints:
    readOnly: true
  name: get-safety-lever
- description: Engage or disengage a safety lever to allow or block experiments
  hints:
    readOnly: false
  name: update-safety-lever-state
---
