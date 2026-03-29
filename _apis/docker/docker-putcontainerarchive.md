---
aid: docker:docker-putcontainerarchive
name: Put Container Archive
tags:
- Put
- Containers
- Archive
humanURL: 
properties: []
description: >-
  Uploads a tar archive containing files and directories to be extracted into a specified path within a container's filesystem. The archive is extracted at the path specified in the query parameter, with the ability to overwrite existing files and directories. This operation allows you to modify the contents of a running or stopped container by injecting new files or replacing existing ones. The container must exist, and the target path must be a valid directory within the container's filesyste...

---
