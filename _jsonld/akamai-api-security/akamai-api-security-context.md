---
class_count: 71
classes:
- url-protection-category
- hostname-coverage-match-target-get-200
- header-logging-put
- custom-rules
- reputation-profile
- attack-payload-logging-put
- url-protection-bypass-request-header-condition
- url-protection-policies
- malware-policy
- hostnames
- prefetch-request-put
- version-notes-get-200
- reputation-profiles
- url-protection-policy
- attack-payload-logging-get-200
- prefetch-request-get-200
- validation
- config-get
- version-notes-put
- request-header-condition-2
- overlap-config
- waf-config-version
- rate-policy-evaluation-put
- validations
- siem-settings
- hostname-object
- custom-deny
- match-targets
- evasive-path-match-get-200
- malware-policies
- config-clone-post
- header-logging-get-200
- siem-version
- request-body
- problem-details
- pii-learning
- configs-get
- hostname-coverage-match-target
- custom-rule
- effectiveTimePeriod
- rate-policy
- cookie-settings
- match-target
- host-info-in-config
- bypass-network-lists-get
- logging-option
- evasive-path-match-put
- header-logging-put-200
- evasive-path-match-put-200
- match-targets-sequence
- hostname-coverage-overlapping-get-200
- attack-payload-logging
- waf-config-versions
- rate-policies
- custom-denies
- logging-header-setting
- url-protection-policy-hostpath
- siem-versions
- pragma-header
- bypass-network-lists-put
- security-controls
- config-rename
- malware-policies-content-types
- tls-fingerprint-condition
- version-notes-put-200
- url-protection-client-list-category
- prefetch-request-put-200
- client-reputation-condition
- config-post
- attack-payload-logging-put-200
- url-protection-bypass-client-list-condition
context_file: json-ld/akamai-api-security-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/akamai-api-security/refs/heads/main/json-ld/akamai-api-security-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Akamai Api Security from Akamai API Security.
layout: jsonld
name: Akamai Api Security Context
namespaces:
- prefix: akamai
  uri: https://developer.akamai.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: type
  type: string
- container: ''
  name: matchTargets
  type: reference
- container: set
  name: apiTargets
  type: reference
- container: set
  name: websiteTargets
  type: reference
- container: ''
  name: allowSampling
  type: boolean
- container: ''
  name: cookies
  type: reference
- container: set
  name: values
  type: string
- container: ''
  name: customHeaders
  type: reference
- container: ''
  name: standardHeaders
  type: reference
- container: set
  name: customRules
  type: reference
- container: ''
  name: condition
  type: reference
- container: set
  name: atomicConditions
  type: reference
- container: ''
  name: positiveMatch
  type: boolean
- container: ''
  name: context
  type: string
- container: ''
  name: contextReadable
  type: string
- container: ''
  name: description
  type: ''
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: id
  type: integer
- container: ''
  name: name
  type: ''
- container: ''
  name: sharedIpHandling
  type: string
- container: ''
  name: threshold
  type: decimal
- container: ''
  name: requestBody
  type: reference
- container: ''
  name: responseBody
  type: reference
- container: ''
  name: className
  type: string
- container: ''
  name: nameWildcard
  type: boolean
- container: set
  name: value
  type: string
- container: ''
  name: valueCase
  type: boolean
- container: ''
  name: valueWildcard
  type: boolean
- container: set
  name: urlProtectionPolicies
  type: reference
- container: ''
  name: allowListId
  type: string
- container: ''
  name: blockListId
  type: string
- container: set
  name: contentTypes
  type: reference
- container: ''
  name: logFilename
  type: boolean
- container: set
  name: paths
  type: string
- container: ''
  name: allExtensions
  type: boolean
- container: ''
  name: enableAppLayer
  type: boolean
- container: ''
  name: enableRateControls
  type: boolean
- container: set
  name: extensions
  type: string
- container: ''
  name: notes
  type: string
- container: set
  name: reputationProfiles
  type: reference
- container: set
  name: apiDefinitions
  type: reference
- container: ''
  name: bypassCondition
  type: reference
- container: set
  name: categories
  type: string
- container: ''
  name: configId
  type: integer
- container: ''
  name: configVersion
  type: integer
- container: ''
  name: createDate
  type: dateTime
- container: ''
  name: createdBy
  type: string
- container: set
  name: hostnamePaths
  type: reference
- container: ''
  name: intelligentLoadShedding
  type: boolean
- container: ''
  name: policyId
  type: integer
- container: ''
  name: protectionType
  type: string
- container: ''
  name: rateThreshold
  type: integer
- container: ''
  name: sheddingThresholdHitsPerSec
  type: integer
- container: ''
  name: updateDate
  type: dateTime
- container: ''
  name: updatedBy
  type: string
- container: ''
  name: used
  type: boolean
- container: ''
  name: detail
  type: string
- container: ''
  name: fieldName
  type: string
- container: ''
  name: jsonReference
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: latestVersion
  type: integer
- container: set
  name: productionHostnames
  type: string
- container: ''
  name: productionVersion
  type: integer
- container: ''
  name: stagingVersion
  type: integer
- container: ''
  name: configName
  type: string
- container: ''
  name: contractId
  type: string
- container: ''
  name: contractName
  type: string
- container: ''
  name: basedOn
  type: integer
- container: ''
  name: production
  type: reference
- container: ''
  name: action
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: time
  type: string
- container: ''
  name: staging
  type: reference
- container: ''
  name: version
  type: ''
- container: ''
  name: versionNotes
  type: string
- container: set
  name: errors
  type: reference
- container: set
  name: notices
  type: reference
- container: set
  name: warnings
  type: reference
- container: ''
  name: enableForAllPolicies
  type: boolean
- container: ''
  name: enableSiem
  type: boolean
- container: ''
  name: enabledBotmanSiemEvents
  type: boolean
- container: set
  name: exceptions
  type: reference
- container: set
  name: firewallPolicyIds
  type: string
- container: ''
  name: siemDefinitionId
  type: integer
- container: ''
  name: activeInProduction
  type: boolean
- container: ''
  name: activeInStaging
  type: boolean
- container: ''
  name: arlInclusion
  type: boolean
- container: ''
  name: configIdInProduction
  type: integer
- container: ''
  name: configNameInProduction
  type: string
- container: ''
  name: hostname
  type: string
- container: set
  name: parameters
  type: reference
- container: ''
  name: enablePathMatch
  type: boolean
- container: set
  name: malwarePolicies
  type: reference
- container: ''
  name: createFromVersion
  type: integer
- container: ''
  name: ruleUpdate
  type: boolean
- container: ''
  name: requestBodyInspectionLimitInKB
  type: string
- container: ''
  name: fieldErrors
  type: reference
- container: ''
  name: instance
  type: string
- container: ''
  name: enablePiiLearning
  type: boolean
- container: set
  name: configurations
  type: reference
- container: set
  name: apis
  type: reference
- container: set
  name: bypassNetworkLists
  type: reference
- container: ''
  name: defaultFile
  type: string
- container: ''
  name: effectiveSecurityControls
  type: reference
- container: ''
  name: applyApiConstraints
  type: boolean
- container: ''
  name: applyApplicationLayerControls
  type: boolean
- container: ''
  name: applyBotmanControls
  type: boolean
- container: ''
  name: applyNetworkLayerControls
  type: boolean
- container: ''
  name: applyRateControls
  type: boolean
- container: ''
  name: applyReputationControls
  type: boolean
- container: ''
  name: applySlowPostControls
  type: boolean
- container: set
  name: fileExtensions
  type: string
- container: set
  name: filePaths
  type: string
- container: ''
  name: isNegativeFileExtensionMatch
  type: boolean
- container: ''
  name: isNegativePathMatch
  type: boolean
- container: ''
  name: securityPolicy
  type: reference
- container: ''
  name: sequence
  type: integer
- container: ''
  name: targetId
  type: integer
- container: set
  name: conditions
  type: reference
- container: ''
  name: endDate
  type: string
- container: ''
  name: startDate
  type: dateTime
- container: ''
  name: inspectRequest
  type: boolean
- container: ''
  name: inspectResponse
  type: boolean
- container: set
  name: loggingOptions
  type: reference
- container: ''
  name: metadata
  type: string
- container: ''
  name: operation
  type: string
- container: ''
  name: ruleActivated
  type: boolean
- container: ''
  name: samplingRate
  type: integer
- container: ''
  name: stagingOnly
  type: boolean
- container: ''
  name: structured
  type: boolean
- container: set
  name: tag
  type: string
- container: set
  name: additionalMatchOptions
  type: reference
- container: set
  name: apiSelectors
  type: reference
- container: ''
  name: averageThreshold
  type: integer
- container: set
  name: bodyParameters
  type: reference
- container: ''
  name: burstThreshold
  type: integer
- container: ''
  name: burstWindow
  type: integer
- container: ''
  name: clientIdentifier
  type: string
- container: ''
  name: counterType
  type: string
- container: ''
  name: evaluation
  type: reference
- container: ''
  name: evaluationId
  type: integer
- container: ''
  name: evaluationStatus
  type: string
- container: ''
  name: hosts
  type: reference
- container: ''
  name: matchType
  type: string
- container: ''
  name: path
  type: reference
- container: ''
  name: pathMatchType
  type: string
- container: ''
  name: pathUriPositiveMatch
  type: boolean
- container: set
  name: queryParameters
  type: reference
- container: ''
  name: requestType
  type: string
- container: ''
  name: sameActionOnIpv6
  type: boolean
- container: ''
  name: useXForwardForHeaders
  type: boolean
- container: ''
  name: cookieDomain
  type: string
- container: ''
  name: useAllSecureTraffic
  type: boolean
- container: set
  name: availableSet
  type: reference
- container: set
  name: errorSet
  type: reference
- container: ''
  name: protectARLInclusionHost
  type: boolean
- container: set
  name: selectedSet
  type: reference
- container: set
  name: networkLists
  type: reference
- container: set
  name: targetSequence
  type: reference
- container: set
  name: overLappingList
  type: reference
- container: ''
  name: lastCreatedVersion
  type: integer
- container: ''
  name: page
  type: integer
- container: ''
  name: pageSize
  type: integer
- container: ''
  name: productionActiveVersion
  type: integer
- container: ''
  name: productionExpediteRequestId
  type: integer
- container: ''
  name: stagingActiveVersion
  type: integer
- container: ''
  name: stagingExpediteRequestId
  type: integer
- container: ''
  name: totalSize
  type: integer
- container: set
  name: versionList
  type: reference
- container: set
  name: ratePolicies
  type: reference
- container: set
  name: hostnameList
  type: reference
- container: ''
  name: mode
  type: string
- container: set
  name: siemDefinitions
  type: reference
- container: ''
  name: conditionOperator
  type: string
- container: set
  name: excludeCondition
  type: reference
- container: set
  name: malwareContentTypes
  type: string
- container: set
  name: listIds
  type: string
- container: ''
  name: createFrom
  type: reference
- container: ''
  name: groupId
  type: integer
- container: ''
  name: checkIps
  type: string
property_count: 180
provider_name: Akamai API Security
provider_slug: akamai-api-security
slug: akamai-api-security-context
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
- JSON-LD
- Linked Data
- Semantic Web
---
