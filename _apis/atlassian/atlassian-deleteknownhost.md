---
aid: atlassian:atlassian-deleteknownhost
name: Delete Known Host
tags:
- Delete
- Known
- Hosts
humanURL: 
properties: []
description: >-
  This API operation removes a specific SSH known host entry from a Bitbucket repository's Pipelines configuration by providing the workspace identifier, repository slug, and the unique UUID of the known host to be deleted. Known hosts are SSH server fingerprints that Pipelines uses to verify the identity of remote servers during SSH connections, and deleting a known host entry means that the repository's pipeline will no longer have that server's SSH key fingerprint stored for authentication p...

---
