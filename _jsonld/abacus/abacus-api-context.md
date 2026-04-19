---
class_count: 8
classes:
- Expense
- ExpenseListResponse
- InviteMemberRequest
- Member
- MemberListResponse
- OAuthTokenRequest
- OAuthTokenResponse
- UpdateMemberRequest
context_file: json-ld/abacus-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/json-ld/abacus-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Abacus Api from Abacus.
layout: jsonld
name: Abacus Api Context
namespaces:
- prefix: abacus
  uri: https://api.abacus.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: set
  name: expenses
  type: ''
- container: ''
  name: total
  type: integer
- container: ''
  name: page
  type: integer
- container: ''
  name: perPage
  type: integer
- container: ''
  name: email
  type: ''
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: role
  type: string
- container: ''
  name: department
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: memberId
  type: string
- container: ''
  name: amount
  type: decimal
- container: ''
  name: currency
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: description
  type: ''
- container: ''
  name: date
  type: date
- container: ''
  name: status
  type: string
- container: ''
  name: receiptUrl
  type: ''
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: grantType
  type: string
- container: ''
  name: clientId
  type: string
- container: ''
  name: clientSecret
  type: string
- container: set
  name: members
  type: ''
- container: ''
  name: accessToken
  type: string
- container: ''
  name: tokenType
  type: string
- container: ''
  name: expiresIn
  type: integer
property_count: 27
provider_name: Abacus
provider_slug: abacus
slug: abacus-api-context
tags:
- Accounting
- Expense Management
- Finance
- Reimbursement
- JSON-LD
- Linked Data
- Semantic Web
---
