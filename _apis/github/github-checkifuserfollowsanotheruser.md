---
aid: github:github-checkifuserfollowsanotheruser
name: Check If User Follows Another User
tags:
- Checks
- Users
- Follows
- Another
humanURL: 
properties: []
description: >-
  This API endpoint allows you to check whether a specified GitHub user (username) is following another user (target_user). It performs a GET request to the path /users/{username}/following/{target_user}, where you replace {username} with the user you want to check and {target_user} with the user they might be following. The endpoint returns a 204 No Content status if the user does follow the target user, or a 404 Not Found status if they do not, making it a simple boolean check for following r...

---
