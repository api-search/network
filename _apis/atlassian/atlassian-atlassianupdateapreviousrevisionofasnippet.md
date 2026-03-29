---
aid: atlassian:atlassian-atlassianupdateapreviousrevisionofasnippet
name: Update A Previous Revision Of A Snippet
tags:
- Snippets
humanURL: 
properties: []
description: >-
  Identical to `UPDATE /snippets/encoded_id`, except that this endpoint<br>takes an explicit commit revision. Only the snippet's "HEAD"/"tip"<br>(most recent) version can be updated and requests on all other,<br>older revisions fail by returning a 405 status.<br><br>Usage of this endpoint over the unrestricted `/snippets/encoded_id`<br>could be desired if the caller wants to be sure no concurrent<br>modifications have taken place between the moment of the UPDATE<br>request and the original GET....

---
