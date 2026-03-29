---
aid: etcd:etcd-leasegrant
name: Grant a lease
tags:
- Lease
humanURL: 
properties: []
description: >-
  Creates a new lease with the specified TTL in seconds. The returned lease ID can be attached to key-value pairs so they are automatically deleted when the lease expires. Clients must periodically renew the lease using the keepalive endpoint to prevent expiration. The ID field can be set to 0 to allow etcd to assign a lease ID automatically.

---
