---
consumed_apis:
- whatsapp-business-mgmt
- whatsapp-cloud
description: Unified workflow for managing WhatsApp Business Accounts, phone numbers, business profiles, user assignments, product catalogs, and phone registration. Combines Business Management API and Cloud API capabilities used by platform administrators and business operations teams.
layout: capability
name: WhatsApp Account And Phone Management
operations:
- description: Retrieves information about a WhatsApp Business Account.
  method: GET
  name: get-business-account
  path: /v1/business-accounts/{waba_id}
- description: Lists all phone numbers associated with a WABA.
  method: GET
  name: list-phone-numbers
  path: /v1/phone-numbers
- description: Retrieves information about a registered phone number.
  method: GET
  name: get-phone-number
  path: /v1/phone-numbers/{phone_number_id}
- description: Retrieves the WhatsApp Business profile.
  method: GET
  name: get-business-profile
  path: /v1/business-profiles
- description: Updates the WhatsApp Business profile.
  method: POST
  name: update-business-profile
  path: /v1/business-profiles
- description: Lists assigned users.
  method: GET
  name: list-assigned-users
  path: /v1/assigned-users
- description: Assigns a user to a WABA.
  method: POST
  name: assign-user
  path: /v1/assigned-users
- description: Removes an assigned user.
  method: DELETE
  name: remove-assigned-user
  path: /v1/assigned-users
- description: Lists product catalogs.
  method: GET
  name: list-product-catalogs
  path: /v1/product-catalogs
- description: Connects a product catalog.
  method: POST
  name: connect-product-catalog
  path: /v1/product-catalogs
- description: Disconnects a product catalog.
  method: DELETE
  name: disconnect-product-catalog
  path: /v1/product-catalogs
- description: Sets or updates the two-step verification PIN.
  method: POST
  name: set-two-step-verification
  path: /v1/two-step-verification
- description: Requests a verification code.
  method: POST
  name: request-verification-code
  path: /v1/registrations/request-code
- description: Verifies a phone number.
  method: POST
  name: verify-code
  path: /v1/registrations/verify-code
- description: Registers a phone number for Cloud API.
  method: POST
  name: register-phone-number
  path: /v1/registrations/register
- description: Deregisters a phone number.
  method: POST
  name: deregister-phone-number
  path: /v1/registrations/deregister
personas: []
provider_name: WhatsApp
provider_slug: whatsapp
search_terms:
- removes an assigned user.
- whatsapp business account information.
- retrieves the whatsapp business profile.
- product catalog management.
- register phone number
- retrieves the whatsapp business profile for a phone number.
- disconnects a product catalog.
- registers a phone number for cloud api.
- register phone numbers.
- sets or updates the two-step verification pin for a phone number.
- verifies a phone number using a verification code.
- connects a product catalog.
- requests a verification code.
- assigns a user to a waba.
- phone numbers
- deregister phone number
- lists assigned users.
- connects a product catalog to a waba.
- get business profile
- sets or updates the two-step verification pin.
- updates the whatsapp business profile for a phone number.
- remove assigned user
- connect product catalog
- deregisters a phone number.
- requests a verification code via sms or voice call for phone registration.
- removes a user from a waba.
- get business account
- whatsapp
- assigns a user with specific tasks to a waba.
- disconnect product catalog
- deregisters a phone number from the cloud api.
- lists all users assigned to a waba.
- list phone numbers
- account management
- user assignments for a waba.
- request verification code
- user management
- verify phone numbers.
- deregister phone numbers.
- whatsapp business profile management.
- retrieves information about a whatsapp business account.
- lists product catalogs connected to a waba.
- verifies a phone number.
- product catalogs
- update business profile
- retrieves information about a registered phone number.
- list product catalogs
- registration
- set two step verification
- disconnects a product catalog from a waba.
- get phone number
- updates the whatsapp business profile.
- two-step verification pin management.
- verify code
- individual phone number information.
- business profile
- registers a phone number for use with the cloud api.
- phone numbers associated with a waba.
- list assigned users
- assign user
- request verification codes for registration.
- lists product catalogs.
- lists all phone numbers associated with a waba.
slug: account-and-phone-management
tags:
- WhatsApp
- Account Management
- Phone Numbers
- Business Profile
- Registration
- User Management
- Product Catalogs
tools:
- description: Retrieves information about a WhatsApp Business Account.
  hints:
    idempotent: true
    readOnly: true
  name: get-business-account
- description: Lists all phone numbers associated with a WABA.
  hints:
    idempotent: true
    readOnly: true
  name: list-phone-numbers
- description: Retrieves information about a registered phone number.
  hints:
    idempotent: true
    readOnly: true
  name: get-phone-number
- description: Retrieves the WhatsApp Business profile for a phone number.
  hints:
    idempotent: true
    readOnly: true
  name: get-business-profile
- description: Updates the WhatsApp Business profile for a phone number.
  hints:
    idempotent: true
    readOnly: false
  name: update-business-profile
- description: Lists all users assigned to a WABA.
  hints:
    idempotent: true
    readOnly: true
  name: list-assigned-users
- description: Assigns a user with specific tasks to a WABA.
  hints:
    destructive: false
    readOnly: false
  name: assign-user
- description: Removes a user from a WABA.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: remove-assigned-user
- description: Lists product catalogs connected to a WABA.
  hints:
    idempotent: true
    readOnly: true
  name: list-product-catalogs
- description: Connects a product catalog to a WABA.
  hints:
    destructive: false
    readOnly: false
  name: connect-product-catalog
- description: Disconnects a product catalog from a WABA.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: disconnect-product-catalog
- description: Sets or updates the two-step verification PIN for a phone number.
  hints:
    idempotent: true
    readOnly: false
  name: set-two-step-verification
- description: Requests a verification code via SMS or voice call for phone registration.
  hints:
    destructive: false
    readOnly: false
  name: request-verification-code
- description: Verifies a phone number using a verification code.
  hints:
    destructive: false
    readOnly: false
  name: verify-code
- description: Registers a phone number for use with the Cloud API.
  hints:
    destructive: false
    readOnly: false
  name: register-phone-number
- description: Deregisters a phone number from the Cloud API.
  hints:
    destructive: true
    readOnly: false
  name: deregister-phone-number
---
