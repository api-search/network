---
aid: hashicorp:hashicorp-getsysconfigstatesanitized
name: Return a sanitized version of the Vault server configuration.
tags:
- system
humanURL: 
properties: []
description: >-
  The sanitized output strips configuration values in the storage, HA storage, and seals stanzas, which may contain sensitive values such as API tokens. It also removes any token or secret fields in other stanzas, such as the circonus_api_token from telemetry.

---
