---
description: Schema for a Prisma Cloud Cloud Security Posture Management (CSPM) security policy. Policies define the security and compliance checks that Prisma Cloud evaluates against cloud resource configurations, network flow logs, audit events, and behavioral data. Each policy contains a rule with an RQL (Resource Query Language) query or detection criteria, along with severity classification, cloud scope, remediation guidance, and compliance framework mappings. Policies can be system-default (maintained by Palo Alto Networks) or custom-created by administrators to enforce organization-specific security requirements.
layout: schema
name: Prisma Cloud Policy
properties_list:
- description: 'Unique UUID identifier for the policy, assigned by Prisma Cloud upon creation. This field is read-only and cannot be set by API clients. Used to reference the policy in alert rules, compliance report '
  name: policyId
  type: string
- description: Human-readable display name of the policy. Must be unique within the Prisma Cloud tenant. Typically follows the pattern 'Cloud Provider - Resource Type - Condition' (e.g., 'AWS S3 bucket is publicly a
  name: name
  type: string
- description: 'Classification of the policy type that determines which evaluation engine and data source is used. ''config'' evaluates cloud resource configurations via RQL config queries. ''network'' analyzes VPC flow '
  name: policyType
  type: string
- description: Detailed description of the policy explaining what misconfiguration or security risk it detects, why the risk matters, and the potential impact of a violation. Displayed in the policy library and with
  name: description
  type: string
- description: Severity level assigned to the policy indicating the potential risk and impact of a detected violation. 'critical' indicates an actively exploitable or high-impact misconfiguration. 'high' indicates a
  name: severity
  type: string
- description: The evaluation rule containing the detection logic for this policy. For RQL-based policies this contains the query string executed against cloud resource data to identify violations.
  name: rule
  type: object
- description: List of administrative labels applied to the policy for organizational grouping, filtering, and bulk management. Labels are user-defined strings supporting operational workflows such as team ownership
  name: labels
  type: array
- description: Whether the policy is currently active and generating alerts. Disabled policies are not evaluated during scheduled or real-time scans. Useful for temporarily suppressing a policy during maintenance wi
  name: enabled
  type: boolean
- description: Whether the policy is a system-default policy provided and maintained by Palo Alto Networks. System-default policies are updated by the Prisma Cloud research team and cannot be deleted, though they ca
  name: systemDefault
  type: boolean
- description: Cloud service provider scope for the policy. Provider-specific policies contain RQL queries and remediation steps tailored to that provider's APIs and resource model. 'all' indicates a cross-cloud pol
  name: cloudType
  type: string
- description: Step-by-step remediation guidance for resolving policy violations. Should include specific instructions for the relevant cloud provider console, CLI, or API. Supports markdown formatting for structure
  name: recommendation
  type: string
- description: Whether automated remediation is available for this policy via the configured CLI script template. When true, analysts can trigger one-click remediation from the Prisma Cloud alert interface.
  name: remediable
  type: boolean
- description: Automated and manual remediation configuration for resolving violations detected by this policy. Includes CLI script templates for automated remediation and descriptive steps for manual resolution.
  name: remediation
  type: object
- description: List of compliance standard mappings associating this policy with specific regulatory or organizational compliance requirements. Each entry links the policy to a named compliance framework, requiremen
  name: complianceMetadata
  type: array
- description: Timestamp when the policy was first created, expressed as Unix epoch time in milliseconds.
  name: createdOn
  type: integer
- description: Email address or username of the administrator who created the policy. Set to 'Prisma Cloud' for system-default policies.
  name: createdBy
  type: string
- description: Timestamp of the most recent modification to the policy configuration, expressed as Unix epoch time in milliseconds.
  name: lastModifiedOn
  type: integer
- description: Email address or username of the administrator who last modified the policy.
  name: lastModifiedBy
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-policy-schema.json
slug: prisma-cloud-policy
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Prisma Cloud Policy
---
