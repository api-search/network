---
aid: amazon-web-services:amazon-web-services-amazonwebservicesupdateserverengineattributes
name: Updateserverengineattributes
tags:
- API
humanURL: 
properties: []
description: >-
  Updates engine-specific attributes on a specified server. The server enters the MODIFYING state when this operation is in progress. Only one update can occur at a time. You can use this command to reset a Chef server's public key (CHEF_PIVOTAL_KEY) or a Puppet server's admin password (PUPPET_ADMIN_PASSWORD).   This operation is asynchronous.   This operation can only be called for servers in HEALTHY or UNHEALTHY states. Otherwise, an InvalidStateException is raised. A ResourceNotFoundExceptio...

---
