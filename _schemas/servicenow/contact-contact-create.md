---
description: Contact creation request
layout: schema
name: ContactCreate
properties_list:
- description: Contact full name
  name: name
  type: string
- description: Contact first name
  name: first_name
  type: string
- description: Contact middle name
  name: middle_name
  type: string
- description: Contact last name
  name: last_name
  type: string
- description: Contact user ID
  name: user_name
  type: string
- description: Contact email address
  name: email
  type: string
- description: Contact business phone number
  name: phone
  type: string
- description: Contact mobile phone number
  name: mobile_phone
  type: string
- description: Contact home phone number
  name: home_phone
  type: string
- description: Contact business title
  name: title
  type: string
- description: Contact employee number
  name: employee_number
  type: string
- description: Sys_id of the company record
  name: company
  type: string
- description: Sys_id of the account record
  name: account
  type: string
- description: Sys_id of the department
  name: department
  type: string
- description: Sys_id of the direct supervisor
  name: manager
  type: string
- description: Sys_id of the location
  name: location
  type: string
- description: Sys_id of the building
  name: building
  type: string
- description: Contact street address
  name: street
  type: string
- description: City in which the contact resides
  name: city
  type: string
- description: State in which the contact resides
  name: state
  type: string
- description: Contact zip code
  name: zip
  type: string
- description: Country code
  name: country
  type: string
- description: Flag indicating whether the contact is active
  name: active
  type: boolean
- description: Flag indicating whether the contact has VIP status
  name: vip
  type: boolean
- description: Flag indicating if the contact is locked-out
  name: locked_out
  type: boolean
- description: Flag indicating whether the contact can only access services through the web
  name: web_service_access_only
  type: boolean
- description: Flag indicating whether the contact is an internal integration user
  name: internal_integration_user
  type: boolean
- description: Flag indicating whether multifactor authorization is required
  name: enable_multifactor_authn
  type: boolean
- description: Flag indicating whether the contact location is obtained through geotracking
  name: geolocation_tracked
  type: boolean
- description: Indicates whether the contact should receive notifications (1=Disabled, 2=Enabled)
  name: notification
  type: integer
- description: Calendar application that the contact uses (1=Outlook)
  name: calendar_integration
  type: integer
- description: Number of failed login attempts
  name: failed_attempts
  type: integer
- description: Latitude coordinate of the contact
  name: latitude
  type: number
- description: Longitude coordinate of the contact
  name: longitude
  type: number
- description: Time zone in which the contact resides
  name: time_zone
  type: string
- description: Format in which to display dates
  name: date_format
  type: string
- description: Format in which to display time
  name: time_format
  type: string
- description: Country code of the contact primary language
  name: preferred_language
  type: string
- description: Contact gender
  name: gender
  type: string
- description: Photo image of the contact
  name: photo
  type: string
- description: Introduction
  name: introduction
  type: string
- description: Source of the contact
  name: source
  type: string
- description: List of user roles associated with the contact
  name: roles
  type: string
- description: Sys_id of the cost center
  name: cost_center
  type: string
- description: Sys_id of the work schedule
  name: schedule
  type: string
- description: Sys_id of the time sheet policy
  name: time_sheet_policy
  type: string
- description: Sys_id of the default perspective
  name: default_perspective
  type: string
- description: Sys_id of the LDAP server
  name: ldap_server
  type: string
- description: Status of the agent
  name: agent_status
  type: string
- description: Indicates the timeliness of dispatched service personnel
  name: on_schedule
  type: string
- description: Education status of the contact
  name: edu_status
  type: string
- description: Date and time the contact logged in to the system
  name: last_login_time
  type: string
- description: Device the consumer used the last time they logged in
  name: last_login_device
  type: string
- description: Social media channel (Twitter, Facebook, Instagram, etc.)
  name: social_channel
  type: string
- description: User handle on the social media channel
  name: social_handle
  type: string
- description: URL to the contact's social channel profile
  name: social_handle_url
  type: string
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/contact-contact-create-schema.json
slug: contact-contact-create
tags:
- Automation
- Cloud Services
- Digital Workflows
- Enterprise Platform
- IT Service Management
- ITSM
- Processes
- T1
- Workflow Automation
- Workflows
title: ContactCreate
---
