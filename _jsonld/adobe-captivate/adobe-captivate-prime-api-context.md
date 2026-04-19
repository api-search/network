---
class_count: 45
classes:
- ResourceIdentifier
- SkillResponse
- LocalizedMetadata
- Notification
- LearningObjectResponse
- GamificationPointsResponse
- UserGroupListResponse
- Skill
- UserBadgeListResponse
- Catalog
- UserResponse
- EnrollmentListResponse
- NotificationListResponse
- UserSkillListResponse
- UserGroup
- EnrollmentCreateRequest
- UserGroupResponse
- CatalogListResponse
- LearningObjectInstance
- User
- CertificationListResponse
- CatalogResponse
- AccountResponse
- JobCreateRequest
- BadgeResponse
- EnrollmentResponse
- Relationship
- Account
- Job
- BadgeListResponse
- Badge
- GamificationPoints
- LearningObjectListResponse
- SkillListResponse
- PaginationLinks
- JobResponse
- Enrollment
- LearningObject
- LearningObjectInstanceListResponse
- JobListResponse
- UserUpdateRequest
- UserListResponse
- description
- name
- email
context_file: json-ld/adobe-captivate-prime-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adobe-captivate/refs/heads/main/json-ld/adobe-captivate-prime-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adobe Captivate Prime Api from Adobe Captivate.
layout: jsonld
name: Adobe Captivate Prime Api Context
namespaces:
- prefix: alm
  uri: https://learningmanager.adobe.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: data
  type: reference
- container: ''
  name: attributes
  type: reference
- container: ''
  name: state
  type: string
- container: ''
  name: relationships
  type: reference
- container: ''
  name: skillLevels
  type: reference
- container: ''
  name: links
  type: reference
- container: ''
  name: learningObjects
  type: reference
- container: ''
  name: locale
  type: string
- container: ''
  name: overview
  type: string
- container: ''
  name: richTextOverview
  type: string
- container: ''
  name: actionTaken
  type: boolean
- container: ''
  name: channel
  type: string
- container: ''
  name: dateCreated
  type: dateTime
- container: ''
  name: message
  type: reference
- container: ''
  name: modelType
  type: string
- container: ''
  name: read
  type: boolean
- container: set
  name: authorNames
  type: string
- container: ''
  name: datePublished
  type: dateTime
- container: ''
  name: dateUpdated
  type: dateTime
- container: ''
  name: duration
  type: integer
- container: ''
  name: effectiveModifiedDate
  type: dateTime
- container: ''
  name: enrollmentType
  type: string
- container: ''
  name: imageUrl
  type: reference
- container: ''
  name: loFormat
  type: string
- container: ''
  name: loType
  type: string
- container: set
  name: localizedMetadata
  type: string
- container: set
  name: tags
  type: string
- container: ''
  name: unenrollmentAllowed
  type: boolean
- container: ''
  name: instances
  type: reference
- container: ''
  name: skills
  type: reference
- container: ''
  name: prerequisiteLOs
  type: reference
- container: ''
  name: subLOs
  type: reference
- container: ''
  name: authors
  type: reference
- container: ''
  name: catalog
  type: reference
- container: set
  name: included
  type: string
- container: ''
  name: learnerPoints
  type: integer
- container: ''
  name: managerPoints
  type: integer
- container: ''
  name: overallPoints
  type: integer
- container: ''
  name: userCount
  type: integer
- container: ''
  name: self
  type: reference
- container: ''
  name: next
  type: reference
- container: ''
  name: prev
  type: reference
- container: ''
  name: related
  type: reference
- container: ''
  name: assertionUrl
  type: reference
- container: ''
  name: dateAchieved
  type: dateTime
- container: ''
  name: badge
  type: reference
- container: ''
  name: learningObject
  type: reference
- container: ''
  name: isDefault
  type: boolean
- container: ''
  name: isInternallySearchable
  type: boolean
- container: ''
  name: avatarUrl
  type: reference
- container: ''
  name: pointsEarned
  type: integer
- container: ''
  name: profile
  type: string
- container: set
  name: roles
  type: string
- container: ''
  name: userType
  type: string
- container: ''
  name: manager
  type: reference
- container: ''
  name: userGroups
  type: reference
- container: ''
  name: account
  type: reference
- container: ''
  name: completedOn
  type: dateTime
- container: ''
  name: dateEnrolled
  type: dateTime
- container: ''
  name: dateStarted
  type: dateTime
- container: ''
  name: hasPassed
  type: boolean
- container: ''
  name: progressPercent
  type: integer
- container: ''
  name: score
  type: decimal
- container: ''
  name: learner
  type: reference
- container: ''
  name: loInstance
  type: reference
- container: ''
  name: skill
  type: reference
- container: ''
  name: skillLevel
  type: reference
- container: ''
  name: loInstanceId
  type: string
- container: ''
  name: completionDeadline
  type: dateTime
- container: ''
  name: enrollmentDeadline
  type: dateTime
- container: ''
  name: seatLimit
  type: integer
- container: ''
  name: gamificationEnabled
  type: boolean
- container: ''
  name: subdomain
  type: string
- container: ''
  name: timezone
  type: string
- container: ''
  name: jobType
  type: string
- container: ''
  name: dateCompleted
  type: dateTime
- container: ''
  name: downloadUrl
  type: reference
- container: ''
  name: status
  type: string
property_count: 80
provider_name: Adobe Captivate
provider_slug: adobe-captivate
slug: adobe-captivate-prime-api-context
tags:
- Authoring
- Education
- eLearning
- LMS
- SCORM
- Training
- xAPI
- JSON-LD
- Linked Data
- Semantic Web
---
