---
description: <p>A policy type that defines the voting rules for the network. The rules decide if a proposal is approved. Approval may be based on criteria such as the percentage of <code>YES</code> votes and the duration of the proposal. The policy applies to all proposals and is specified when the network is created.</p> <p>Applies only to Hyperledger Fabric.</p>
layout: schema
name: ApprovalThresholdPolicy
properties_list:
- description: ''
  name: ThresholdPercentage
  type: object
- description: ''
  name: ProposalDurationInHours
  type: object
- description: ''
  name: ThresholdComparator
  type: object
provider_name: Amazon Managed Blockchain
provider_slug: amazon-managed-blockchain
schema_file: json-schema/amazon-managed-blockchain-approval-threshold-policy-schema.json
slug: amazon-managed-blockchain-approval-threshold-policy
tags:
- AWS
- Blockchain
- Distributed Ledger
- Hyperledger Fabric
- Ethereum
title: ApprovalThresholdPolicy
---
