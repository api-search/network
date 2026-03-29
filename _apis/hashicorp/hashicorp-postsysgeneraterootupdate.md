---
aid: hashicorp:hashicorp-postsysgeneraterootupdate
name: Enter a single master key share to progress the root generation attempt.
tags:
- system
humanURL: 
properties: []
description: >-
  If the threshold number of master key shares is reached, Vault will complete the root generation and issue the new token. Otherwise, this API must be called multiple times until that threshold is met. The attempt nonce must be provided with each call.

---
