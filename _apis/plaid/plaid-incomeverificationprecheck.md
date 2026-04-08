---
aid: plaid:plaid-incomeverificationprecheck
name: Plaid (Deprecated) Check digital income verification eligibility and optimize conversion
tags:
- Plaid
humanURL: 
properties: []
description: >-
  `/income/verification/precheck` is an optional endpoint that can be called before initializing a Link session for income verification. It evaluates whether a given user is supportable by digital income verification and returns a `precheck_id` that can be provided to `/link/token/create`. If the user is eligible for digital verification, providing the `precheck_id` in this way will generate a Link UI optimized for the end user and their specific employer. If the user cannot be confirmed as eli...

---
