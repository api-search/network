---
class_count: 146
classes:
- ChoiceAnswerSummary
- ProfileSummary
- ChoiceImprovementPlan
- BestPractice
- RiskCounts
- CheckDetail
- DisassociateProfilesInput
- DeleteLensShareInput
- GetProfileOutput
- Profile
- ProfileTemplateQuestion
- ListProfilesOutput
- AssociateLensesInput
- ListLensesInput
- ImprovementSummary
- WorkloadDiscoveryConfig
- ListProfileSharesInput
- CreateProfileShareOutput
- AnswerSummary
- GetLensReviewInput
- GetProfileTemplateOutput
- GetLensOutput
- Lens
- GetLensVersionDifferenceOutput
- LensMetric
- GetWorkloadInput
- UpdateLensReviewInput
- PillarNotes
- QuestionMetric
- ListTagsForResourceInput
- ListProfileSharesOutput
- TagResourceOutput
- NotificationSummary
- GetLensReviewOutput
- LensReview
- UntagResourceOutput
- GetConsolidatedReportInput
- ChoiceUpdate
- CheckSummary
- ProfileQuestionUpdate
- GetMilestoneOutput
- Milestone
- CreateLensVersionOutput
- UpdateAnswerOutput
- Answer
- ListAnswersOutput
- ProfileTemplateChoice
- UpdateWorkloadInput
- TagMap
- ListLensReviewImprovementsOutput
- ChoiceAnswer
- ListShareInvitationsOutput
- ListLensReviewsInput
- DeleteWorkloadShareInput
- CreateLensShareOutput
- ListCheckSummariesOutput
- PillarReviewSummary
- GetLensReviewReportOutput
- LensReviewReport
- ChoiceContent
- ListProfileNotificationsOutput
- UpdateGlobalSettingsInput
- CreateMilestoneInput
- ListLensReviewsOutput
- ListNotificationsOutput
- ShareInvitationSummary
- PillarMetric
- ListLensesOutput
- UpdateShareInvitationOutput
- ShareInvitation
- AssociateProfilesInput
- DeleteLensInput
- GetAnswerOutput
- ListNotificationsInput
- GetMilestoneInput
- ListLensSharesInput
- WorkloadShareSummary
- CreateWorkloadShareOutput
- ListProfileNotificationsInput
- UpdateWorkloadShareInput
- ListWorkloadSharesOutput
- UpdateProfileOutput
- ImportLensInput
- DeleteWorkloadInput
- GetProfileTemplateInput
- ListMilestonesOutput
- CreateWorkloadShareInput
- CreateProfileOutput
- ProfileQuestion
- DeleteProfileInput
- ProfileShareSummary
- ExportLensOutput
- Choice
- AdditionalResources
- GetLensReviewReportInput
- GetProfileInput
- ProfileChoice
- UpdateShareInvitationInput
- ExportLensInput
- ListCheckDetailsInput
- CreateProfileShareInput
- GetAnswerInput
- UntagResourceInput
- ListCheckDetailsOutput
- CreateWorkloadInput
- ListMilestonesInput
- ListShareInvitationsInput
- ListProfilesInput
- UpdateProfileInput
- UpdateWorkloadShareOutput
- WorkloadShare
- ListCheckSummariesInput
- UpgradeProfileVersionInput
- UpdateWorkloadOutput
- LensShareSummary
- LensSummary
- UpgradeLensReviewInput
- ConsolidatedReportMetric
- DeleteProfileShareInput
- ListWorkloadsOutput
- ListAnswersInput
- ProfileNotificationSummary
- GetLensInput
- ListTagsForResourceOutput
- GetLensVersionDifferenceInput
- LensReviewSummary
- CreateLensShareInput
- CreateMilestoneOutput
- ListLensReviewImprovementsInput
- PillarDifference
- DisassociateLensesInput
- TagResourceInput
- ListWorkloadSharesInput
- CreateLensVersionInput
- WorkloadProfile
- GetWorkloadOutput
- ImportLensOutput
- GetConsolidatedReportOutput
- MilestoneSummary
- ListLensSharesOutput
- UpdateAnswerInput
- ListWorkloadsInput
- CreateProfileInput
- QuestionDifference
- CreateWorkloadOutput
- UpdateLensReviewOutput
context_file: json-ld/amazon-well-architected-tool-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-well-architected-tool/refs/heads/main/json-ld/amazon-well-architected-tool-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Well Architected Tool from Amazon Well-Architected Tool.
layout: jsonld
name: Amazon Well Architected Tool Context
namespaces:
- prefix: amz
  uri: https://amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: ChoiceId
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: Reason
  type: string
- container: ''
  name: ProfileArn
  type: string
- container: ''
  name: ProfileVersion
  type: string
- container: ''
  name: ProfileName
  type: string
- container: ''
  name: ProfileDescription
  type: string
- container: ''
  name: Owner
  type: string
- container: ''
  name: CreatedAt
  type: string
- container: ''
  name: UpdatedAt
  type: string
- container: ''
  name: DisplayText
  type: string
- container: ''
  name: ImprovementPlanUrl
  type: string
- container: ''
  name: ChoiceTitle
  type: string
- container: ''
  name: WorkloadSummary
  type: string
- container: ''
  name: WorkloadId
  type: string
- container: ''
  name: WorkloadArn
  type: string
- container: ''
  name: WorkloadName
  type: string
- container: ''
  name: Lenses
  type: string
- container: ''
  name: ImprovementStatus
  type: string
- container: ''
  name: Profiles
  type: string
- container: ''
  name: PrioritizedRiskCounts
  type: string
- container: ''
  name: Id
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: Description
  type: string
- container: ''
  name: Provider
  type: string
- container: ''
  name: LensArn
  type: string
- container: ''
  name: PillarId
  type: string
- container: ''
  name: QuestionId
  type: string
- container: ''
  name: AccountId
  type: string
- container: ''
  name: FlaggedResources
  type: string
- container: ''
  name: ProfileArns
  type: string
- container: ''
  name: ProfileTemplate
  type: string
- container: ''
  name: TemplateName
  type: string
- container: ''
  name: TemplateQuestions
  type: string
- container: ''
  name: QuestionTitle
  type: string
- container: ''
  name: QuestionDescription
  type: string
- container: ''
  name: QuestionChoices
  type: string
- container: ''
  name: MinSelectedChoices
  type: string
- container: ''
  name: MaxSelectedChoices
  type: string
- container: ''
  name: ProfileSummaries
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: LensAliases
  type: string
- container: ''
  name: Risk
  type: string
- container: ''
  name: ImprovementPlans
  type: string
- container: ''
  name: TrustedAdvisorIntegrationStatus
  type: string
- container: ''
  name: WorkloadResourceDefinition
  type: string
- container: ''
  name: AccountSummary
  type: string
- container: ''
  name: ShareId
  type: string
- container: ''
  name: LensUpgradeSummary
  type: string
- container: ''
  name: LensAlias
  type: string
- container: ''
  name: CurrentLensVersion
  type: string
- container: ''
  name: LatestLensVersion
  type: string
- container: ''
  name: VersionDifferences
  type: string
- container: ''
  name: PillarDifferences
  type: string
- container: ''
  name: Choices
  type: string
- container: ''
  name: SelectedChoices
  type: string
- container: ''
  name: ChoiceAnswerSummaries
  type: string
- container: ''
  name: IsApplicable
  type: string
- container: ''
  name: QuestionType
  type: string
- container: ''
  name: BaseLensVersion
  type: string
- container: ''
  name: TargetLensVersion
  type: string
- container: ''
  name: Pillars
  type: string
- container: ''
  name: LensNotes
  type: string
- container: ''
  name: BestPractices
  type: string
- container: ''
  name: ProfileShareSummaries
  type: string
- container: ''
  name: ChoiceUpdates
  type: string
- container: ''
  name: Type
  type: string
- container: ''
  name: MilestoneNumber
  type: string
- container: ''
  name: Notes
  type: string
- container: ''
  name: SelectedChoiceIds
  type: string
- container: ''
  name: LensVersion
  type: string
- container: ''
  name: AnswerSummaries
  type: string
- container: ''
  name: ChoiceDescription
  type: string
- container: ''
  name: Environment
  type: string
- container: ''
  name: AccountIds
  type: string
- container: ''
  name: AwsRegions
  type: string
- container: ''
  name: NonAwsRegions
  type: string
- container: ''
  name: PillarPriorities
  type: string
- container: ''
  name: ArchitecturalDesign
  type: string
- container: ''
  name: ReviewOwner
  type: string
- container: ''
  name: IsReviewOwnerUpdateAcknowledged
  type: string
- container: ''
  name: IndustryType
  type: string
- container: ''
  name: Industry
  type: string
- container: ''
  name: DiscoveryConfig
  type: string
- container: ''
  name: Applications
  type: string
- container: ''
  name: ImprovementSummaries
  type: string
- container: ''
  name: ShareInvitationSummaries
  type: string
- container: ''
  name: CheckSummaries
  type: string
- container: ''
  name: PillarName
  type: string
- container: ''
  name: Url
  type: string
- container: ''
  name: NotificationSummaries
  type: string
- container: ''
  name: OrganizationSharingStatus
  type: string
- container: ''
  name: DiscoveryIntegrationStatus
  type: string
- container: ''
  name: MilestoneName
  type: string
- container: ''
  name: ClientRequestToken
  type: string
- container: ''
  name: LensReviewSummaries
  type: string
- container: ''
  name: ShareInvitationId
  type: string
- container: ''
  name: SharedBy
  type: string
- container: ''
  name: SharedWith
  type: string
- container: ''
  name: PermissionType
  type: string
- container: ''
  name: ShareResourceType
  type: string
- container: ''
  name: LensName
  type: string
- container: ''
  name: Questions
  type: string
- container: ''
  name: LensSummaries
  type: string
- container: ''
  name: MaxResults
  type: string
- container: ''
  name: StatusMessage
  type: string
- container: ''
  name: WorkloadShareSummaries
  type: string
- container: ''
  name: Tags
  type: string
- container: ''
  name: Workload
  type: string
- container: ''
  name: ReviewRestrictionDate
  type: string
- container: ''
  name: JSONString
  type: string
- container: ''
  name: MilestoneSummaries
  type: string
- container: ''
  name: LensJSON
  type: string
- container: ''
  name: Title
  type: string
- container: ''
  name: HelpfulResource
  type: string
- container: ''
  name: ImprovementPlan
  type: string
- container: ''
  name: RecordedAt
  type: string
- container: ''
  name: ShareInvitationAction
  type: string
- container: ''
  name: CheckDetails
  type: string
- container: ''
  name: ProfileQuestions
  type: string
- container: ''
  name: HelpfulResourceUrl
  type: string
- container: ''
  name: HelpfulResourceDisplayText
  type: string
- container: ''
  name: ChoiceAnswers
  type: string
- container: ''
  name: LensType
  type: string
- container: ''
  name: LensStatus
  type: string
- container: ''
  name: MetricType
  type: string
- container: ''
  name: LensesAppliedCount
  type: string
- container: ''
  name: PillarReviewSummaries
  type: string
- container: ''
  name: WorkloadSummaries
  type: string
- container: ''
  name: Base64String
  type: string
- container: ''
  name: CurrentProfileVersion
  type: string
- container: ''
  name: LatestProfileVersion
  type: string
- container: ''
  name: Content
  type: string
- container: ''
  name: DifferenceStatus
  type: string
- container: ''
  name: QuestionDifferences
  type: string
- container: ''
  name: IsMajorVersion
  type: string
- container: ''
  name: Metrics
  type: string
- container: ''
  name: LensShareSummaries
  type: string
- container: ''
  name: WorkloadNamePrefix
  type: string
property_count: 139
provider_name: Amazon Well-Architected Tool
provider_slug: amazon-well-architected-tool
slug: amazon-well-architected-tool-context
tags:
- Architecture
- AWS
- Best Practices
- Cloud Governance
- Well-Architected
- Workloads
- JSON-LD
- Linked Data
- Semantic Web
---
