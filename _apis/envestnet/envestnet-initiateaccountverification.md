---
aid: envestnet:envestnet-initiateaccountverification
name: Verify Accounts Using Transactions
tags:
- Verify Account
humanURL: 
properties: []
description: >-
  The verify account service is used to verify the account's ownership by  matching the transaction details with the accounts aggregated for the user.<br><ul><li>If a match is identified, the service returns details of all the accounts along with the matched transaction's details.<li>If no transaction match is found, an empty response will be returned.<li>A maximum of 5 transactionCriteria can be passed in a request.<li>The baseType, date, and amount parameters should mandatorily be passed.<li>...

---
