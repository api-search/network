---
aid: amazon-web-services:glacier
name: Amazon S3 Glacier
tags:
  - Access
  - Accounts
  - Archive
  - Archives
  - Capacity
  - Complete
  - Configurations
  - Data
  - Describe
  - Initiate
  - Jobs
  - Locks
  - Multipart
  - Names
  - Notifications
  - Output
  - Policies
  - Provisioned
  - Purchase
  - Removes
  - Retrieval
  - Sets
  - Tags
  - Uploads
  - Vault
  - Vaults
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/s3/storage-classes/glacier/
overlays:
  - url: overlays/glacier-openapi-search.yml
    type: APIs.io Search
  - url: overlays/glacier-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/s3/storage-classes/glacier/
    type: Documentation
  - url: properties/glacier-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/s3/storage-classes/glacier/instant-retrieval/
    type: Instant-retrieval
description: >-
  Amazon S3 Glacier (Glacier) is a cost-effective storage solution designed for
  long-term storage of infrequently accessed data. It provides secure, durable,
  and easy-to-use storage for data backup and archival purposes. With Glacier,
  users can store data for extended periods without worrying about capacity
  planning or hardware management. Glacier is ideal for when low storage costs
  are a priority and data retrieval is rare. For applications requiring fast or
  frequent access to data, Amazon S3 is recommended. Users can store data in any
  format without limits on the total amount of data stored in Glacier. 

---