---
aid: vtex:vtex-removerolefromuser
name: VTex Remove role from user or appKey
tags:
- Roles
humanURL: 
properties: []
description: >-
  Allows you to remove a License Manager [role](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) from a specific user or application key. This method only allows the removal of one role per request. The role's ID must be specified on the request path, not on the request body.  > Note that a successful response returns a `204` response with an empty body. A deletion on a role or user that does not exist will also return a `204`. Thus, this method should not be used to verify th...

---
