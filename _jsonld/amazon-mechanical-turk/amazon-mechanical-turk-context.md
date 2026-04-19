---
class_count: 96
classes:
- AcceptQualificationRequestRequest
- AcceptQualificationRequestResponse
- ApproveAssignmentRequest
- ApproveAssignmentResponse
- Assignment
- AssociateQualificationWithWorkerRequest
- AssociateQualificationWithWorkerResponse
- BonusPayment
- CreateAdditionalAssignmentsForHITRequest
- CreateAdditionalAssignmentsForHITResponse
- CreateHITRequest
- CreateHITResponse
- CreateHITTypeRequest
- CreateHITTypeResponse
- CreateHITWithHITTypeRequest
- CreateHITWithHITTypeResponse
- CreateQualificationTypeRequest
- CreateQualificationTypeResponse
- CreateWorkerBlockRequest
- CreateWorkerBlockResponse
- DeleteHITRequest
- DeleteHITResponse
- DeleteQualificationTypeRequest
- DeleteQualificationTypeResponse
- DeleteWorkerBlockRequest
- DeleteWorkerBlockResponse
- DisassociateQualificationFromWorkerRequest
- DisassociateQualificationFromWorkerResponse
- GetAccountBalanceRequest
- GetAccountBalanceResponse
- GetAssignmentRequest
- GetAssignmentResponse
- GetFileUploadURLRequest
- GetFileUploadURLResponse
- GetHITRequest
- GetHITResponse
- GetQualificationScoreRequest
- GetQualificationScoreResponse
- GetQualificationTypeRequest
- GetQualificationTypeResponse
- HIT
- HITLayoutParameter
- ListAssignmentsForHITRequest
- ListAssignmentsForHITResponse
- ListBonusPaymentsRequest
- ListBonusPaymentsResponse
- ListHITsForQualificationTypeRequest
- ListHITsForQualificationTypeResponse
- ListHITsRequest
- ListHITsResponse
- ListQualificationRequestsRequest
- ListQualificationRequestsResponse
- ListQualificationTypesRequest
- ListQualificationTypesResponse
- ListReviewPolicyResultsForHITRequest
- ListReviewPolicyResultsForHITResponse
- ListReviewableHITsRequest
- ListReviewableHITsResponse
- ListWorkerBlocksRequest
- ListWorkerBlocksResponse
- ListWorkersWithQualificationTypeRequest
- ListWorkersWithQualificationTypeResponse
- Locale
- NotificationSpecification
- NotifyWorkersFailureStatus
- NotifyWorkersRequest
- NotifyWorkersResponse
- ParameterMapEntry
- PolicyParameter
- Qualification
- QualificationRequest
- QualificationRequirement
- QualificationType
- RejectAssignmentRequest
- RejectAssignmentResponse
- RejectQualificationRequestRequest
- RejectQualificationRequestResponse
- ReviewActionDetail
- ReviewPolicy
- ReviewReport
- ReviewResultDetail
- SendBonusRequest
- SendBonusResponse
- SendTestEventNotificationRequest
- SendTestEventNotificationResponse
- UpdateExpirationForHITRequest
- UpdateExpirationForHITResponse
- UpdateHITReviewStatusRequest
- UpdateHITReviewStatusResponse
- UpdateHITTypeOfHITRequest
- UpdateHITTypeOfHITResponse
- UpdateNotificationSettingsRequest
- UpdateNotificationSettingsResponse
- UpdateQualificationTypeRequest
- UpdateQualificationTypeResponse
- WorkerBlock
context_file: json-ld/amazon-mechanical-turk-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-mechanical-turk/refs/heads/main/json-ld/amazon-mechanical-turk-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Mechanical Turk from Amazon Mechanical Turk.
layout: jsonld
name: Amazon Mechanical Turk Context
namespaces:
- prefix: amtu
  uri: https://amtu.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: AcceptTime
  type: ''
- container: ''
  name: ActionId
  type: ''
- container: ''
  name: ActionName
  type: ''
- container: ''
  name: ActionsGuarded
  type: ''
- container: ''
  name: Active
  type: ''
- container: ''
  name: Answer
  type: ''
- container: ''
  name: AnswerKey
  type: ''
- container: ''
  name: ApprovalTime
  type: ''
- container: ''
  name: AssignmentDurationInSeconds
  type: ''
- container: ''
  name: AssignmentId
  type: ''
- container: ''
  name: AssignmentReviewPolicy
  type: ''
- container: ''
  name: AssignmentReviewReport
  type: ''
- container: ''
  name: AssignmentStatus
  type: ''
- container: ''
  name: AssignmentStatuses
  type: ''
- container: ''
  name: Assignments
  type: ''
- container: ''
  name: AutoApprovalDelayInSeconds
  type: ''
- container: ''
  name: AutoApprovalTime
  type: ''
- container: ''
  name: AutoGranted
  type: ''
- container: ''
  name: AutoGrantedValue
  type: ''
- container: ''
  name: AvailableBalance
  type: ''
- container: ''
  name: BonusAmount
  type: ''
- container: ''
  name: BonusPayments
  type: ''
- container: ''
  name: Comparator
  type: ''
- container: ''
  name: CompleteTime
  type: ''
- container: ''
  name: Country
  type: ''
- container: ''
  name: CreationTime
  type: ''
- container: ''
  name: Deadline
  type: ''
- container: ''
  name: Description
  type: ''
- container: ''
  name: Destination
  type: ''
- container: ''
  name: ErrorCode
  type: ''
- container: ''
  name: EventTypes
  type: ''
- container: ''
  name: Expiration
  type: ''
- container: ''
  name: ExpireAt
  type: ''
- container: ''
  name: FileUploadURL
  type: ''
- container: ''
  name: GrantTime
  type: ''
- container: ''
  name: HITGroupId
  type: ''
- container: ''
  name: HITId
  type: ''
- container: ''
  name: HITLayoutId
  type: ''
- container: ''
  name: HITLayoutParameters
  type: ''
- container: ''
  name: HITReviewPolicy
  type: ''
- container: ''
  name: HITReviewReport
  type: ''
- container: ''
  name: HITReviewStatus
  type: ''
- container: ''
  name: HITStatus
  type: ''
- container: ''
  name: HITTypeId
  type: ''
- container: ''
  name: HITs
  type: ''
- container: ''
  name: IntegerValue
  type: ''
- container: ''
  name: IntegerValues
  type: ''
- container: ''
  name: IsRequestable
  type: ''
- container: ''
  name: Key
  type: ''
- container: ''
  name: Keywords
  type: ''
- container: ''
  name: LifetimeInSeconds
  type: ''
- container: ''
  name: LocaleValue
  type: ''
- container: ''
  name: LocaleValues
  type: ''
- container: ''
  name: MapEntries
  type: ''
- container: ''
  name: MaxAssignments
  type: ''
- container: ''
  name: MaxResults
  type: ''
- container: ''
  name: MessageText
  type: ''
- container: ''
  name: MustBeOwnedByCaller
  type: ''
- container: ''
  name: MustBeRequestable
  type: ''
- container: ''
  name: Name
  type: ''
- container: ''
  name: NextToken
  type: ''
- container: ''
  name: Notification
  type: ''
- container: ''
  name: NotifyWorkersFailureCode
  type: ''
- container: ''
  name: NotifyWorkersFailureMessage
  type: ''
- container: ''
  name: NotifyWorkersFailureStatuses
  type: ''
- container: ''
  name: NumResults
  type: ''
- container: ''
  name: NumberOfAdditionalAssignments
  type: ''
- container: ''
  name: NumberOfAssignmentsAvailable
  type: ''
- container: ''
  name: NumberOfAssignmentsCompleted
  type: ''
- container: ''
  name: NumberOfAssignmentsPending
  type: ''
- container: ''
  name: OnHoldBalance
  type: ''
- container: ''
  name: OverrideRejection
  type: ''
- container: ''
  name: Parameters
  type: ''
- container: ''
  name: PolicyLevels
  type: ''
- container: ''
  name: PolicyName
  type: ''
- container: ''
  name: QualificationRequestId
  type: ''
- container: ''
  name: QualificationRequests
  type: ''
- container: ''
  name: QualificationRequirements
  type: ''
- container: ''
  name: QualificationTypeId
  type: ''
- container: ''
  name: QualificationTypeStatus
  type: ''
- container: ''
  name: QualificationTypes
  type: ''
- container: ''
  name: Qualifications
  type: ''
- container: ''
  name: Query
  type: ''
- container: ''
  name: Question
  type: ''
- container: ''
  name: QuestionId
  type: ''
- container: ''
  name: QuestionIdentifier
  type: ''
- container: ''
  name: Reason
  type: ''
- container: ''
  name: RejectionTime
  type: ''
- container: ''
  name: RequesterAnnotation
  type: ''
- container: ''
  name: RequesterFeedback
  type: ''
- container: ''
  name: RequiredToPreview
  type: ''
- container: ''
  name: Result
  type: ''
- container: ''
  name: RetrieveActions
  type: ''
- container: ''
  name: RetrieveResults
  type: ''
- container: ''
  name: RetryDelayInSeconds
  type: ''
- container: ''
  name: Revert
  type: ''
- container: ''
  name: ReviewActions
  type: ''
- container: ''
  name: ReviewResults
  type: ''
- container: ''
  name: Reward
  type: ''
- container: ''
  name: SendNotification
  type: ''
- container: ''
  name: Status
  type: ''
- container: ''
  name: Subdivision
  type: ''
- container: ''
  name: Subject
  type: ''
- container: ''
  name: SubjectId
  type: ''
- container: ''
  name: SubjectType
  type: ''
- container: ''
  name: SubmitTime
  type: ''
- container: ''
  name: TargetId
  type: ''
- container: ''
  name: TargetType
  type: ''
- container: ''
  name: Test
  type: ''
- container: ''
  name: TestDurationInSeconds
  type: ''
- container: ''
  name: TestEventType
  type: ''
- container: ''
  name: Title
  type: ''
- container: ''
  name: Transport
  type: ''
- container: ''
  name: UniqueRequestToken
  type: ''
- container: ''
  name: Value
  type: ''
- container: ''
  name: Values
  type: ''
- container: ''
  name: Version
  type: ''
- container: ''
  name: WorkerBlocks
  type: ''
- container: ''
  name: WorkerId
  type: ''
- container: ''
  name: WorkerIds
  type: ''
property_count: 120
provider_name: Amazon Mechanical Turk
provider_slug: amazon-mechanical-turk
slug: amazon-mechanical-turk-context
tags:
- AWS
- Crowdsourcing
- Human Intelligence
- Labor
- Machine Learning
- Tasks
- JSON-LD
- Linked Data
- Semantic Web
---
