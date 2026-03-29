---
aid: github:github-createuser
name: Create User
tags:
- Create
- Users
humanURL: 
properties: []
description: >-
  If an external authentication mechanism is used, the login name should match the login name in the external system. If you are using LDAP authentication, you should also [update the LDAP mapping](https://docs.github.com/enterprise-server@3.9/rest/enterprise-admin/ldap#update-ldap-mapping-for-a-user) for the user.  The login name will be normalized to only contain alphanumeric characters or single hyphens. For example, if you send `"octo_cat"` as the login, a user named `"octo-cat"` will be cr...

---
