---
description: A Google Workspace user account. JSON representation of a user resource from the Admin SDK Directory API.
layout: schema
name: User
properties_list:
- description: The type of the API resource.
  name: kind
  type: string
- description: The unique ID for the user.
  name: id
  type: string
- description: ETag of the resource.
  name: etag
  type: string
- description: The user primary email address. This property is required in a request to create a user account. The primaryEmail must be unique and cannot be an alias of another user.
  name: primaryEmail
  type: string
- description: Indicates a user with super administrator privileges. The isAdmin property can only be edited using the makeAdmin method; it is not directly editable in the user resource.
  name: isAdmin
  type: boolean
- description: Indicates if the user is a delegated administrator.
  name: isDelegatedAdmin
  type: boolean
- description: The last time the user logged into the user account. The value is in ISO 8601 date and time format.
  name: lastLoginTime
  type: string
- description: The time the user account was created. The value is in ISO 8601 date and time format.
  name: creationTime
  type: string
- description: The time the user account was deleted (for deleted users).
  name: deletionTime
  type: string
- description: Indicates whether the user has completed an initial login and accepted the Terms of Service.
  name: agreedToTerms
  type: boolean
- description: Stores the password for the user account. The password value is never returned in the API response body. Required when creating a user account. Must be 8-100 ASCII characters.
  name: password
  type: string
- description: Stores the hash format of the password property. Use MD5, SHA-1, or crypt for supported hash formats.
  name: hashFunction
  type: string
- description: Indicates if the user is suspended. A suspended user cannot sign in.
  name: suspended
  type: boolean
- description: The reason a user account is suspended. Only returned when the suspended property is true.
  name: suspensionReason
  type: string
- description: Indicates if the user is forced to change their password at next login.
  name: changePasswordAtNextLogin
  type: boolean
- description: If true, the user IP address is subject to a deprecated IP address allowlist configuration.
  name: ipWhitelisted
  type: boolean
- description: The customer ID to retrieve all account users. You can use the alias my_customer to represent the account customerId.
  name: customerId
  type: string
- description: The full path of the parent organization associated with the user. If the parent organization is the top-level, it is represented as a forward slash (/).
  name: orgUnitPath
  type: string
- description: Indicates if the user Gmail mailbox has been created.
  name: isMailboxSetup
  type: boolean
- description: Indicates if the user profile is visible in the Google Workspace global address list.
  name: includeInGlobalAddressList
  type: boolean
- description: Photo URL of the user. The URL might be temporary or private. Read-only.
  name: thumbnailPhotoUrl
  type: string
- description: ETag of the user photo.
  name: thumbnailPhotoEtag
  type: string
- description: Indicates if the user is archived.
  name: archived
  type: boolean
- description: Recovery email of the user.
  name: recoveryEmail
  type: string
- description: Recovery phone of the user in E.164 format.
  name: recoveryPhone
  type: string
- description: Is enrolled in 2-step verification. Read-only.
  name: isEnrolledIn2Sv
  type: boolean
- description: Is 2-step verification enforced. Read-only.
  name: isEnforcedIn2Sv
  type: boolean
- description: A list of the user email addresses. The maximum allowed data size is 10KB.
  name: emails
  type: array
- description: A list of the user phone numbers.
  name: phones
  type: array
- description: A list of the user addresses.
  name: addresses
  type: array
- description: A list of organizations the user belongs to.
  name: organizations
  type: array
- description: A list of the user relationships to other users.
  name: relations
  type: array
- description: A list of external IDs for the user.
  name: externalIds
  type: array
- description: A list of the user websites.
  name: websites
  type: array
- description: The user Instant Messenger (IM) accounts.
  name: ims
  type: array
- description: The user languages.
  name: languages
  type: array
- description: The user gender.
  name: gender
  type: object
- description: The user keywords.
  name: keywords
  type: array
- description: The user locations.
  name: locations
  type: array
- description: Notes for the user.
  name: notes
  type: object
- description: Custom fields of the user. Keys are schema names and values are objects with field name/value pairs.
  name: customSchemas
  type: object
provider_name: Google Workspace
provider_slug: google-workspace
schema_file: json-schema/admin-sdk-directory-user-schema.json
slug: admin-sdk-directory-user
tags:
- Calendar
- Collaboration
- Email
- Productivity
- Storage
- Video Conferencing
title: User
---
