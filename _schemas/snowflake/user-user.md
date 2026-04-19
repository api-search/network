---
description: Properties of user.
layout: schema
name: User
properties_list:
- description: User name
  name: name
  type: string
- description: Password
  name: password
  type: string
- description: Login name
  name: login_name
  type: string
- description: Display name
  name: display_name
  type: string
- description: First name
  name: first_name
  type: string
- description: Middle name
  name: middle_name
  type: string
- description: Last name
  name: last_name
  type: string
- description: Email address
  name: email
  type: string
- description: Does this user need to change their password (e.g., after assigning a temp password)
  name: must_change_password
  type: boolean
- description: Has this user been disabled from the system
  name: disabled
  type: boolean
- description: How many days until this user expires
  name: days_to_expiry
  type: integer
- description: How many minutes until the account is unlocked after multiple failed logins
  name: mins_to_unlock
  type: integer
- description: The default warehouse to use when this user starts a session
  name: default_warehouse
  type: string
- description: The default namespace to use when this user starts a session
  name: default_namespace
  type: string
- description: The default role to use when this user starts a session
  name: default_role
  type: string
- description: The default secondary roles of this user to use when starting a session. Only valid set values are ALL or NONE. Default is ALL after 2024-07 BCR.
  name: default_secondary_roles
  type: string
- description: How many minutes until MFA is required again
  name: mins_to_bypass_mfa
  type: integer
- description: RSA public key of the user
  name: rsa_public_key
  type: string
- description: Second RSA public key of the user
  name: rsa_public_key_2
  type: string
- description: Comment about the user.
  name: comment
  type: string
- description: Indicates the type of user (PERSON | SERVICE | LEGACY_SERVICE)
  name: type
  type: string
- description: Whether to show unredacted query syntax errors in the query history.
  name: enable_unredacted_query_syntax_error
  type: boolean
- description: Specifies an existing network policy is active for the user. Otherwise, use account default.
  name: network_policy
  type: string
- description: ''
  name: created_on
  type: string
- description: ''
  name: last_successful_login
  type: string
- description: ''
  name: expires_at
  type: string
- description: ''
  name: locked_until
  type: string
- description: ''
  name: has_password
  type: boolean
- description: ''
  name: has_rsa_public_key
  type: boolean
- description: Fingerprint of the user's RSA public key
  name: rsa_public_key_fp
  type: string
- description: Fingerprint of the user's second RSA public key
  name: rsa_public_key_2_fp
  type: string
- description: ''
  name: ext_authn_duo
  type: boolean
- description: ''
  name: ext_authn_uid
  type: string
- description: ''
  name: owner
  type: string
- description: Whether the user, account, or organization is locked by Snowflake.
  name: snowflake_lock
  type: boolean
- description: Whether Snowflake Support is allowed to use the user or account
  name: snowflake_support
  type: boolean
- description: Temporary bypass network policy on the user for a specified number of minutes
  name: mins_to_bypass_network_policy
  type: integer
- description: ''
  name: password_last_set
  type: string
- description: ''
  name: custom_landing_page_url
  type: string
- description: Whether or not to flush the custom landing page of the user on next UI load
  name: custom_landing_page_url_flush_next_ui_load
  type: boolean
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/user-user-schema.json
slug: user-user
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: User
---
