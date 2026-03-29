---
aid: keda:keda-getmetricvalue
name: Get metric value
tags:
- Metrics
humanURL: 
properties: []
description: >-
  Returns a JSON (or other format) payload containing a numeric metric value that KEDA extracts using the configured valueLocation path (GJSON notation). The response can include nested objects; KEDA will navigate to the configured path to read the scalar value. The extracted value can be an unquoted integer (e.g., 42) or a Kubernetes quantity string (e.g., "10Mi"). An optional targetValue or activationValue can be compared against this number to determine scaling behavior.

---
