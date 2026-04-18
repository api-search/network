---
class_count: 85
classes:
- GitHub Commit
- GitHub Issue
- GitHub Organization
- GitHub Pull Request
- GitHub Repository
- GitHub User
- GitHub Webhook Delivery
- api-overview
- app-permissions
- application-grant
- authorization
- autolink
- base-gist
- basic-error
- code-of-conduct
- collaborator
- configuration-status
- enterprise-settings
- feed
- ghes-config-nodes
- ghes-replication-status
- gist-comment
- gist-commit
- gist-simple
- gitignore-template
- global-hook
- global-hook-2
- group-response
- hook-delivery
- hook-delivery-item
- installation-token
- integration
- integration-installation-request
- ldap-mapping-team
- ldap-mapping-user
- maintenance-status
- meta
- minimal-repository
- nullable-collaborator
- nullable-license-simple
- nullable-milestone
- nullable-simple-user
- nullable-team-simple
- organization-custom-repository-role
- organization-full
- organization-simple
- pre-receive-environment
- project
- project-card
- project-collaborator-permission
- project-column
- public-key-full
- public-user
- rate-limit
- rate-limit-overview
- reaction
- repository-collaborator-permission
- repository-invitation
- repository-subscription
- root
- scim-error
- security-and-analysis
- simple-user
- ssh-key
- starred-repository
- team
- team-discussion
- team-discussion-comment
- team-full
- team-project
- thread
- thread-subscription
- user-name-response
- user-response
- validation-error
- validation-error-simple
- webhook-branch-protection-rule-created
- webhook-branch-protection-rule-deleted
- webhook-branch-protection-rule-edited
- webhook-cache-sync
- webhook-check-run-completed
- webhook-check-run-completed-form-encoded
- webhook-check-run-created
- webhook-check-run-created-form-encoded
- webhook-config
context_file: json-ld/github-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/json-ld/github-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Github from GitHub.
layout: jsonld
name: Github Context
namespaces:
- prefix: gh
  uri: https://docs.github.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: enterprise
  type: string
- container: ''
  name: event
  type: string
- container: ''
  name: installation
  type: string
- container: ''
  name: license
  type: string
- container: ''
  name: repository
  type: string
- container: ''
  name: _links
  type: reference
- container: ''
  name: access_tokens_url
  type: reference
- container: ''
  name: account
  type: string
- container: ''
  name: action
  type: string
- container: ''
  name: actions
  type: string
- container: ''
  name: active
  type: boolean
- container: ''
  name: active_lock_reason
  type: string
- container: ''
  name: actor
  type: string
- container: ''
  name: added_by
  type: string
- container: ''
  name: additions
  type: integer
- container: ''
  name: administration
  type: string
- container: ''
  name: advanced_security
  type: reference
- container: ''
  name: advanced_security_enabled_for_new_repositories
  type: boolean
- container: ''
  name: after
  type: string
- container: ''
  name: allow_auto_merge
  type: boolean
- container: ''
  name: allow_forking
  type: boolean
- container: ''
  name: allow_merge_commit
  type: boolean
- container: ''
  name: allow_rebase_merge
  type: boolean
- container: ''
  name: allow_squash_merge
  type: boolean
- container: ''
  name: allow_update_branch
  type: boolean
- container: ''
  name: anonymous_access_enabled
  type: boolean
- container: ''
  name: app
  type: reference
- container: ''
  name: app_id
  type: integer
- container: ''
  name: app_slug
  type: string
- container: ''
  name: archive_url
  type: string
- container: ''
  name: archived
  type: boolean
- container: ''
  name: assignee
  type: string
- container: set
  name: assignees
  type: string
- container: ''
  name: assignees_url
  type: string
- container: ''
  name: author
  type: string
- container: ''
  name: author_association
  type: string
- container: ''
  name: authorizations_url
  type: string
- container: ''
  name: auto_merge
  type: reference
- container: ''
  name: avatar_url
  type: reference
- container: ''
  name: base
  type: string
- container: ''
  name: base_role
  type: string
- container: ''
  name: before
  type: string
- container: ''
  name: billing_email
  type: string
- container: ''
  name: bio
  type: string
- container: ''
  name: blobs_url
  type: string
- container: ''
  name: blog
  type: string
- container: ''
  name: body
  type: string
- container: ''
  name: body_html
  type: string
- container: ''
  name: body_version
  type: string
- container: ''
  name: branches_url
  type: string
- container: ''
  name: business_plus
  type: boolean
- container: ''
  name: cache_location
  type: string
- container: ''
  name: cards_url
  type: reference
- container: ''
  name: change_status
  type: reference
- container: ''
  name: changed_files
  type: integer
- container: ''
  name: changes
  type: reference
- container: ''
  name: check_run
  type: string
- container: ''
  name: checks
  type: string
- container: ''
  name: client_id
  type: string
- container: ''
  name: client_secret
  type: string
- container: ''
  name: clone_url
  type: string
- container: ''
  name: closed_at
  type: dateTime
- container: ''
  name: closed_by
  type: string
- container: ''
  name: closed_issues
  type: integer
- container: ''
  name: code_of_conduct
  type: string
- container: ''
  name: code_search_url
  type: string
- container: ''
  name: codespaces
  type: string
- container: ''
  name: collaborators
  type: integer
- container: ''
  name: collaborators_url
  type: string
- container: ''
  name: column_name
  type: string
- container: ''
  name: column_url
  type: reference
- container: ''
  name: columns_url
  type: reference
- container: ''
  name: comments
  type: integer
- container: ''
  name: comments_count
  type: integer
- container: ''
  name: comments_url
  type: reference
- container: ''
  name: commit
  type: string
- container: ''
  name: commit_search_url
  type: string
- container: ''
  name: commits
  type: integer
- container: ''
  name: commits_url
  type: reference
- container: ''
  name: committed_at
  type: dateTime
- container: ''
  name: committer
  type: string
- container: ''
  name: company
  type: string
- container: ''
  name: compare_url
  type: string
- container: set
  name: conditions
  type: string
- container: ''
  name: config
  type: reference
- container: set
  name: connection_services
  type: string
- container: ''
  name: contact_email
  type: string
- container: ''
  name: content
  type: string
- container: ''
  name: content_type
  type: string
- container: ''
  name: content_url
  type: reference
- container: ''
  name: contents
  type: string
- container: ''
  name: contents_url
  type: string
- container: ''
  name: contributors_url
  type: reference
- container: ''
  name: created
  type: string
- container: ''
  name: created_at
  type: dateTime
- container: ''
  name: creator
  type: string
- container: ''
  name: current_user_actor_url
  type: string
- container: ''
  name: current_user_authorizations_html_url
  type: string
- container: ''
  name: current_user_organization_url
  type: string
- container: set
  name: current_user_organization_urls
  type: string
- container: ''
  name: current_user_public_url
  type: string
- container: ''
  name: current_user_repositories_url
  type: string
- container: ''
  name: current_user_url
  type: string
- container: ''
  name: default_branch
  type: string
- container: ''
  name: default_environment
  type: boolean
- container: ''
  name: default_repository_permission
  type: string
- container: ''
  name: delete_branch_on_merge
  type: boolean
- container: ''
  name: deletions
  type: integer
- container: ''
  name: delivered_at
  type: dateTime
- container: set
  name: dependabot
  type: string
- container: ''
  name: dependabot_alerts_enabled_for_new_repositories
  type: boolean
- container: ''
  name: dependabot_secrets
  type: string
- container: ''
  name: dependabot_security_updates_enabled_for_new_repositories
  type: boolean
- container: ''
  name: dependency_graph_enabled_for_new_repositories
  type: boolean
- container: ''
  name: deployments
  type: string
- container: ''
  name: deployments_url
  type: reference
- container: ''
  name: description
  type: string
- container: ''
  name: detail
  type: string
- container: ''
  name: diff_url
  type: reference
- container: ''
  name: disabled
  type: boolean
- container: ''
  name: discussion_url
  type: reference
- container: ''
  name: disk_usage
  type: integer
- container: ''
  name: displayName
  type: string
- container: ''
  name: documentation_url
  type: string
- container: ''
  name: domains
  type: reference
- container: ''
  name: download
  type: reference
- container: ''
  name: downloads_url
  type: reference
- container: ''
  name: draft
  type: boolean
- container: ''
  name: due_on
  type: dateTime
- container: ''
  name: duration
  type: decimal
- container: ''
  name: email
  type: string
- container: ''
  name: email_addresses
  type: string
- container: ''
  name: emails
  type: string
- container: ''
  name: emails_url
  type: string
- container: ''
  name: emojis_url
  type: string
- container: ''
  name: environments
  type: string
- container: set
  name: errors
  type: string
- container: set
  name: events
  type: string
- container: ''
  name: events_url
  type: string
- container: ''
  name: expired
  type: boolean
- container: ''
  name: expires_at
  type: dateTime
- container: ''
  name: externalId
  type: string
- container: ''
  name: external_url
  type: reference
- container: ''
  name: familyName
  type: string
- container: ''
  name: featured
  type: boolean
- container: ''
  name: feeds_url
  type: string
- container: set
  name: files
  type: string
- container: ''
  name: fingerprint
  type: string
- container: ''
  name: followers
  type: integer
- container: ''
  name: followers_url
  type: reference
- container: ''
  name: following
  type: integer
- container: ''
  name: following_url
  type: string
- container: ''
  name: fork
  type: boolean
- container: ''
  name: fork_of
  type: reference
- container: set
  name: forks
  type: string
- container: ''
  name: forks_count
  type: integer
- container: ''
  name: forks_url
  type: reference
- container: ''
  name: formatted
  type: string
- container: ''
  name: full_name
  type: string
- container: ''
  name: gists_url
  type: string
- container: ''
  name: git_commits_url
  type: string
- container: ''
  name: git_pull_url
  type: reference
- container: ''
  name: git_push_url
  type: reference
- container: ''
  name: git_refs_url
  type: string
- container: ''
  name: git_ssh_keys
  type: string
- container: ''
  name: git_tags_url
  type: string
- container: ''
  name: git_url
  type: string
- container: ''
  name: givenName
  type: string
- container: ''
  name: gpg_keys
  type: string
- container: ''
  name: gravatar_id
  type: string
- container: ''
  name: guid
  type: string
- container: ''
  name: has_discussions
  type: boolean
- container: ''
  name: has_downloads
  type: boolean
- container: ''
  name: has_issues
  type: boolean
- container: ''
  name: has_multiple_single_files
  type: boolean
- container: ''
  name: has_organization_projects
  type: boolean
- container: ''
  name: has_pages
  type: boolean
- container: ''
  name: has_projects
  type: boolean
- container: ''
  name: has_repository_projects
  type: boolean
- container: ''
  name: has_wiki
  type: boolean
- container: ''
  name: hashed_token
  type: string
- container: ''
  name: head
  type: string
- container: ''
  name: hireable
  type: boolean
- container: set
  name: history
  type: string
- container: ''
  name: homepage
  type: reference
- container: ''
  name: hooks_count
  type: integer
- container: ''
  name: hooks_url
  type: string
- container: ''
  name: html_url
  type: reference
- container: ''
  name: hub_url
  type: string
- container: ''
  name: id
  type: integer
- container: ''
  name: ignored
  type: boolean
- container: ''
  name: image_url
  type: string
- container: ''
  name: implementation
  type: string
- container: ''
  name: insecure_ssl
  type: string
- container: ''
  name: installation_id
  type: integer
- container: ''
  name: installations_count
  type: integer
- container: ''
  name: installed_version
  type: string
- container: ''
  name: interaction_limits
  type: string
- container: ''
  name: invitee
  type: string
- container: ''
  name: inviter
  type: string
- container: ''
  name: is_alphanumeric
  type: boolean
- container: ''
  name: is_template
  type: boolean
- container: ''
  name: is_verified
  type: boolean
- container: ''
  name: issue_comment_url
  type: string
- container: ''
  name: issue_events_url
  type: string
- container: ''
  name: issue_search_url
  type: string
- container: ''
  name: issues
  type: string
- container: ''
  name: issues_url
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: key_prefix
  type: string
- container: ''
  name: keys_url
  type: string
- container: ''
  name: label_search_url
  type: string
- container: set
  name: labels
  type: string
- container: ''
  name: labels_url
  type: string
- container: ''
  name: language
  type: string
- container: ''
  name: languages_url
  type: reference
- container: ''
  name: lastModified
  type: string
- container: ''
  name: last_edited_at
  type: dateTime
- container: ''
  name: last_read_at
  type: string
- container: ''
  name: last_used
  type: dateTime
- container: ''
  name: ldap_dn
  type: string
- container: ''
  name: limit
  type: integer
- container: set
  name: limitations
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: locked
  type: boolean
- container: ''
  name: login
  type: string
- container: ''
  name: master_branch
  type: string
- container: ''
  name: members
  type: string
- container: ''
  name: members_allowed_repository_creation_type
  type: string
- container: ''
  name: members_can_create_internal_repositories
  type: boolean
- container: ''
  name: members_can_create_pages
  type: boolean
- container: ''
  name: members_can_create_private_pages
  type: boolean
- container: ''
  name: members_can_create_private_repositories
  type: boolean
- container: ''
  name: members_can_create_public_pages
  type: boolean
- container: ''
  name: members_can_create_public_repositories
  type: boolean
- container: ''
  name: members_can_create_repositories
  type: boolean
- container: ''
  name: members_can_fork_private_repositories
  type: boolean
- container: ''
  name: members_count
  type: integer
- container: ''
  name: members_url
  type: string
- container: ''
  name: merge_commit_message
  type: string
- container: ''
  name: merge_commit_sha
  type: string
- container: ''
  name: merge_commit_title
  type: string
- container: ''
  name: mergeable
  type: boolean
- container: ''
  name: mergeable_state
  type: string
- container: ''
  name: merged
  type: boolean
- container: ''
  name: merged_at
  type: dateTime
- container: ''
  name: merged_by
  type: string
- container: ''
  name: merges_url
  type: reference
- container: ''
  name: message
  type: string
- container: ''
  name: metadata
  type: string
- container: ''
  name: middleName
  type: string
- container: ''
  name: milestone
  type: string
- container: ''
  name: milestones_url
  type: string
- container: ''
  name: mirror_url
  type: reference
- container: ''
  name: name
  type: string
- container: ''
  name: network_count
  type: integer
- container: ''
  name: node_id
  type: string
- container: set
  name: nodes
  type: string
- container: ''
  name: note
  type: string
- container: ''
  name: note_url
  type: reference
- container: ''
  name: notifications_url
  type: string
- container: ''
  name: number
  type: integer
- container: ''
  name: open_issues
  type: integer
- container: ''
  name: open_issues_count
  type: integer
- container: ''
  name: org
  type: string
- container: ''
  name: organization
  type: string
- container: ''
  name: organization_administration
  type: string
- container: ''
  name: organization_announcement_banners
  type: string
- container: ''
  name: organization_copilot_seat_management
  type: string
- container: ''
  name: organization_custom_roles
  type: string
- container: ''
  name: organization_events
  type: string
- container: ''
  name: organization_hooks
  type: string
- container: ''
  name: organization_packages
  type: string
- container: ''
  name: organization_permission
  type: string
- container: ''
  name: organization_personal_access_token_requests
  type: string
- container: ''
  name: organization_personal_access_tokens
  type: string
- container: ''
  name: organization_plan
  type: string
- container: ''
  name: organization_projects
  type: string
- container: ''
  name: organization_repositories_url
  type: string
- container: ''
  name: organization_secrets
  type: string
- container: ''
  name: organization_self_hosted_runners
  type: string
- container: ''
  name: organization_teams_url
  type: string
- container: ''
  name: organization_url
  type: string
- container: ''
  name: organization_user_blocking
  type: string
- container: ''
  name: organizations_url
  type: reference
- container: ''
  name: owned_private_repos
  type: integer
- container: ''
  name: owner
  type: string
- container: ''
  name: owner_url
  type: reference
- container: ''
  name: packages
  type: string
- container: ''
  name: pages
  type: string
- container: ''
  name: parent
  type: string
- container: set
  name: parents
  type: string
- container: ''
  name: patch_url
  type: reference
- container: ''
  name: payload
  type: string
- container: ''
  name: pem
  type: string
- container: ''
  name: permission
  type: string
- container: ''
  name: permissions
  type: string
- container: ''
  name: ping_url
  type: string
- container: ''
  name: pinned
  type: boolean
- container: ''
  name: plan
  type: reference
- container: ''
  name: pretty-print
  type: string
- container: ''
  name: privacy
  type: string
- container: ''
  name: private
  type: boolean
- container: ''
  name: private_gists
  type: integer
- container: ''
  name: profile
  type: string
- container: set
  name: progress
  type: string
- container: ''
  name: project_id
  type: string
- container: ''
  name: project_url
  type: reference
- container: ''
  name: public
  type: boolean
- container: ''
  name: public_gists
  type: integer
- container: ''
  name: public_gists_url
  type: string
- container: ''
  name: public_members_url
  type: string
- container: ''
  name: public_repos
  type: integer
- container: ''
  name: pull_request
  type: reference
- container: ''
  name: pull_requests
  type: string
- container: ''
  name: pulls_url
  type: string
- container: ''
  name: pushed_at
  type: dateTime
- container: ''
  name: rate
  type: string
- container: ''
  name: rate_limit_url
  type: string
- container: ''
  name: reactions
  type: string
- container: ''
  name: read_only
  type: boolean
- container: ''
  name: reason
  type: string
- container: ''
  name: received_events_url
  type: reference
- container: ''
  name: redelivery
  type: boolean
- container: ''
  name: ref
  type: string
- container: ''
  name: releases_url
  type: string
- container: ''
  name: remaining
  type: integer
- container: ''
  name: repo
  type: reference
- container: ''
  name: repos_count
  type: integer
- container: ''
  name: repos_url
  type: reference
- container: set
  name: repositories
  type: string
- container: ''
  name: repositories_url
  type: reference
- container: ''
  name: repository_discussions_category_url
  type: string
- container: ''
  name: repository_discussions_url
  type: string
- container: ''
  name: repository_hooks
  type: string
- container: ''
  name: repository_id
  type: integer
- container: ''
  name: repository_projects
  type: string
- container: ''
  name: repository_search_url
  type: string
- container: ''
  name: repository_selection
  type: string
- container: ''
  name: repository_url
  type: string
- container: ''
  name: request
  type: reference
- container: set
  name: requested_reviewers
  type: string
- container: set
  name: requested_teams
  type: string
- container: ''
  name: requester
  type: string
- container: ''
  name: reset
  type: integer
- container: ''
  name: resourceType
  type: string
- container: ''
  name: resources
  type: reference
- container: ''
  name: response
  type: reference
- container: ''
  name: review_comments
  type: integer
- container: ''
  name: role_name
  type: string
- container: ''
  name: roles
  type: string
- container: ''
  name: rule
  type: reference
- container: set
  name: run_list
  type: string
- container: ''
  name: scheduled_time
  type: string
- container: set
  name: schemas
  type: string
- container: ''
  name: scimType
  type: string
- container: set
  name: scopes
  type: string
- container: ''
  name: secret
  type: string
- container: ''
  name: secret_scanning
  type: reference
- container: ''
  name: secret_scanning_alerts
  type: string
- container: ''
  name: secret_scanning_enabled_for_new_repositories
  type: boolean
- container: ''
  name: secret_scanning_push_protection
  type: reference
- container: ''
  name: secret_scanning_push_protection_custom_link
  type: string
- container: ''
  name: secret_scanning_push_protection_custom_link_enabled
  type: boolean
- container: ''
  name: secret_scanning_push_protection_enabled_for_new_repositories
  type: boolean
- container: ''
  name: secrets
  type: string
- container: ''
  name: security_advisories_url
  type: string
- container: ''
  name: security_and_analysis
  type: string
- container: ''
  name: security_events
  type: string
- container: ''
  name: sender
  type: string
- container: ''
  name: sha
  type: string
- container: ''
  name: single_file
  type: string
- container: ''
  name: single_file_name
  type: string
- container: set
  name: single_file_paths
  type: string
- container: ''
  name: site_admin
  type: boolean
- container: ''
  name: size
  type: integer
- container: ''
  name: slug
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: spdx_id
  type: string
- container: ''
  name: squash_merge_commit_message
  type: string
- container: ''
  name: squash_merge_commit_title
  type: string
- container: ''
  name: ssh_url
  type: string
- container: ''
  name: stargazers_count
  type: integer
- container: ''
  name: stargazers_url
  type: reference
- container: ''
  name: starred_at
  type: string
- container: ''
  name: starred_gists_url
  type: string
- container: ''
  name: starred_url
  type: string
- container: ''
  name: starring
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: state_reason
  type: string
- container: ''
  name: stats
  type: reference
- container: ''
  name: status
  type: string
- container: ''
  name: status_code
  type: integer
- container: ''
  name: statuses
  type: string
- container: ''
  name: statuses_url
  type: string
- container: ''
  name: subject
  type: reference
- container: ''
  name: subscribed
  type: boolean
- container: ''
  name: subscribers_count
  type: integer
- container: ''
  name: subscribers_url
  type: reference
- container: ''
  name: subscription_url
  type: string
- container: ''
  name: subscriptions_url
  type: reference
- container: ''
  name: suspended_at
  type: dateTime
- container: ''
  name: suspended_by
  type: string
- container: ''
  name: svn_url
  type: reference
- container: ''
  name: tags_url
  type: reference
- container: ''
  name: target_id
  type: integer
- container: ''
  name: target_type
  type: string
- container: ''
  name: team_discussions
  type: string
- container: ''
  name: team_url
  type: reference
- container: ''
  name: teams_url
  type: reference
- container: ''
  name: temp_clone_token
  type: string
- container: ''
  name: thread_url
  type: reference
- container: ''
  name: throttled_at
  type: dateTime
- container: ''
  name: timeline_url
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: token
  type: string
- container: ''
  name: token_last_eight
  type: string
- container: ''
  name: topic_search_url
  type: string
- container: set
  name: topics
  type: string
- container: ''
  name: topology
  type: string
- container: ''
  name: total_private_repos
  type: integer
- container: ''
  name: trees_url
  type: string
- container: ''
  name: truncated
  type: boolean
- container: ''
  name: twitter_username
  type: string
- container: ''
  name: two_factor_authentication
  type: boolean
- container: ''
  name: two_factor_requirement_enabled
  type: boolean
- container: ''
  name: type
  type: string
- container: ''
  name: unread
  type: boolean
- container: ''
  name: updated_at
  type: dateTime
- container: ''
  name: url
  type: reference
- container: ''
  name: url_template
  type: string
- container: ''
  name: use_squash_pr_title_as_default
  type: boolean
- container: ''
  name: used
  type: integer
- container: ''
  name: user
  type: string
- container: ''
  name: userName
  type: string
- container: ''
  name: user_id
  type: integer
- container: ''
  name: user_organizations_url
  type: string
- container: ''
  name: user_repositories_url
  type: string
- container: ''
  name: user_search_url
  type: string
- container: ''
  name: user_url
  type: string
- container: ''
  name: verifiable_password_authentication
  type: boolean
- container: ''
  name: verified
  type: boolean
- container: ''
  name: version
  type: string
- container: ''
  name: visibility
  type: string
- container: ''
  name: vulnerability_alerts
  type: string
- container: ''
  name: watchers
  type: integer
- container: ''
  name: watchers_count
  type: integer
- container: ''
  name: web_commit_signoff_required
  type: boolean
- container: ''
  name: webhook_secret
  type: string
- container: ''
  name: website_url
  type: reference
- container: ''
  name: workflows
  type: string
property_count: 451
provider_name: GitHub
provider_slug: github
slug: github-context
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
- JSON-LD
- Linked Data
- Semantic Web
---
