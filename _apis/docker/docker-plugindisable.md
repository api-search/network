---
aid: docker:docker-plugindisable
name: Plugin Disable
tags:
- Plugin
- Disables
humanURL: 
properties: []
description: >-
  Disables an active Docker plugin by its name, allowing administrators to deactivate plugin functionality without completely removing it from the system. This operation accepts the plugin name as a path parameter and optionally supports a force parameter to disable the plugin even if it's currently in use by containers or other resources. When successfully executed, the plugin transitions to a disabled state where it no longer provides its capabilities to the Docker daemon, but remains install...

---
