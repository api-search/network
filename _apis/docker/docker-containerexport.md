---
aid: docker:docker-containerexport
name: Container Export
tags:
- Containers
- Exports
humanURL: 
properties: []
description: >-
  This operation exports a Docker container's filesystem as a tar archive. When you make a GET request to this endpoint with a specific container ID, Docker bundles the entire filesystem of that container into a tarball stream, which can be saved to a file or piped to another process. This is useful for backing up container filesystems, analyzing their contents, or transferring them between systems. The exported archive contains only the filesystem contents and does not include the container's ...

---
