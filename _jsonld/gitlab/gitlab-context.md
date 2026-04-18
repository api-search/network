---
class_count: 38
classes:
- API_Entities_AccessRequester
- API_Entities_Appearance
- API_Entities_ApplicationWithSecret
- API_Entities_Avatar
- API_Entities_Badge
- API_Entities_BasicBadgeDetails
- API_Entities_BatchedBackgroundMigration
- API_Entities_Branch
- API_Entities_BroadcastMessage
- API_Entities_BulkImport
- API_Entities_BulkImports
- API_Entities_Ci_Variable
- API_Entities_Cluster
- API_Entities_Commit
- API_Entities_CustomAttribute
- API_Entities_Dictionary_Table
- API_Entities_Job
- API_Entities_Metadata
- API_Entities_MetricImage
- API_Entities_PlanLimit
- API_Entities_Platform_Kubernetes
- API_Entities_ProjectIdentity
- API_Entities_Provider_Gcp
- API_Entities_UserBasic
- DeviceAuthorizationRequest
- DeviceAuthorizationResponse
- GitLab Issue
- GitLab Merge Request
- GitLab Pipeline
- GitLab Project
- RevokeTokenRequest
- TokenInfo
- TokenRequest
- TokenResponse
- UserInfo
- Webhook
- WebhookEvent
- WebhookInput
context_file: json-ld/gitlab-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/gitlab/refs/heads/main/json-ld/gitlab-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Gitlab from GitLab.
layout: jsonld
name: Gitlab Context
namespaces:
- prefix: gl
  uri: https://docs.gitlab.com/api/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: access_token
  type: string
- container: ''
  name: active
  type: string
- container: ''
  name: alert_status
  type: string
- container: ''
  name: allow_failure
  type: boolean
- container: ''
  name: api_url
  type: string
- container: ''
  name: application
  type: reference
- container: ''
  name: application_id
  type: string
- container: ''
  name: application_name
  type: string
- container: ''
  name: archived
  type: boolean
- container: set
  name: artifacts
  type: string
- container: set
  name: assignees
  type: string
- container: ''
  name: author
  type: string
- container: ''
  name: author_email
  type: string
- container: ''
  name: author_name
  type: string
- container: ''
  name: authored_date
  type: dateTime
- container: ''
  name: authorization_type
  type: string
- container: ''
  name: avatar_path
  type: string
- container: ''
  name: avatar_url
  type: string
- container: ''
  name: before_sha
  type: string
- container: ''
  name: branch_filter_strategy
  type: string
- container: ''
  name: broadcast_type
  type: string
- container: ''
  name: builds_access_level
  type: string
- container: ''
  name: bulk_import_id
  type: string
- container: ''
  name: ca_cert
  type: string
- container: ''
  name: callback_url
  type: string
- container: ''
  name: can_push
  type: boolean
- container: ''
  name: changes_count
  type: string
- container: ''
  name: ci_active_jobs
  type: string
- container: ''
  name: ci_config_path
  type: string
- container: ''
  name: ci_needs_size_limit
  type: string
- container: ''
  name: ci_pipeline_schedules
  type: string
- container: ''
  name: ci_pipeline_size
  type: string
- container: ''
  name: ci_project_subscriptions
  type: string
- container: ''
  name: ci_registered_group_runners
  type: string
- container: ''
  name: ci_registered_project_runners
  type: string
- container: ''
  name: client_id
  type: string
- container: ''
  name: client_secret
  type: string
- container: ''
  name: closed_at
  type: dateTime
- container: ''
  name: closed_by
  type: string
- container: ''
  name: cluster_id
  type: string
- container: ''
  name: cluster_type
  type: string
- container: ''
  name: code
  type: string
- container: ''
  name: code_verifier
  type: string
- container: ''
  name: color
  type: string
- container: ''
  name: commit
  type: string
- container: ''
  name: committed_at
  type: dateTime
- container: ''
  name: committed_date
  type: dateTime
- container: ''
  name: committer_email
  type: string
- container: ''
  name: committer_name
  type: string
- container: ''
  name: conan_max_file_size
  type: string
- container: ''
  name: confidential
  type: boolean
- container: ''
  name: confidential_issues_events
  type: boolean
- container: ''
  name: confidential_note_events
  type: boolean
- container: ''
  name: container_registry_access_level
  type: string
- container: ''
  name: coverage
  type: string
- container: ''
  name: created_at
  type: dateTime
- container: ''
  name: creator_id
  type: integer
- container: set
  name: custom_attributes
  type: string
- container: ''
  name: default
  type: boolean
- container: ''
  name: default_branch
  type: string
- container: ''
  name: deployment_events
  type: boolean
- container: ''
  name: description
  type: string
- container: ''
  name: destination_full_path
  type: string
- container: ''
  name: destination_name
  type: string
- container: ''
  name: destination_namespace
  type: string
- container: ''
  name: destination_slug
  type: string
- container: ''
  name: detailed_merge_status
  type: string
- container: ''
  name: developers_can_merge
  type: boolean
- container: ''
  name: developers_can_push
  type: boolean
- container: ''
  name: device_code
  type: string
- container: ''
  name: disabled_until
  type: dateTime
- container: ''
  name: dismissable
  type: string
- container: ''
  name: domain
  type: string
- container: ''
  name: downvotes
  type: integer
- container: ''
  name: draft
  type: boolean
- container: ''
  name: due_date
  type: string
- container: ''
  name: duration
  type: integer
- container: ''
  name: email
  type: string
- container: ''
  name: email_header_and_footer_enabled
  type: string
- container: ''
  name: email_verified
  type: boolean
- container: ''
  name: empty_repo
  type: boolean
- container: ''
  name: enable_ssl_verification
  type: boolean
- container: ''
  name: enabled
  type: string
- container: ''
  name: endpoint
  type: string
- container: ''
  name: ends_at
  type: string
- container: ''
  name: enforcement_limit
  type: string
- container: ''
  name: enterprise
  type: boolean
- container: ''
  name: entity_type
  type: string
- container: ''
  name: environment_scope
  type: string
- container: ''
  name: erased_at
  type: dateTime
- container: ''
  name: execution_duration
  type: decimal
- container: ''
  name: expires_in
  type: integer
- container: ''
  name: expires_in_seconds
  type: integer
- container: set
  name: failures
  type: string
- container: ''
  name: favicon
  type: string
- container: set
  name: feature_categories
  type: string
- container: ''
  name: file_path
  type: string
- container: ''
  name: filename
  type: string
- container: ''
  name: finished_at
  type: dateTime
- container: ''
  name: font
  type: string
- container: ''
  name: footer_message
  type: string
- container: ''
  name: forks_count
  type: integer
- container: ''
  name: gcp_project_id
  type: string
- container: ''
  name: generic_packages_max_file_size
  type: string
- container: ''
  name: grant_type
  type: string
- container: set
  name: groups
  type: string
- container: ''
  name: has_tasks
  type: boolean
- container: ''
  name: header_logo
  type: string
- container: ''
  name: header_message
  type: string
- container: ''
  name: helm_max_file_size
  type: string
- container: ''
  name: http_url_to_repo
  type: reference
- container: ''
  name: id
  type: string
- container: ''
  name: iid
  type: integer
- container: ''
  name: image_url
  type: string
- container: ''
  name: interval
  type: integer
- container: ''
  name: issue_type
  type: string
- container: ''
  name: issues_access_level
  type: string
- container: ''
  name: issues_events
  type: boolean
- container: ''
  name: job_class_name
  type: string
- container: ''
  name: job_events
  type: boolean
- container: ''
  name: kas
  type: reference
- container: ''
  name: key
  type: string
- container: ''
  name: kind
  type: string
- container: set
  name: labels
  type: string
- container: ''
  name: last_activity_at
  type: dateTime
- container: ''
  name: limits_history
  type: reference
- container: ''
  name: link_url
  type: string
- container: ''
  name: logo
  type: string
- container: ''
  name: machine_type
  type: string
- container: ''
  name: managed
  type: string
- container: ''
  name: management_project
  type: string
- container: ''
  name: masked
  type: boolean
- container: ''
  name: maven_max_file_size
  type: string
- container: ''
  name: member_events
  type: boolean
- container: ''
  name: merge_commit_sha
  type: string
- container: ''
  name: merge_requests_access_level
  type: string
- container: ''
  name: merge_requests_count
  type: integer
- container: ''
  name: merge_requests_events
  type: boolean
- container: ''
  name: merge_user
  type: string
- container: ''
  name: merged
  type: boolean
- container: ''
  name: merged_at
  type: dateTime
- container: ''
  name: message
  type: string
- container: ''
  name: message_background_color
  type: string
- container: ''
  name: message_font_color
  type: string
- container: ''
  name: migrate_projects
  type: boolean
- container: ''
  name: milestone
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: name_with_namespace
  type: string
- container: ''
  name: namespace
  type: string
- container: ''
  name: namespace_id
  type: string
- container: ''
  name: namespace_per_environment
  type: string
- container: ''
  name: new_project_guidelines
  type: string
- container: ''
  name: nickname
  type: string
- container: ''
  name: note_events
  type: boolean
- container: ''
  name: notification_limit
  type: string
- container: ''
  name: npm_max_file_size
  type: string
- container: ''
  name: nuget_max_file_size
  type: string
- container: ''
  name: num_nodes
  type: string
- container: ''
  name: open_issues_count
  type: integer
- container: ''
  name: owner
  type: string
- container: ''
  name: pages_access_level
  type: string
- container: ''
  name: parent_id
  type: string
- container: set
  name: parent_ids
  type: string
- container: ''
  name: password
  type: string
- container: ''
  name: path
  type: string
- container: ''
  name: path_with_namespace
  type: string
- container: ''
  name: permissions
  type: string
- container: ''
  name: picture
  type: reference
- container: ''
  name: pipeline_events
  type: boolean
- container: ''
  name: pipeline_hierarchy_size
  type: string
- container: ''
  name: platform_kubernetes
  type: string
- container: ''
  name: platform_type
  type: string
- container: ''
  name: prepared_at
  type: dateTime
- container: ''
  name: profile
  type: reference
- container: ''
  name: profile_image_guidelines
  type: string
- container: ''
  name: progress
  type: string
- container: ''
  name: project
  type: reference
- container: ''
  name: project_id
  type: string
- container: ''
  name: protected
  type: boolean
- container: ''
  name: provider_gcp
  type: string
- container: ''
  name: provider_type
  type: string
- container: ''
  name: push_events
  type: boolean
- container: ''
  name: push_events_branch_filter
  type: string
- container: ''
  name: pwa_description
  type: string
- container: ''
  name: pwa_icon
  type: string
- container: ''
  name: pwa_name
  type: string
- container: ''
  name: pwa_short_name
  type: string
- container: ''
  name: pypi_max_file_size
  type: string
- container: ''
  name: queued_duration
  type: decimal
- container: ''
  name: raw
  type: boolean
- container: ''
  name: readme_url
  type: reference
- container: ''
  name: redirect_uri
  type: reference
- container: ''
  name: ref
  type: string
- container: ''
  name: references
  type: string
- container: ''
  name: refresh_token
  type: string
- container: ''
  name: releases_events
  type: boolean
- container: ''
  name: rendered_image_url
  type: string
- container: ''
  name: rendered_link_url
  type: string
- container: ''
  name: request_data
  type: string
- container: ''
  name: request_headers
  type: reference
- container: ''
  name: requested_at
  type: string
- container: ''
  name: resource_owner_id
  type: integer
- container: ''
  name: response_body
  type: string
- container: ''
  name: response_headers
  type: reference
- container: ''
  name: response_status
  type: string
- container: set
  name: reviewers
  type: string
- container: ''
  name: revision
  type: string
- container: ''
  name: scope
  type: string
- container: ''
  name: secret
  type: string
- container: ''
  name: secret_token
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: sha
  type: string
- container: ''
  name: short_id
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: source_branch
  type: string
- container: ''
  name: source_full_path
  type: string
- container: ''
  name: source_project_id
  type: integer
- container: ''
  name: source_type
  type: string
- container: ''
  name: squash
  type: boolean
- container: ''
  name: squash_commit_sha
  type: string
- container: ''
  name: ssh_url_to_repo
  type: string
- container: ''
  name: stage
  type: string
- container: ''
  name: star_count
  type: integer
- container: ''
  name: started_at
  type: dateTime
- container: ''
  name: starts_at
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: statistics
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: status_name
  type: string
- container: ''
  name: storage_size_limit
  type: string
- container: ''
  name: sub
  type: string
- container: ''
  name: table_name
  type: string
- container: ''
  name: tag
  type: boolean
- container: ''
  name: tag_push_events
  type: boolean
- container: ''
  name: target_access_levels
  type: string
- container: ''
  name: target_branch
  type: string
- container: ''
  name: target_path
  type: string
- container: ''
  name: target_project_id
  type: integer
- container: ''
  name: task_completion_status
  type: string
- container: ''
  name: terraform_module_max_file_size
  type: string
- container: ''
  name: time_stats
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
- container: set
  name: topics
  type: string
- container: ''
  name: trailers
  type: reference
- container: ''
  name: trigger
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: updated_at
  type: dateTime
- container: ''
  name: upvotes
  type: integer
- container: ''
  name: url
  type: string
- container: ''
  name: url_text
  type: string
- container: ''
  name: user
  type: string
- container: ''
  name: user_code
  type: string
- container: ''
  name: user_notes_count
  type: integer
- container: ''
  name: username
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: variable_type
  type: string
- container: ''
  name: verification_uri
  type: reference
- container: ''
  name: verification_uri_complete
  type: reference
- container: ''
  name: version
  type: string
- container: ''
  name: visibility
  type: string
- container: ''
  name: web_url
  type: string
- container: ''
  name: weight
  type: integer
- container: ''
  name: wiki_access_level
  type: string
- container: ''
  name: wiki_page_events
  type: boolean
- container: ''
  name: yaml_errors
  type: string
- container: ''
  name: zone
  type: string
property_count: 268
provider_name: GitLab
provider_slug: gitlab
slug: gitlab-context
tags:
- Code
- Platform
- Software Development
- Source Control
- JSON-LD
- Linked Data
- Semantic Web
---
