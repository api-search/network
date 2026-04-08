---
aid: microsoft-azure:microsoft-azure-microsoftazurecomponentspurge
name: Microsoft Azure Post Subscriptions Subscriptionid Resourcegroups Resourcegroupname Providers Microsoft Insights Components Resourcename Purge
tags:
- Subscriptions
humanURL: 
properties: []
description: >-
  Purges data in an Application Insights component by a set of user-defined filters.<br><br>In order to manage system resources, purge requests are throttled at 50 requests per hour. You should batch the execution of purge requests by sending a single command whose predicate includes all user identities that require purging. Use the in operator to specify multiple identities. You should run the query prior to using for a purge request to verify that the results are expected.

---
