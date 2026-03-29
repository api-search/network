---
aid: etcd:etcd-maintenancealarm
name: Manage cluster alarms
tags:
- Maintenance
humanURL: 
properties: []
description: >-
  Manages cluster-level alarms that indicate error conditions such as insufficient storage space (NOSPACE). Supports activating alarms, deactivating (disarming) alarms, and listing all active alarms. When a NOSPACE alarm is active, the cluster becomes read-only to prevent data loss. After addressing the underlying issue, the alarm must be explicitly deactivated to restore write access.

---
