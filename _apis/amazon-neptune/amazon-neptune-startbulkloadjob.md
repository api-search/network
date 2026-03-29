---
aid: amazon-neptune:amazon-neptune-startbulkloadjob
name: Start a bulk data load job from S3
tags:
- Loader
humanURL: 
properties: []
description: >-
  Initiates a bulk data loading job from Amazon S3 into the Neptune database. The source data can be in CSV format for property graphs or in N-Triples, N-Quads, RDF/XML, or Turtle formats for RDF data. The loader requires an IAM role with access to the S3 bucket. Neptune queues up to 64 jobs in FIFO order when queueRequest is enabled.

---
