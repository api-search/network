---
aid: plaid:plaid-identityget
name: Plaid Retrieve identity data
tags:
- Plaid
humanURL: 
properties: []
description: >-
  The `/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses. Only name data is guaranteed to be returned; other fields will be empty arrays if not provided by the institution.  This request may take some time to complete if identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retriev...

---
