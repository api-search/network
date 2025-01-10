---
aid: ovh-cloud:ovh-cloud-snapshot-api
name: OVH Cloud Snapshot  API
tags:
  - Servers
  - Cloud
  - Compute
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: |-

  https://api.us.ovhcloud.com/console/?section=%2Fdedicated%2Fserver&branch=v1
properties:
  - url: openapi/ovh-cloud-snapshot-api-openapi.yml
    type: OpenAPI
  - url: >-
      https://help.ovhcloud.com/csm/en-public-cloud-storage-nas-snapshots-api?id=kb_article_view&sysparm_article=KB0046777
    type: Documentation
description: >-
  The OVH Cloud Snapshot API allows users to easily create, manage, and restore
  snapshots of their virtual server instances. With this API, users can schedule
  and automate the process of taking snapshots, which are essentially a
  point-in-time copy of the server's data and configuration. These snapshots can
  be used to back up important files and settings, as well as to quickly restore
  the server to a previous state in case of data loss or system failure. The API
  provides a convenient way for users to protect their data and ensure the
  availability of their server instances.

---