---
aid: algolia:algolia-getuserscount
name: Retrieve number of users
tags:
- analytics
- - Users
  - Count
  - Analytics
humanURL: 
properties: []
description: >-
  Retrieves the number of unique users within a time range, including a daily breakdown.  Since it returns the number of unique users, the sum of the daily values might be different from the total number.  By default:  - Algolia distinguishes search users by their IP address, _unless_ you include a pseudonymous user identifier in your search requests with the `userToken` API parameter or `x-algolia-usertoken` request header. - The analyzed period includes the last eight days including the curre...

---
