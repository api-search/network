---
aid: cloudflare:cloudflare-custom-hostname-for-a-zone-create-custom-hostname
name: Create Custom Hostname
tags:
- - - - - - - Custom Hostname for a Zone
humanURL: 
properties: []
description: >-
  Add a new custom hostname and request that an SSL certificate be issued for it. One of three validation methods—http, txt, email—should be used, with 'http' recommended if the CNAME is already in place (or will be soon). Specifying 'email' will send an email to the WHOIS contacts on file for the base domain plus hostmaster, postmaster, webmaster, admin, administrator. If http is used and the domain is not already pointing to the Managed CNAME host, the PATCH method must be used once it is (to...

---
