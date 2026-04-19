---
channels:
- description: Events triggered when a learner enrolls in a course, learning program, certification, or job aid. Includes both self-enrollment and manager/admin-initiated enrollments.
  name: /learner-enrollment
  operation: subscribe
  operation_id: onLearnerEnrollment
  summary: Learner enrollment event
- description: Events triggered when a learner completes a course, learning program, or certification module. Includes completion status, score, and timestamp information.
  name: /learner-completion
  operation: subscribe
  operation_id: onLearnerCompletion
  summary: Learner completion event
- description: Events triggered when a learner's progress in a course or module is updated. Tracks incremental progress changes.
  name: /learner-progress
  operation: subscribe
  operation_id: onLearnerProgress
  summary: Learner progress update event
- description: Events triggered when a learner is unenrolled from a course, learning program, or certification.
  name: /learner-unenrollment
  operation: subscribe
  operation_id: onLearnerUnenrollment
  summary: Learner unenrollment event
- description: Events triggered when a new course or learning object is created in the Learning Manager account.
  name: /course-created
  operation: subscribe
  operation_id: onCourseCreated
  summary: Course creation event
- description: Events triggered when an existing course or learning object is modified, including content updates, metadata changes, and state transitions.
  name: /course-updated
  operation: subscribe
  operation_id: onCourseUpdated
  summary: Course update event
- description: Events triggered when a badge is awarded to a learner upon achieving a specific milestone or completing a learning objective.
  name: /badge-awarded
  operation: subscribe
  operation_id: onBadgeAwarded
  summary: Badge awarded event
- description: Events triggered when a learner completes a certification, including initial certification and recertification cycles.
  name: /certification-completed
  operation: subscribe
  operation_id: onCertificationCompleted
  summary: Certification completion event
- description: Events triggered when a learner achieves a new skill level through course completions or skill credit assignments.
  name: /skill-achieved
  operation: subscribe
  operation_id: onSkillAchieved
  summary: Skill achievement event
- description: Events triggered when a new user is created in the Learning Manager account, either through self-registration, admin creation, or bulk import.
  name: /user-created
  operation: subscribe
  operation_id: onUserCreated
  summary: User creation event
- description: Events triggered when a user's profile or state is updated, including role changes, group assignments, and status changes.
  name: /user-updated
  operation: subscribe
  operation_id: onUserUpdated
  summary: User update event
- description: Events triggered when a user is deleted or purged from the Learning Manager account.
  name: /user-deleted
  operation: subscribe
  operation_id: onUserDeleted
  summary: User deletion event
- description: Events triggered when a bulk import or export job completes, including status and result details.
  name: /job-completed
  operation: subscribe
  operation_id: onJobCompleted
  summary: Job completion event
description: The Adobe Learning Manager Webhooks API enables real-time event notifications for learning management activities. When configured, Adobe Learning Manager sends HTTP POST requests to registered webhook URLs whenever significant events occur, such as learner enrollments, course completions, certification achievements, badge awards, and administrative changes. Webhooks support real-time integration with external systems, enabling automated workflows for learner management, reporting, and compliance tracking. Events are delivered as JSON payloads with retry logic for failed deliveries.
layout: asyncapi
messages:
- description: ''
  name: LearnerEnrollmentEvent
  summary: Notification when a learner enrolls in a learning object
  title: Learner Enrollment Event
- description: ''
  name: LearnerCompletionEvent
  summary: Notification when a learner completes a learning object
  title: Learner Completion Event
- description: ''
  name: LearnerProgressEvent
  summary: Notification when learner progress is updated
  title: Learner Progress Event
- description: ''
  name: LearnerUnenrollmentEvent
  summary: Notification when a learner is unenrolled
  title: Learner Unenrollment Event
- description: ''
  name: CourseCreatedEvent
  summary: Notification when a new course is created
  title: Course Created Event
- description: ''
  name: CourseUpdatedEvent
  summary: Notification when a course is updated
  title: Course Updated Event
- description: ''
  name: BadgeAwardedEvent
  summary: Notification when a badge is awarded to a learner
  title: Badge Awarded Event
- description: ''
  name: CertificationCompletedEvent
  summary: Notification when a learner completes a certification
  title: Certification Completed Event
- description: ''
  name: SkillAchievedEvent
  summary: Notification when a learner achieves a new skill level
  title: Skill Achieved Event
- description: ''
  name: UserCreatedEvent
  summary: Notification when a new user is created
  title: User Created Event
- description: ''
  name: UserUpdatedEvent
  summary: Notification when a user is updated
  title: User Updated Event
- description: ''
  name: UserDeletedEvent
  summary: Notification when a user is deleted
  title: User Deleted Event
- description: ''
  name: JobCompletedEvent
  summary: Notification when a bulk job completes
  title: Job Completed Event
name: Adobe Learning Manager Webhooks API
provider_name: Adobe Captivate
provider_slug: adobe-captivate
servers:
- description: Your webhook receiver endpoint. Adobe Learning Manager sends HTTP POST requests to this URL when events occur. The URL must be HTTPS and publicly accessible.
  name: webhookReceiver
  protocol: https
  url: '{webhookUrl}'
slug: adobe-captivate-learning-manager-webhooks-asyncapi
spec_file: asyncapi/adobe-captivate-learning-manager-webhooks-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/adobe-captivate/refs/heads/main/asyncapi/adobe-captivate-learning-manager-webhooks-asyncapi.yml
tags:
- Authoring
- Education
- eLearning
- LMS
- SCORM
- Training
- xAPI
- AsyncAPI
- Webhooks
- Events
version: '1.0'
---
