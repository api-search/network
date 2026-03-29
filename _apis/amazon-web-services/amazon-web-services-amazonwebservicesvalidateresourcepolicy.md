---
aid: amazon-web-services:amazon-web-services-amazonwebservicesvalidateresourcepolicy
name: Validateresourcepolicy
tags:
- API
humanURL: 
properties: []
description: >-
  Validates that a resource policy does not grant a wide range of principals access to your secret. A resource-based policy is optional for secrets. The API performs three checks when validating the policy:   Sends a call to Zelkova, an automated reasoning engine, to ensure your resource policy does not allow broad access to your secret, for example policies that use a wildcard for the principal.   Checks for correct syntax in a policy.   Verifies the policy does not lock out a caller.   Secret...

---
