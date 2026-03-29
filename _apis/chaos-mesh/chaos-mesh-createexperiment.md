---
aid: chaos-mesh:chaos-mesh-createexperiment
name: Create an experiment
tags:
- Experiments
humanURL: 
properties: []
description: >-
  Creates a new chaos experiment by submitting a Chaos Mesh custom resource to Kubernetes. The request body must include the kind field specifying the chaos type (e.g., PodChaos, NetworkChaos) and a spec field with the chaos-type-specific configuration. The experiment begins immediately upon creation unless a duration or schedule is specified.

---
