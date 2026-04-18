---
class_count: 132
classes:
- AccessTokenRequest
- AccessTokenResponse
- AdAccount
- AdAccountCreateRequest
- AdAccountUser
- AdAccountUserCreateRequest
- AdAccountUserUpdateRequest
- AdAccountsResponse
- AdTargetingEntitiesResponse
- AdTargetingEntity
- AdTargetingFacet
- AdTargetingFacetsResponse
- AdditionalQuestions
- Address
- AdvertiserTransparencyRequest
- AdvertiserTransparencyResponse
- ApplicationCredentials
- ApplicationData
- ApplicationQuestions
- ApplicationRequest
- AtsIntegrationUpdateRequest
- AudienceCount
- AudienceInsight
- AudienceInsightsRequest
- AudienceInsightsResponse
- BatchGetOnAdministeredResponse200
- BatchGetOnNonadministeredResponse200
- BatchOrganizationResponse
- BatchProfileAssociationResponse
- Budget
- Campaign
- CampaignGroup
- CampaignUpdateRequest
- CandidateData
- CandidateRequest
- CompanyStreamElement
- CompanyStreamRequest
- ComplianceAuthorization
- ComplianceAuthorizationRequest
- ComplianceAuthorizationResponse
- ComplianceEvent
- ComplianceEventsResponse
- ConfigurationValue
- Contract
- ContractsResponse
- ConversionsByMemberCompanyResponse200
- CoverLetterQuestions
- CreateANewConversionResponse201
- Creative
- CreativeCreateRequest
- CrmDataValidationExportJob
- CrmDataValidationExportJobRequest
- CustomQuestion
- CustomQuestionSet
- DateInfo
- DmpSegment
- DmpSegmentCreateRequest
- DmpSegmentsResponse
- EducationQuestions
- ErrorResponse
- FetchActiveCampaignsResponse200
- FetchExistingConversionRulesResponse200
- FetchFullLeadDataResponse200
- FindAdministeredOrganizationBrandsResponse200
- FindNonadministeredOrganizationResponse200
- GetAListOfResponse200
- GetApplicationResponse
- GetBingGeoLocationsResponse200
- GetFormsForTheResponse200
- GetTheUsersSponsoredResponse200
- ImageAsset
- ImageReference
- InsightSegmentation
- IntegrationConfigurationRequest
- IntegrationPatch
- JobPostingElement
- JobPostingResponse
- LearnerDetails
- LearnerEntity
- LearningActivity
- LearningActivityReport
- LearningActivityReportResponse
- ListUploadRequest
- Locale
- LocalizedString
- LookupByOrganizationPrimaryResponse200
- MemberProfile
- MultipleChoiceQuestionDetails
- NoteData
- NoteRequest
- OnsiteApplyConfiguration
- OrganizationAcl
- OrganizationAclResponse
- OrganizationLocation
- OrganizationResponse
- Paging
- PagingLink
- PersonName
- PhoneNumber
- Post
- PostResponse
- ProvisionApplicationRequest
- ProvisionApplicationResponse
- QuestionChoice
- QuestionDetails
- ReactionResponse
- RequestMetaData
- ResumeQuestions
- RetrieveAnAdministeredOrganizationResponse200
- RetrieveAuthenticatedUsersSponsoredResponse200
- RetrieveOrganizationFollowerCountResponse200
- RunSchedule
- SalesAccessToken
- SalesAccessTokenResponse
- SalesAnalyticsExportJob
- SalesAnalyticsExportJobRequest
- SalesAnalyticsExportJobResponse
- SalesNavigatorProfileAssociation
- SalesNavigatorProfileAssociationKey
- SegmentDestination
- SimpleJobPostingRequest
- StreamMultipleConversionEventsResponse200
- StreamResponse
- StreamResultElement
- TargetingCriteria
- Timestamp
- UpdateCallbackUrlRequest
- UserId
- UserStreamElement
- UserStreamRequest
- ValidateTheUsersOrganizationResponse200
- WorkQuestions
context_file: json-ld/linkedin-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/linkedin/refs/heads/main/json-ld/linkedin-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Linkedin Api from LinkedIn.
layout: jsonld
name: Linkedin Api Context
namespaces:
- prefix: li
  uri: https://learn.microsoft.com/en-us/linkedin/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: accessPolicy
  type: string
- container: ''
  name: access_token
  type: string
- container: ''
  name: account
  type: string
- container: ''
  name: accountUrn
  type: string
- container: ''
  name: action
  type: string
- container: ''
  name: activeCount
  type: integer
- container: set
  name: activities
  type: string
- container: ''
  name: activity
  type: string
- container: ''
  name: actor
  type: string
- container: ''
  name: additionalQuestions
  type: string
- container: ''
  name: address
  type: string
- container: set
  name: addresses
  type: string
- container: ''
  name: advertiserName
  type: string
- container: set
  name: alternativeNames
  type: string
- container: ''
  name: amount
  type: string
- container: ''
  name: applicationUrn
  type: string
- container: ''
  name: assetType
  type: string
- container: set
  name: associatedCampaigns
  type: string
- container: ''
  name: associatedEntity
  type: string
- container: ''
  name: atsCandidateId
  type: string
- container: ''
  name: atsCreatedAt
  type: string
- container: ''
  name: atsJobPostingId
  type: string
- container: ''
  name: atsJobPostingName
  type: string
- container: ''
  name: atsLastModifiedAt
  type: string
- container: ''
  name: attributionType
  type: string
- container: ''
  name: audienceSize
  type: integer
- container: ''
  name: author
  type: string
- container: ''
  name: autoCreated
  type: boolean
- container: set
  name: availableEntityFinders
  type: string
- container: ''
  name: campaign
  type: string
- container: ''
  name: campaignGroup
  type: string
- container: set
  name: campaigns
  type: string
- container: ''
  name: candidateEmail
  type: string
- container: ''
  name: capturedAt
  type: string
- container: set
  name: choices
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: clientId
  type: string
- container: ''
  name: clientSecret
  type: string
- container: ''
  name: client_id
  type: string
- container: ''
  name: client_secret
  type: string
- container: ''
  name: code
  type: string
- container: ''
  name: commentary
  type: string
- container: ''
  name: companyApplyUrl
  type: reference
- container: ''
  name: companyDomain
  type: string
- container: ''
  name: companyName
  type: string
- container: ''
  name: companyPageUrl
  type: string
- container: ''
  name: configVersion
  type: string
- container: ''
  name: configurationValue
  type: string
- container: ''
  name: contentUrn
  type: string
- container: ''
  name: contract
  type: string
- container: ''
  name: conversionMethod
  type: string
- container: ''
  name: count
  type: integer
- container: ''
  name: country
  type: string
- container: ''
  name: coverLetterQuestionRequirement
  type: string
- container: ''
  name: coverLetterQuestions
  type: string
- container: ''
  name: coverPhotoV2
  type: string
- container: ''
  name: created
  type: integer
- container: ''
  name: createdAt
  type: string
- container: ''
  name: cropInfo
  type: string
- container: ''
  name: cropped
  type: string
- container: ''
  name: currency
  type: string
- container: ''
  name: currencyCode
  type: string
- container: ''
  name: currentCompanyName
  type: string
- container: ''
  name: currentJobTitle
  type: string
- container: set
  name: customQuestionSets
  type: string
- container: ''
  name: dailyBudget
  type: string
- container: ''
  name: day
  type: integer
- container: ''
  name: defaultLocale
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: destination
  type: string
- container: set
  name: destinations
  type: string
- container: ''
  name: developerApplication
  type: string
- container: ''
  name: displayValue
  type: string
- container: ''
  name: dispositionReason
  type: string
- container: ''
  name: downloadUrl
  type: reference
- container: ''
  name: downloadUrlExpiresAt
  type: string
- container: set
  name: downloadUrls
  type: string
- container: ''
  name: educationExperienceQuestionSet
  type: string
- container: ''
  name: educationQuestions
  type: string
- container: set
  name: elements
  type: string
- container: set
  name: emailAddresses
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: end
  type: string
- container: ''
  name: endAt
  type: integer
- container: ''
  name: engagementMetricQualifier
  type: string
- container: ''
  name: engagementType
  type: string
- container: ''
  name: engagementValue
  type: integer
- container: ''
  name: entities
  type: string
- container: ''
  name: entity
  type: string
- container: ''
  name: entityCount
  type: integer
- container: ''
  name: entityPercentage
  type: integer
- container: ''
  name: entityStatus
  type: string
- container: set
  name: entityTypes
  type: string
- container: ''
  name: errors
  type: string
- container: ''
  name: expireAt
  type: string
- container: ''
  name: expires_in
  type: integer
- container: ''
  name: expiryTime
  type: integer
- container: ''
  name: exportEndAt
  type: string
- container: ''
  name: exportStartAt
  type: string
- container: ''
  name: extension
  type: string
- container: ''
  name: externalJobPostingId
  type: string
- container: ''
  name: externalProfileUrl
  type: reference
- container: ''
  name: facetName
  type: string
- container: ''
  name: facetUrn
  type: string
- container: ''
  name: firstDegreeSize
  type: integer
- container: ''
  name: firstEngagedAt
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: formResponse
  type: string
- container: ''
  name: foundedOn
  type: string
- container: ''
  name: geoLocation
  type: string
- container: ''
  name: geographicArea
  type: string
- container: ''
  name: geographicAreaType
  type: string
- container: ''
  name: grant_type
  type: string
- container: ''
  name: groupUrn
  type: string
- container: ''
  name: groupedBy
  type: string
- container: set
  name: groups
  type: string
- container: ''
  name: hasReportingAccess
  type: boolean
- container: ''
  name: headline
  type: string
- container: ''
  name: href
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: idType
  type: string
- container: ''
  name: idValue
  type: string
- container: ''
  name: impressions
  type: integer
- container: ''
  name: include
  type: string
- container: set
  name: industries
  type: string
- container: set
  name: industriesV2
  type: string
- container: ''
  name: inputCount
  type: integer
- container: ''
  name: inputFile
  type: string
- container: ''
  name: instanceId
  type: string
- container: ''
  name: integrationContext
  type: string
- container: ''
  name: jobApplicationWebhookUrl
  type: reference
- container: ''
  name: jobId
  type: string
- container: ''
  name: jobPostingOperationType
  type: string
- container: ''
  name: language
  type: string
- container: ''
  name: lastEngagedAt
  type: string
- container: ''
  name: lastModified
  type: integer
- container: ''
  name: lastName
  type: string
- container: ''
  name: latestDataAt
  type: string
- container: ''
  name: leadMetadata
  type: string
- container: ''
  name: leadType
  type: string
- container: ''
  name: learnerDetails
  type: string
- container: ''
  name: learnerUrn
  type: string
- container: ''
  name: lifecycleState
  type: string
- container: ''
  name: line1
  type: string
- container: set
  name: links
  type: string
- container: ''
  name: listedAt
  type: string
- container: ''
  name: listingType
  type: string
- container: ''
  name: localized
  type: string
- container: ''
  name: localizedDescription
  type: string
- container: ''
  name: localizedName
  type: string
- container: set
  name: localizedSpecialties
  type: string
- container: ''
  name: localizedTagline
  type: string
- container: ''
  name: localizedWebsite
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: locationType
  type: string
- container: set
  name: locations
  type: string
- container: ''
  name: logoV2
  type: string
- container: ''
  name: matchedCount
  type: integer
- container: ''
  name: member
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: method
  type: string
- container: ''
  name: middleInitial
  type: string
- container: ''
  name: month
  type: integer
- container: ''
  name: multipleChoiceQuestionDetails
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: nextExportStartAt
  type: string
- container: ''
  name: note
  type: string
- container: ''
  name: notifiedOnCampaignOptimization
  type: boolean
- container: ''
  name: notifiedOnCreativeApproval
  type: boolean
- container: ''
  name: notifiedOnCreativeRejection
  type: boolean
- container: ''
  name: notifiedOnEndOfCampaign
  type: boolean
- container: ''
  name: number
  type: string
- container: set
  name: oauth2AuthorizedCallbackUrls
  type: string
- container: ''
  name: objectiveType
  type: string
- container: ''
  name: onsiteApplyConfiguration
  type: string
- container: ''
  name: organization
  type: string
- container: ''
  name: organizationType
  type: string
- container: ''
  name: original
  type: string
- container: ''
  name: owner
  type: string
- container: ''
  name: paging
  type: string
- container: ''
  name: parentActivity
  type: string
- container: ''
  name: parentRelationship
  type: string
- container: set
  name: parentSiblingActivities
  type: string
- container: ''
  name: partner
  type: string
- container: ''
  name: partnerQuestionIdentifier
  type: string
- container: ''
  name: patch
  type: string
- container: set
  name: phoneNumbers
  type: string
- container: ''
  name: postClickAttributionWindowSize
  type: integer
- container: ''
  name: postalCode
  type: string
- container: ''
  name: preferredFormComponent
  type: string
- container: ''
  name: preferredLocale
  type: string
- container: ''
  name: prefix
  type: string
- container: ''
  name: primaryOrganizationType
  type: string
- container: ''
  name: processedActivity
  type: string
- container: ''
  name: processedAt
  type: string
- container: ''
  name: profile
  type: reference
- container: ''
  name: profilePhoto
  type: reference
- container: ''
  name: questionDetails
  type: string
- container: ''
  name: questionSetId
  type: string
- container: ''
  name: questionText
  type: string
- container: set
  name: questions
  type: string
- container: ''
  name: recordId
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: rel
  type: string
- container: ''
  name: request
  type: string
- container: ''
  name: required
  type: boolean
- container: ''
  name: resourceId
  type: string
- container: ''
  name: resourceName
  type: string
- container: ''
  name: resourceUri
  type: string
- container: ''
  name: results
  type: string
- container: ''
  name: resumeQuestionRequirement
  type: string
- container: ''
  name: resumeQuestions
  type: string
- container: ''
  name: role
  type: string
- container: ''
  name: roleAssignee
  type: string
- container: ''
  name: rowCount
  type: integer
- container: ''
  name: runSchedule
  type: string
- container: set
  name: segmentations
  type: string
- container: ''
  name: selectMultiple
  type: boolean
- container: ''
  name: serviceErrorCode
  type: integer
- container: set
  name: siblingActivities
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: sourcePlatform
  type: string
- container: set
  name: specialties
  type: string
- container: ''
  name: sponsoredAccount
  type: string
- container: ''
  name: sponsoredAccountId
  type: string
- container: ''
  name: sponsoredAccountUrn
  type: string
- container: ''
  name: staffCountRange
  type: string
- container: ''
  name: start
  type: integer
- container: ''
  name: startAt
  type: integer
- container: ''
  name: state
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: statuses
  type: string
- container: ''
  name: submittedAt
  type: integer
- container: ''
  name: submitter
  type: string
- container: ''
  name: suffix
  type: string
- container: ''
  name: symbolicName
  type: string
- container: ''
  name: tagline
  type: string
- container: ''
  name: test
  type: boolean
- container: ''
  name: testLead
  type: boolean
- container: ''
  name: time
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: token
  type: string
- container: ''
  name: token_type
  type: string
- container: ''
  name: total
  type: integer
- container: ''
  name: totalBudget
  type: string
- container: ''
  name: totalSpend
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: uniqueForeignId
  type: string
- container: set
  name: urlRules
  type: string
- container: ''
  name: urn
  type: string
- container: ''
  name: user
  type: string
- container: set
  name: userIds
  type: string
- container: set
  name: validJsSdkDomains
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: vanityName
  type: string
- container: ''
  name: variables
  type: string
- container: ''
  name: versionTag
  type: string
- container: ''
  name: versionedLeadGenFormUrn
  type: string
- container: ''
  name: viewThroughAttributionWindowSize
  type: integer
- container: ''
  name: visibility
  type: string
- container: ''
  name: voluntarySelfIdentificationQuestions
  type: string
- container: ''
  name: website
  type: string
- container: ''
  name: workExperienceQuestionSet
  type: string
- container: ''
  name: workQuestions
  type: string
- container: ''
  name: year
  type: integer
property_count: 265
provider_name: LinkedIn
provider_slug: linkedin
slug: linkedin-api-context
tags:
- Business
- Careers
- Marketing
- Professional Networking
- Recruiting
- Social Media
- JSON-LD
- Linked Data
- Semantic Web
---
