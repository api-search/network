---
aid: envestnet:envestnet-getuserviewrecommendations
name: Fetch recommended Views for a user.
tags:
- View
humanURL: 
properties: []
description: >-
  This API fetches the recommended Views for a specific user. For each user, their transaction history for 90 days is considered based on which recommendations are generated. The recommendations contain meta-data as well as the exact View object that can be passed to the POST /views API endpoint to create a View.<br><br>   Note- The recommendationId field is used to make sure that the same view is not recommended again for the user. If you modify the recommendationId or let users edit a View ma...

---
