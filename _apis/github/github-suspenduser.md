---
aid: github:github-suspenduser
name: Suspend User
tags:
- Suspend
- Users
humanURL: 
properties: []
description: >-
  If your GitHub instance uses [LDAP Sync with Active Directory LDAP servers](https://docs.github.com/enterprise-server@3.9/admin/identity-and-access-management/using-ldap-for-enterprise-iam/using-ldap), Active Directory LDAP-authenticated users cannot be suspended through this API. If you attempt to suspend an Active Directory LDAP-authenticated user through this API, it will return a `403` response.  You can suspend any user account except your own.  Note that, if you choose not to pass any p...

---
