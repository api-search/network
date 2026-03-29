---
aid: knative:knative-replaceservice
name: Replace a Knative Service
tags:
- Services
humanURL: 
properties: []
description: >-
  Replaces a Knative Service. Any change to the spec.template causes Knative to create a new Revision. Traffic routing continues to the previous Revision until the new one becomes ready, unless traffic configuration specifies otherwise.

---
