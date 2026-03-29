---
aid: bigcommerce:bigcommerce-createpage
name: Create a Page
tags:
- Pages
humanURL: 
properties: []
description: >-
  Creates a *Page*. The request payload limit is 1MB.  **Required Fields** *   `type` *   `name` *   `link` (for a page of `type: link`) *   `feed` (for a page of `type: rss_feed`) *   `body` (for a page of `type: raw`)  **Read Only Fields** *   `id`  ## Content Type  The default value for `content_type` is `text/html`; however, if `page_type` is set to `raw`, `content_type` can be changed to `text/javascript` or `application/json`. Updating this field allows you to place a JavaScript or a JSON...

---
