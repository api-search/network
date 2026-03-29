---
aid: envestnet:envestnet-deleteuserviewrule
name: Delete the specified rules for a specific view.
tags:
- View
humanURL: 
properties: []
description: >-
  The delete rules API allows you to delete one or more rules that are associated with a specific view by passing the viewId and ruleId. The HTTP response code is 204 (Success without content). <br><br>   Important notes-   <ul>   <li>Using this API you cannot delete all Rules of a View. Meaning if a View has 5 Rules, using this API you can delete maximum of 4 rules only. Reason- A view has no meaning without a Rule. If you want to delete all Rules, consider Deleting the views itself by calling...

---
