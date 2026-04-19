---
description: Contains the cookie settings for a configuration.
layout: schema
name: cookie-settings
properties_list:
- description: Choose the type of domain. The default recommended type is `automatic`. Otherwise, choose `fqdn` to use the current Fully Qualified Domain name, `legacy` to use the original way in which the domain wa
  name: cookieDomain
  type: string
- description: If all of your traffic uses HTTPS, specify `true`. This option sets the Secure flag on all security product cookies, which are then only included with HTTPS traffic. It also adds `SameSite=None` to mo
  name: useAllSecureTraffic
  type: boolean
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-cookie-settings-schema.json
slug: api-security-cookie-settings
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: cookie-settings
---
