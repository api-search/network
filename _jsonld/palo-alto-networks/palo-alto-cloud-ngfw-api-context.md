---
class_count: 16
classes:
- Firewall
- FirewallRequest
- FirewallSummary
- FqdnListRequest
- FqdnListSummary
- PrefixListRequest
- PrefixListSummary
- ResponseStatus
- RuleDestination
- RuleSource
- RuleStack
- RuleStackRequest
- RuleStackSummary
- SecurityRule
- SecurityRuleRequest
- SecurityRuleSummary
context_file: json-ld/palo-alto-cloud-ngfw-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-cloud-ngfw-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Cloud Ngfw Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Cloud Ngfw Api Context
namespaces:
- prefix: pan
  uri: https://pan.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: set
  name: FqdnList
  type: string
- container: set
  name: PrefixList
  type: string
- container: ''
  name: Action
  type: string
- container: ''
  name: AntiSpywareProfile
  type: string
- container: ''
  name: AntiVirusProfile
  type: string
- container: set
  name: Applications
  type: string
- container: ''
  name: AssociatedRuleStack
  type: string
- container: set
  name: Attachments
  type: reference
- container: ''
  name: AuditComment
  type: string
- container: ''
  name: AvailabilityZone
  type: string
- container: ''
  name: Category
  type: reference
- container: set
  name: Cidrs
  type: string
- container: set
  name: Countries
  type: string
- container: ''
  name: DecryptionRuleType
  type: string
- container: ''
  name: Description
  type: string
- container: ''
  name: Destination
  type: reference
- container: ''
  name: Enabled
  type: boolean
- container: ''
  name: EndpointId
  type: string
- container: ''
  name: ErrorCode
  type: integer
- container: set
  name: Feeds
  type: string
- container: ''
  name: FileBlockingProfile
  type: string
- container: ''
  name: FirewallEntry
  type: reference
- container: ''
  name: FirewallName
  type: string
- container: ''
  name: FirewallStatus
  type: reference
- container: ''
  name: FqdnListEntry
  type: reference
- container: ''
  name: FqdnListName
  type: string
- container: set
  name: FqdnLists
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: LookupXForwardedFor
  type: string
- container: ''
  name: MinAppIdVersion
  type: string
- container: ''
  name: NegateDestination
  type: boolean
- container: ''
  name: NegateSource
  type: boolean
- container: ''
  name: PrefixListEntry
  type: reference
- container: ''
  name: PrefixListName
  type: string
- container: set
  name: PrefixLists
  type: string
- container: ''
  name: Priority
  type: integer
- container: ''
  name: Profile
  type: reference
- container: ''
  name: Protocol
  type: string
- container: ''
  name: Reason
  type: string
- container: ''
  name: RuleEntry
  type: reference
- container: ''
  name: RuleName
  type: string
- container: ''
  name: RuleStackEntry
  type: reference
- container: ''
  name: RuleStackName
  type: string
- container: ''
  name: Scope
  type: string
- container: ''
  name: Source
  type: reference
- container: ''
  name: Status
  type: string
- container: ''
  name: SubnetId
  type: string
- container: set
  name: SubnetMappings
  type: reference
- container: set
  name: Tags
  type: reference
- container: set
  name: URLCategoryNames
  type: string
- container: ''
  name: URLFilteringProfile
  type: string
- container: ''
  name: UpdateToken
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: VpcId
  type: string
- container: ''
  name: VulnerabilityProfile
  type: string
property_count: 55
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-cloud-ngfw-api-context
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
- JSON-LD
- Linked Data
- Semantic Web
---
