---
aid: hashicorp:hashicorp-postsyspluginsreloadbackend
name: Reload mounted plugin backends.
tags:
- system
humanURL: 
properties: []
description: >-
  Either the plugin name (`plugin`) or the desired plugin backend mounts (`mounts`) must be provided, but not both. In the case that the plugin name is provided, all mounted paths that use that plugin backend will be reloaded.  If (`scope`) is provided and is (`global`), the plugin(s) are reloaded globally.

---
