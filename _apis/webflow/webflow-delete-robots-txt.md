---
aid: webflow:webflow-delete-robots-txt
name: Webflow Delete robots.txt
tags:
- Sites
humanURL: 
properties: []
description: >-
  Remove specific rules for a user-agent in your `robots.txt` file. To delete all rules for a user-agent, provide an empty rule set. This will remove the user-agent's entry entirely, leaving it subject to your site's default crawling behavior.  **Note:** Deleting a user-agent with no rules will make the user-agent's access unrestricted unless other directives apply.  <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>  Required scope: `site_config:write`

---
