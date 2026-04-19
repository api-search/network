---
description: Person with whom a business unit has a relationship, such as a customer, supplier, or colleague. Corresponds to the contact entity type in the Microsoft.Dynamics.CRM namespace.
layout: schema
name: Contact
properties_list:
- description: Unique identifier of the contact.
  name: contactid
  type: string
- description: First name of the contact.
  name: firstname
  type: string
- description: Last name of the contact.
  name: lastname
  type: string
- description: Full name of the contact, combining first name, middle name, and last name.
  name: fullname
  type: string
- description: Middle name or initial of the contact.
  name: middlename
  type: string
- description: Nickname of the contact.
  name: nickname
  type: string
- description: Salutation for correspondence with the contact.
  name: salutation
  type: string
- description: Suffix used in the contact's name.
  name: suffix
  type: string
- description: Job title of the contact.
  name: jobtitle
  type: string
- description: Department or business unit where the contact works.
  name: department
  type: string
- description: Primary email address for the contact.
  name: emailaddress1
  type: string
- description: Secondary email address for the contact.
  name: emailaddress2
  type: string
- description: Alternate email address for the contact.
  name: emailaddress3
  type: string
- description: Main phone number for the contact.
  name: telephone1
  type: string
- description: Second phone number for the contact.
  name: telephone2
  type: string
- description: Third phone number for the contact.
  name: telephone3
  type: string
- description: Mobile phone number for the contact.
  name: mobilephone
  type: string
- description: Fax number for the contact.
  name: fax
  type: string
- description: Website URL for the contact.
  name: websiteurl
  type: string
- description: Additional information to describe the contact.
  name: description
  type: string
- description: Gender of the contact. 1 = Male, 2 = Female.
  name: gendercode
  type: integer
- description: Marital status of the contact. 1 = Single, 2 = Married, 3 = Divorced, 4 = Widowed.
  name: familystatuscode
  type: integer
- description: Birthday of the contact.
  name: birthdate
  type: string
- description: Anniversary date of the contact.
  name: anniversary
  type: string
- description: Name of the contact's spouse or partner.
  name: spousesname
  type: string
- description: Number of children the contact has.
  name: numberofchildren
  type: integer
- description: Descriptive name for the primary address.
  name: address1_name
  type: string
- description: First line of the primary address.
  name: address1_line1
  type: string
- description: Second line of the primary address.
  name: address1_line2
  type: string
- description: Third line of the primary address.
  name: address1_line3
  type: string
- description: City for the primary address.
  name: address1_city
  type: string
- description: State or province for the primary address.
  name: address1_stateorprovince
  type: string
- description: ZIP code or postal code for the primary address.
  name: address1_postalcode
  type: string
- description: Country or region for the primary address.
  name: address1_country
  type: string
- description: County for the primary address.
  name: address1_county
  type: string
- description: Main phone number for the primary address.
  name: address1_telephone1
  type: string
- description: Fax number for the primary address.
  name: address1_fax
  type: string
- description: Latitude value for the primary address.
  name: address1_latitude
  type: number
- description: Longitude value for the primary address.
  name: address1_longitude
  type: number
- description: Descriptive name for the secondary address.
  name: address2_name
  type: string
- description: First line of the secondary address.
  name: address2_line1
  type: string
- description: Second line of the secondary address.
  name: address2_line2
  type: string
- description: Third line of the secondary address.
  name: address2_line3
  type: string
- description: City for the secondary address.
  name: address2_city
  type: string
- description: State or province for the secondary address.
  name: address2_stateorprovince
  type: string
- description: ZIP code or postal code for the secondary address.
  name: address2_postalcode
  type: string
- description: Country or region for the secondary address.
  name: address2_country
  type: string
- description: Preferred method of contact. 1 = Any, 2 = Email, 3 = Phone, 4 = Fax, 5 = Mail.
  name: preferredcontactmethodcode
  type: integer
- description: Whether the contact allows direct email.
  name: donotemail
  type: boolean
- description: Whether the contact allows phone calls.
  name: donotphone
  type: boolean
- description: Whether the contact allows faxes.
  name: donotfax
  type: boolean
- description: Whether the contact allows direct mail.
  name: donotpostalmail
  type: boolean
- description: Whether the contact allows bulk email through campaigns.
  name: donotbulkemail
  type: boolean
- description: Whether the contact accepts marketing materials.
  name: donotsendmm
  type: boolean
- description: Credit limit of the contact.
  name: creditlimit
  type: number
- description: Whether the credit for the contact is on hold.
  name: creditonhold
  type: boolean
- description: Status of the contact. 0 = Active, 1 = Inactive. Inactive contacts are read-only.
  name: statecode
  type: integer
- description: Status reason for the contact. 1 = Active, 2 = Inactive.
  name: statuscode
  type: integer
- description: Date and time when the contact record was created.
  name: createdon
  type: string
- description: Date and time when the contact record was last updated.
  name: modifiedon
  type: string
- description: Version number of the contact record.
  name: versionnumber
  type: integer
- description: Lookup property for the parent customer (account or contact) associated with this contact.
  name: _parentcustomerid_value
  type: string
- description: Lookup property for the user or team assigned to manage the record.
  name: _ownerid_value
  type: string
- description: Lookup property for the currency associated with the record.
  name: _transactioncurrencyid_value
  type: string
- description: Phonetic spelling of the first name (Japanese).
  name: yomifirstname
  type: string
- description: Phonetic spelling of the last name (Japanese).
  name: yomilastname
  type: string
- description: Phonetic spelling of the middle name (Japanese).
  name: yomimiddlename
  type: string
- description: Phonetic spelling of the full name (Japanese).
  name: yomifullname
  type: string
provider_name: Microsoft Power Apps
provider_slug: microsoft-power-apps
schema_file: json-schema/microsoft-power-apps-dataverse-web-contact-schema.json
slug: microsoft-power-apps-dataverse-web-contact
tags:
- Business Applications
- Cloud
- Enterprise
- Low-Code
- Microsoft
- No-Code
- Power Platform
- SaaS
title: Contact
---
