---
aid: docker:docker-volumecreate
name: Volume Create
tags:
- Volume
- Create
humanURL: 
properties: []
description: >-
  Creates a new Docker volume with the specified name and driver options. This endpoint accepts a JSON payload containing volume configuration parameters such as the volume name, driver type (defaulting to 'local' if not specified), driver-specific options, and labels for metadata. Upon successful creation, it returns a 201 status code along with the volume object containing details like the volume name, driver, mount point, creation timestamp, and any associated labels or options. If a volume ...

---
