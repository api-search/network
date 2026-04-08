---
aid: sendgrid:sendgrid-updateteammate
name: Update teammate's permissions
tags:
- Teammates
humanURL: 
properties: []
description: >-
  **This endpoint allows you to update a teammate’s permissions.**  To turn a teammate into an admin, the request body should contain an `is_admin` set to `true`. Otherwise, set `is_admin` to `false` and pass in all the scopes that a teammate should have.  **Only the parent user or other admin teammates can update another teammate’s permissions.**  **Admin users can only update permissions.**

---
