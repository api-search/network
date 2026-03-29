---
aid: amazon-web-services:amazon-web-services-amazonwebservicesfinalizecutover
name: Finalizecutover
tags:
- API
humanURL: 
properties: []
description: >-
  Finalizes the cutover immediately for specific Source Servers. All AWS resources created by Application Migration Service for enabling the replication of these source servers will be terminated / deleted within 90 minutes. Launched Test or Cutover instances will NOT be terminated. The AWS Replication Agent will receive a command to uninstall itself (within 10 minutes). The following properties of the SourceServer will be changed immediately: dataReplicationInfo.dataReplicationState will be ch...

---
