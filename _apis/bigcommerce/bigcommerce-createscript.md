---
aid: bigcommerce:bigcommerce-createscript
name: Create a Script
tags:
- Scripts
humanURL: 
properties: []
description: >-
  Creates a *Script*.  **Required Fields** * name  **Read Only Fields** * uuid  **Limits** * 50 scripts per channel.  **Notes** * If the `kind` is `src`:   * Specify the `src` property.    * Optionally, you can supply a `load_method`.    * Do not specify the `html` field. * If the `kind` is `script_tag`:   * Specify the `html` property.   * Do not specify the `src` field. * Each app can have 10 scripts installed. * Multiple scripts can be created [per call](/docs/integrations/scripts#notes).

---
