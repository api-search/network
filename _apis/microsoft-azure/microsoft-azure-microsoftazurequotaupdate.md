---
aid: microsoft-azure:microsoft-azure-microsoftazurequotaupdate
name: Microsoft Azure Patch Subscriptions Subscriptionid Providers Microsoft Capacity Resourceproviders Providerid Locations Location Servicelimits Resourcename
tags:
- QuotaInformation
humanURL: 
properties: []
description: >-
  Update the service limits (quota) of a resource to requested value.<br> Steps:<br>  1. Make the Get request to get the quota information for specific resource.<br>  2. To increase the quota, update the limit field in the response from Get request to new value.<br>  3. Submit the JSON to the quota request API to update the quota.<br>  The Update quota request may be constructed as follows. The PATCH operation can be used to update the quota.

---
