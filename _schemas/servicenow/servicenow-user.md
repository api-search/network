---
description: A ServiceNow user record from the sys_user table representing a person who can authenticate and interact with the platform.
layout: schema
name: ServiceNow User
properties_list:
- description: The unique 32-character system identifier for the user.
  name: sys_id
  type: string
- description: The login user name.
  name: user_name
  type: string
- description: The user's first name.
  name: first_name
  type:
  - string
  - 'null'
- description: The user's middle name.
  name: middle_name
  type:
  - string
  - 'null'
- description: The user's last name.
  name: last_name
  type:
  - string
  - 'null'
- description: The user's full display name.
  name: name
  type:
  - string
  - 'null'
- description: The user's email address.
  name: email
  type:
  - string
  - 'null'
- description: The user's business phone number.
  name: phone
  type:
  - string
  - 'null'
- description: The user's mobile phone number.
  name: mobile_phone
  type:
  - string
  - 'null'
- description: The user's job title.
  name: title
  type:
  - string
  - 'null'
- description: The employee number.
  name: employee_number
  type:
  - string
  - 'null'
- description: The user's department.
  name: department
  type: object
- description: The user's company.
  name: company
  type: object
- description: The user's direct manager.
  name: manager
  type: object
- description: The user's primary location.
  name: location
  type: object
- description: The user's building.
  name: building
  type: object
- description: The user's cost center.
  name: cost_center
  type: object
- description: The user's time zone.
  name: time_zone
  type:
  - string
  - 'null'
- description: Whether the user account is active.
  name: active
  type: boolean
- description: Whether the user account is locked out.
  name: locked_out
  type: boolean
- description: Whether the user has VIP status.
  name: vip
  type: boolean
- description: Comma-separated list of role names assigned to the user.
  name: roles
  type:
  - string
  - 'null'
- description: The source from which the user record was created.
  name: source
  type:
  - string
  - 'null'
- description: The date and time of the user's last login.
  name: last_login_time
  type:
  - string
  - 'null'
- description: The number of failed login attempts.
  name: failed_attempts
  type:
  - integer
  - 'null'
- description: The URL or reference to the user's photo.
  name: photo
  type:
  - string
  - 'null'
- description: The date and time the record was created.
  name: sys_created_on
  type: string
- description: The user who created the record.
  name: sys_created_by
  type: string
- description: The date and time the record was last updated.
  name: sys_updated_on
  type: string
- description: The user who last updated the record.
  name: sys_updated_by
  type: string
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-user-schema.json
slug: servicenow-user
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
title: ServiceNow User
---
