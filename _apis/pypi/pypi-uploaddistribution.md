---
aid: pypi:pypi-uploaddistribution
name: Upload a distribution file
tags:
- Upload
humanURL: 
properties: []
description: >-
  Uploads a Python package distribution file (source distribution or wheel) to PyPI. The request must use multipart/form-data encoding and include the distribution file as the content part along with package metadata as form fields. Authentication is required via HTTP Basic Auth using the username __token__ and an API token as the password, or via a short-lived token obtained through Trusted Publishing. PEP 740 attestations may optionally be attached for supply chain integrity verification.

---
