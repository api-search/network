---
description: Business that represents a customer or potential customer. The company that is billed in business transactions. Corresponds to the account entity type in the Microsoft.Dynamics.CRM namespace.
layout: schema
name: Account
properties_list:
- description: Unique identifier of the account.
  name: accountid
  type: string
- description: Company or business name of the account.
  name: name
  type: string
- description: ID number or code for the account to quickly search and identify the account in system views.
  name: accountnumber
  type: string
- description: Category indicating whether the customer account is standard or preferred. 1 = Preferred Customer, 2 = Standard.
  name: accountcategorycode
  type: integer
- description: Classification code indicating the potential value of the customer account. 1 = Default Value.
  name: accountclassificationcode
  type: integer
- description: Rating indicating the value of the customer account.
  name: accountratingcode
  type: integer
- description: Additional information describing the account.
  name: description
  type: string
- description: Primary email address for the account.
  name: emailaddress1
  type: string
- description: Secondary email address for the account.
  name: emailaddress2
  type: string
- description: Alternate email address for the account.
  name: emailaddress3
  type: string
- description: Main phone number for the account.
  name: telephone1
  type: string
- description: Second phone number for the account.
  name: telephone2
  type: string
- description: Third phone number for the account.
  name: telephone3
  type: string
- description: Fax number for the account.
  name: fax
  type: string
- description: Website URL for the account.
  name: websiteurl
  type: string
- description: Primary industry of the account for marketing segmentation. Values include 1=Accounting, 2=Agriculture, 3=Broadcasting, 4=Brokers, 5=Building Supply, 6=Business Services, 7=Consulting, 8=Consumer Serv
  name: industrycode
  type: integer
- description: Number of employees at the account.
  name: numberofemployees
  type: integer
- description: Annual revenue for the account.
  name: revenue
  type: number
- description: Annual revenue converted to the system default base currency.
  name: revenue_base
  type: number
- description: Ownership structure of the account. 1 = Public, 2 = Private, 3 = Subsidiary, 4 = Other.
  name: ownershipcode
  type: integer
- description: Category describing the relationship between the account and the organization. 1=Competitor, 2=Consultant, 3=Customer, 4=Investor, 5=Partner, 6=Influencer, 7=Press, 8=Prospect, 9=Reseller, 10=Supplier
  name: customertypecode
  type: integer
- description: Legal designation or other business type of the account.
  name: businesstypecode
  type: integer
- description: Standard Industrial Classification (SIC) code.
  name: sic
  type: string
- description: Stock exchange symbol for the account.
  name: tickersymbol
  type: string
- description: Stock exchange at which the account is listed.
  name: stockexchange
  type: string
- description: Number of shares available to the public.
  name: sharesoutstanding
  type: integer
- description: Market capitalization of the account.
  name: marketcap
  type: number
- description: Credit limit of the account.
  name: creditlimit
  type: number
- description: Whether the credit for the account is on hold.
  name: creditonhold
  type: boolean
- description: Payment terms for the account. 1 = Net 30, 2 = 2% 10 Net 30, 3 = Net 45, 4 = Net 60.
  name: paymenttermscode
  type: integer
- description: Preferred method of contact. 1 = Any, 2 = Email, 3 = Phone, 4 = Fax, 5 = Mail.
  name: preferredcontactmethodcode
  type: integer
- description: Whether the account allows direct email.
  name: donotemail
  type: boolean
- description: Whether the account allows phone calls.
  name: donotphone
  type: boolean
- description: Whether the account allows faxes.
  name: donotfax
  type: boolean
- description: Whether the account allows direct mail.
  name: donotpostalmail
  type: boolean
- description: Whether the account allows bulk email through campaigns.
  name: donotbulkemail
  type: boolean
- description: Whether the account accepts marketing materials.
  name: donotsendmm
  type: boolean
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
- description: Primary address type. 1 = Bill To, 2 = Ship To, 3 = Primary, 4 = Other.
  name: address1_addresstypecode
  type: integer
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
- description: Status of the account. 0 = Active, 1 = Inactive. Inactive accounts are read-only.
  name: statecode
  type: integer
- description: Status reason for the account. 1 = Active, 2 = Inactive.
  name: statuscode
  type: integer
- description: Date and time when the account record was created.
  name: createdon
  type: string
- description: Date and time when the account record was last updated.
  name: modifiedon
  type: string
- description: Version number of the account record.
  name: versionnumber
  type: integer
- description: Lookup property for the primary contact of the account.
  name: _primarycontactid_value
  type: string
- description: Lookup property for the parent account.
  name: _parentaccountid_value
  type: string
- description: Lookup property for the user or team assigned to manage the record.
  name: _ownerid_value
  type: string
- description: Lookup property for the currency associated with the record.
  name: _transactioncurrencyid_value
  type: string
- description: Phonetic spelling of the company name for Japanese pronunciation.
  name: yominame
  type: string
provider_name: Microsoft Power Apps
provider_slug: microsoft-power-apps
schema_file: json-schema/microsoft-power-apps-dataverse-web-account-schema.json
slug: microsoft-power-apps-dataverse-web-account
tags:
- Business Applications
- Cloud
- Enterprise
- Low-Code
- Microsoft
- No-Code
- Power Platform
- SaaS
title: Account
---
